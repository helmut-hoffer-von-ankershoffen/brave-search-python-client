"""Provides a Python client for the Brave Search API."""

import json
import os
import pathlib
from typing import Any
from urllib.parse import urljoin, urlparse

import httpx
from tenacity import AsyncRetrying, RetryError, stop_after_attempt, wait_fixed

from brave_search_python_client.constants import (
    BASE_URL,
    DEFAULT_RETRY_WAIT_TIME,
    MOCK_API_KEY,
    __version__,
)

from .requests import (
    ImagesSearchRequest,
    NewsSearchRequest,
    SearchType,
    VideosSearchRequest,
    WebSearchRequest,
)
from .responses import (
    BraveSearchAPIError,
    BraveSearchClientError,
    ImageSearchApiResponse,
    NewsSearchApiResponse,
    VideoSearchApiResponse,
    WebSearchApiResponse,
)


class BraveSearch:
    """
    A python client for the Brave Search API.

    Provides access to all search types (web, images, news and videos).
    """

    def __init__(self, api_key: str | None = None) -> None:
        """
        Initialize the Brave Search client.

        Args:
            api_key: API key for authentication with API (https://brave.com/search/api/).
                If not given as argument looks for BRAVE_SEARCH_API_KEY in environment.
                If the key is set to brave_search_python_client.MOCK_API_KEY,
                the client will return mock data for integration testing purposes.

        Raises:
            BraveSearchClientError: Raised if no API key given or found in environment.

        """
        self._api_key = api_key or os.environ.get("BRAVE_SEARCH_API_KEY", "NA")
        if self._api_key == "NA":
            msg = (
                "API key must be given as argument when constructing BraveSearch "
                "python client or as variable BRAVE_SEARCH_API_KEY in environment."
            )
            raise BraveSearchClientError(msg)

        self._base_url = BASE_URL

        self._headers = {
            "X-Subscription-Token": self._api_key,
            "Accept": "application/json",
            "Accept-Encoding": "gzip",
            "Cache-Control": "no-cache",
        }
        self._headers["User-Agent"] = f"brave-search-python-client/{__version__}"

    async def _get(
        self,
        search_type: SearchType,
        params: dict[str, Any] | None = None,
        retries: int = 0,
        wait_time: int = DEFAULT_RETRY_WAIT_TIME,
    ) -> httpx.Response:
        """
        Awaitable async HTTP/GET to Brave Search API with auth and optional retries.

        Args:
            search_type: Type of search (web, images, news or videos).
            params: Query parameters for the httpx.get request.
            retries: Number of retries for failures. Default is 0.
            wait_time: Time to wait between retries in seconds. Default is 2.

        Returns:
            httpx.Response: Awaitable response object from the HTTP/GET request.

        Raises:
            BraveSearchAPIError: If API request fails.

        """
        url = urljoin(self._base_url, f"{search_type}/search")

        if retries == 0:
            try:
                async with httpx.AsyncClient() as client:
                    return (await client.get(url, headers=self._headers, params=params)).raise_for_status()
            except httpx.HTTPError as http_error:
                msg = f"Failed to get API response with {http_error}"
                raise BraveSearchAPIError(
                    msg,
                ) from http_error

        # In case you really want to retry
        try:
            async for attempt in AsyncRetrying(
                stop=stop_after_attempt(retries),
                wait=wait_fixed(wait_time),
            ):
                with attempt:
                    async with httpx.AsyncClient() as client:
                        return (await client.get(url, headers=self._headers, params=params)).raise_for_status()
            msg = f"Failed to get API response after {retries} retries with {wait_time} seconds wait time"
            raise BraveSearchAPIError(
                msg,
            )  # pragma: no cover
        except RetryError as retry_error:
            raise BraveSearchAPIError(
                retry_error.last_attempt.exception(),
            ) from retry_error

    @staticmethod
    def _load_mock_data(search_type: SearchType) -> dict[str, Any]:
        """
        Load mock data for testing purposes.

        Returns:
            dict[str, Any]: Mock data for the specified search type.

        """
        # Get package root directory
        package_root = pathlib.Path(__file__).parent
        mock_path = package_root / f"responses/mock_data/{search_type}.json"

        with mock_path.open(encoding="utf-8") as f:
            return json.load(f)

    @staticmethod
    def _dump_response(response: httpx.Response) -> None:
        """Dump API response to a file."""
        pathlib.Path("response.json").write_text(response.text, encoding="utf-8")

    async def web(
        self,
        request: WebSearchRequest,
        retries: int = 0,
        wait_time: int = DEFAULT_RETRY_WAIT_TIME,
        dump_response: bool = False,
    ) -> WebSearchApiResponse:
        """
        Execute a web search query using the Brave Search API.

        For details see: https://api.search.brave.com/app/documentation/web-search/query

        Args:
            request (WebSearchRequest): request object with query parameters.
            retries (int): Number of retries to be attempted in case of failure.
                Default is 0.
            wait_time (int): Time to wait between retries. Default is 2 seconds.
            dump_response (bool): Whether to dump the original response. If enabled
                will be dumped into response.json in current working directory.

        Returns:
            WebSearchApiResponse: Top level response model for successful Web Search
                API requests. The response includes relevant keys based on plan,
                query relevance and result_filter parameters.

        Raises:
            BraveSearchAPIError: If API request fails or returns an error.

        """
        # For integration testing purposes, if API key is MOCK, load from mock data
        if self._api_key == MOCK_API_KEY:
            return WebSearchApiResponse.model_validate(
                self._load_mock_data(SearchType.web),
            )

        response = await self._get(
            SearchType.web,
            params=request.model_dump(exclude_none=True),
            retries=retries,
            wait_time=wait_time,
        )

        if dump_response:
            self._dump_response(response)

        return WebSearchApiResponse.model_validate(response.json())

    async def images(
        self,
        request: ImagesSearchRequest,
        retries: int = 0,
        wait_time: int = DEFAULT_RETRY_WAIT_TIME,
        dump_response: bool = False,
    ) -> ImageSearchApiResponse:
        """
        Execute an image search query using the Brave Search API.

        Args:
            request (ImagesSearchRequest): request object with query parameters.
            retries (int): Number of retries to be attempted in case of failure. Default is 0.
            wait_time (int): Time to wait between retries. Default is 2 seconds.
            dump_response (bool): Whether to dump the original response. If enabled, it will be dumped
                                 into response.json in current working directory.

        Returns:
            ImageSearchApiResponse: Top-level response model for successful Image Search API requests.
                The API can also respond back with an error response based on invalid subscription
                keys and rate limit events
                (https://api.search.brave.com/app/documentation/image-search/responses).

        Raises:
            BraveSearchAPIError: If the API response fails after retries.

        """
        # For integration testing purposes, if API key is MOCK, load from mock data
        if self._api_key == MOCK_API_KEY:
            return ImageSearchApiResponse.model_validate(
                self._load_mock_data(SearchType.images),
            )

        response = await self._get(
            SearchType.images,
            params=request.model_dump(exclude_none=True),
            retries=retries,
            wait_time=wait_time,
        )

        if dump_response:
            self._dump_response(response)

        return ImageSearchApiResponse.model_validate(response.json())

    async def videos(
        self,
        request: VideosSearchRequest,
        retries: int = 0,
        wait_time: int = DEFAULT_RETRY_WAIT_TIME,
        dump_response: bool = False,
    ) -> VideoSearchApiResponse:
        """
        Execute a video search query using the Brave Search API.

        Returns:
            VideoSearchApiResponse: Top level response model for successful Video Search API requests.
            The API can also respond back with an error response based on invalid subscription keys
            and rate limit events. See: https://api.search.brave.com/app/documentation/news-search/responses

        Raises:
            ValueError: If query validation fails.
            BraveSearchAPIError: If API request fails.

        """
        # For integration testing purposes, if API key is MOCK, load from mock data
        if self._api_key == MOCK_API_KEY:
            return VideoSearchApiResponse.model_validate(
                self._load_mock_data(SearchType.videos),
            )

        response = await self._get(
            SearchType.videos,
            params=request.model_dump(exclude_none=True),
            retries=retries,
            wait_time=wait_time,
        )

        if dump_response:
            self._dump_response(response)

        return VideoSearchApiResponse.model_validate(response.json())

    async def news(
        self,
        request: NewsSearchRequest,
        retries: int = 0,
        wait_time: int = DEFAULT_RETRY_WAIT_TIME,
        dump_response: bool = False,
    ) -> NewsSearchApiResponse:
        """
        Execute a news search query using the Brave Search API.

        Args:
            request (NewsSearchRequest): request object with query parameters.
            retries (int): Number of retries to be attempted in case of failure. Default is 0.
            wait_time (int): Time to wait between retries. Default is 2 seconds.
            dump_response (bool): Whether to dump the original response. If enabled will be dumped
            into response.json in current working directory.

        Returns:
            NewsSearchApiResponse: Top level response model for successful News Search API requests.
            The API can also respond back with an error response based on invalid subscription keys
            and rate limit events. See: https://api.search.brave.com/app/documentation/news-search/responses

        Raises:
            ValueError: If query validation fails.
            BraveSearchAPIError: If API request fails or returns an error.

        """
        # For integration testing purposes, if API key is MOCK, load from mock data
        if self._api_key == MOCK_API_KEY:
            return NewsSearchApiResponse.model_validate(
                self._load_mock_data(SearchType.news),
            )

        response = await self._get(
            SearchType.news,
            params=request.model_dump(exclude_none=True),
            retries=retries,
            wait_time=wait_time,
        )

        if dump_response:
            self._dump_response(response)

        return NewsSearchApiResponse.model_validate(response.json())

    @staticmethod
    async def is_connected() -> bool:
        """
        Check if the Brave Search API is accessible. Important: This does not check if the API key is valid.

        Returns:
            bool: True if API is accessible, False otherwise.

        """
        parsed = urlparse(BASE_URL)
        api_url = f"{parsed.scheme}://{parsed.netloc}/"
        try:
            async with httpx.AsyncClient() as client:
                response = await client.head(api_url, timeout=5)
                return response.status_code in {200, 303}
        except httpx.HTTPError:
            return False
