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
    """A python client for the Brave Search API that provides access to all search types (web, images, news and videos).

    Args:
        api_key: API key for authentication with API (https://brave.com/search/api/). If not given as argument looks for BRAVE_SEARCH_API_KEY in environment. If the key is set to brave_search_python_client.MOCK_API_KEY, the client will return mock data for integration testing purposes.

    Raises:
        BraveSearchClientError: Raised if no API key given or found in environment.
    """

    def __init__(self, api_key: str | None = None) -> None:
        self._api_key = api_key or os.environ.get("BRAVE_SEARCH_API_KEY", "NA")
        if self._api_key == "NA":
            raise BraveSearchClientError(
                "API key must be given as argument when constructing BraveSearch python client or as variable BRAVE_SEARCH_API_KEY in environment."
            )
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
        retries=0,
        wait_time=DEFAULT_RETRY_WAIT_TIME,
    ) -> httpx.Response:
        """
        Awaitable async HTTP/GET to Brave Search API with authentication and optional retries.

        Args:
            search_type: Type of search to be performed (web, images, news or videos).
            params: Query parameters for the httpx.get request.
            retries: Number of retries to be attempted in case of failure. Default is 0.
            wait_time: Time to wait between retries. Default is 2 seconds.

        Returns:
            httpx.Response: Awaitable response object from the HTTP/GET request.

        Raises:
            BraveSearchAPIError: If API request fails.

        """
        url = urljoin(self._base_url, f"{search_type}/search")

        if retries == 0:
            try:
                async with httpx.AsyncClient() as client:
                    return (
                        await client.get(url, headers=self._headers, params=params)
                    ).raise_for_status()
            except httpx.HTTPError as http_error:
                raise BraveSearchAPIError(
                    f"Failed to get API response with {http_error}"
                ) from http_error

        # In case you really want to retry
        try:
            async for attempt in AsyncRetrying(
                stop=stop_after_attempt(retries), wait=wait_fixed(wait_time)
            ):
                with attempt:
                    async with httpx.AsyncClient() as client:
                        return (
                            await client.get(url, headers=self._headers, params=params)
                        ).raise_for_status()
            raise BraveSearchAPIError(
                f"Failed to get API response after {retries} retries with {wait_time} seconds wait time"
            )  # pragma: no cover
        except RetryError as retry_error:
            raise BraveSearchAPIError(
                retry_error.last_attempt.exception()
            ) from retry_error

    def _load_mock_data(self, search_type: SearchType):
        """Helper method to load mock data for testing purposes."""

        # Get package root directory
        package_root = pathlib.Path(__file__).parent
        mock_path = package_root / f"responses/mock_data/{search_type}.json"

        with open(mock_path) as f:
            return json.load(f)

    def _dump_response(self, response: httpx.Response) -> None:
        """Helper method to dump API response to a file."""
        with open("response.json", "w") as f:
            f.write(response.text)

    async def web(
        self,
        request: WebSearchRequest,
        retries: int = 0,
        wait_time: int = DEFAULT_RETRY_WAIT_TIME,
        dump_response: bool = False,
    ) -> WebSearchApiResponse:
        """Execute a web search query using the Brave Search API (https://api.search.brave.com/app/documentation/web-search/query#WebSearchAPIQueryParameters).

        Args:
            request: WebSearchRequest object with query parameters.
            retries: Number of retries to be attempted in case of failure. Default is 0.
            wait_time: Time to wait between retries. Default is 2 seconds.
            dump_response = Whether to dump the original response. If enabled will be dumped into response.json in current working directory.

        Returns:
            WebSearchResponse: Top level response model for successful Web Search API requests. The response will include the relevant keys based on the plan subscribed, query relevance or applied result_filter as a query parameter. The API can also respond back with an error response based on invalid subscription keys and rate limit events (https://api.search.brave.com/app/documentation/web-search/responses#WebSearchApiResponse).

        Raises:
            BraveSearchAPIError: If API request fails or returns an error.
        """
        # For integration testing purposes, if API key is MOCK, load from mock data
        if self._api_key == MOCK_API_KEY:
            return WebSearchApiResponse.model_validate(
                self._load_mock_data(SearchType.web)
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
        """Execute an image search query using the Brave Search API.

        Args:
            request: ImagesSearchRequest object with query parameters.
            retries: Number of retries to be attempted in case of failure. Default is 0.
            wait_time: Time to wait between retries. Default is 2 seconds.
            dump_response = Whether to dump the original response. If enabled will be dumped into response.json in current working directory.

        Returns:
            ImageSearchApiResponse: Top level response model for successful Image Search API requests. The API can also respond back with an error response based on invalid subscription keys and rate limit events (https://api.search.brave.com/app/documentation/image-search/responses).

        Raises:
            BraveSearchAPIError: If API request fails.
        """

        # For integration testing purposes, if API key is MOCK, load from mock data
        if self._api_key == MOCK_API_KEY:
            return ImageSearchApiResponse.model_validate(
                self._load_mock_data(SearchType.images)
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
        """Execute a video search query using the Brave Search API.

        Args:
            request: VideosSearchRequest object with query parameters.
            retries: Number of retries to be attempted in case of failure. Default is 0.
            wait_time: Time to wait between retries. Default is 2 seconds.
            dump_response = Whether to dump the original response. If enabled will be dumped into response.json in current working directory.

        Returns:
            VideoSearchApiResponse: Top level response model for successful Video Search API requests. The API can also respond back with an error response based on invalid subscription keys and rate limit events (https://api.search.brave.com/app/documentation/news-search/responses).

        Raises:
            ValueError: If query validation fails.
            BraveSearchAPIError: If API request fails.
        """
        # For integration testing purposes, if API key is MOCK, load from mock data
        if self._api_key == MOCK_API_KEY:
            return VideoSearchApiResponse.model_validate(
                self._load_mock_data(SearchType.videos)
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
        """Execute a news search query using the Brave Search API.

         Args:
            request: NewsSearchRequest object with query parameters.
            retries: Number of retries to be attempted in case of failure. Default is 0.
            wait_time: Time to wait between retries. Default is 2 seconds.
            dump_response = Whether to dump the original response. If enabled will be dumped into response.json in current working directory.

        Returns:
            NewsSearchApiResponse: Top level response model for successful News Search API requests. The API can also respond back with an error response based on invalid subscription keys and rate limit events (https://api.search.brave.com/app/documentation/news-search/responses).

        Raises:
            ValueError: If query validation fails.
            BraveSearchAPIError: If API request fails or returns an error.
        """
        # For integration testing purposes, if API key is MOCK, load from mock data
        if self._api_key == MOCK_API_KEY:
            return NewsSearchApiResponse.model_validate(
                self._load_mock_data(SearchType.news)
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

    async def is_connected(self) -> bool:
        """Check if the Brave Search API is accessible. Important: This does not check if the API key is valid.

        Returns:
            bool: True if API is accessible, False otherwise.
        """
        parsed = urlparse(BASE_URL)
        api_url = f"{parsed.scheme}://{parsed.netloc}/"
        try:
            async with httpx.AsyncClient() as client:
                response = await client.head(api_url, timeout=5)
                return response.status_code in (200, 303)
        except Exception:
            return False
