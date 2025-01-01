import os
from typing import Any
from urllib.parse import urljoin

import httpx
from tenacity import AsyncRetrying, RetryError, stop_after_attempt, wait_fixed

from brave_search_python_client.constants import (
    RETRY_COUNT,
    RETRY_WAIT_TIME,
)

from .requests import (
    FreshnessType,
    ImageSafeSearchType,
    ImageSearchRequest,
    NewsSafeSearchType,
    NewsSearchRequest,
    UnitsType,
    VideoSearchRequest,
    WebSafeSearchType,
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

BASE_URL = "https://api.search.brave.com/res/v1/"


class BraveSearch:
    """A python client for the Brave Search API that provides access to all search types (web, images, news and videos).

    Args:
        api_key: API key for authentication with API (https://brave.com/search/api/). If not given as argument looks for BRAVE_SEARCH_API_KEY in environment.

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
            "Accept": "application/json",
            "Accept-Encoding": "gzip",
            "X-Subscription-Token": self._api_key,
        }

    async def _get(
        self,
        search_type: str,
        params: dict[str, Any] | None = None,
        retry_count=RETRY_COUNT,
        wait_time=RETRY_WAIT_TIME,
    ) -> httpx.Response:
        """
        Async GET to Brave Search API with authentication and retries.
        """
        url = urljoin(self._base_url, f"{search_type}/search")

        try:
            async for attempt in AsyncRetrying(
                stop=stop_after_attempt(retry_count), wait=wait_fixed(wait_time)
            ):
                with attempt:
                    async with httpx.AsyncClient() as client:
                        return (
                            await client.get(url, headers=self._headers, params=params)
                        ).raise_for_status()
            raise BraveSearchAPIError(
                f"Failed to get API response after {retry_count} retries with {wait_time} seconds wait time"
            )  # pragma: no cover
        except RetryError as retry_error:
            raise BraveSearchAPIError(
                retry_error.last_attempt.exception()
            ) from retry_error

    async def web_search(
        self,
        q: str,
        country: str = "US",
        search_lang: str = "en",
        ui_lang: str = "en-US",
        count: int = 20,
        offset: int = 0,
        safesearch: WebSafeSearchType = WebSafeSearchType.moderate,
        freshness: FreshnessType | None = None,
        text_decorations: bool = True,
        spellcheck: bool = True,
        result_filter: str | None = None,
        goggles_id: str | None = None,
        units: UnitsType | None = None,
        extra_snippets: bool = False,
        summary: bool = False,
        dump_response: bool = False,
    ) -> WebSearchApiResponse:
        """Execute a web search query using the Brave Search API (https://api.search.brave.com/app/documentation/web-search/query#WebSearchAPIQueryParameters).

        Args:
            q: The user’s search query term. Query can not be empty. Maximum of 400 characters and 50 words in the query.
            country: The search query country, where the results come from. The country string is limited to 2 character country codes of supported countries. For a list of supported values, see Country Codes (https://api.search.brave.com/app/documentation/web-search/codes#country-codes).
            search_lang: The search language preference. The 2 or more character language code for which the search results are provided. For a list of possible values, see Language Codes (https://api.search.brave.com/app/documentation/web-search/codes#language-codes).
            ui_lang: User interface language preferred in response. Usually of the format ‘<language_code>-<country_code>’. For more, see RFC 9110 (https://www.rfc-editor.org/rfc/rfc9110.html#name-accept-language). For a list of supported values, see UI Language Codes (https://api.search.brave.com/app/documentation/web-search/codes#market-codes)
            count: The number of search results returned in response. The maximum is 20. The actual number delivered may be less than requested. Combine this parameter with offset to paginate search results.
            offset: In order to paginate results use this parameter together with count. For example, if your user interface displays 20 search results per page, set count to 20 and offset to 0 to show the first page of results. To get subsequent pages, increment offset by 1 (e.g. 0, 1, 2). The results may overlap across multiple pages.
            safesearch: Filters search results for adult content. The following values are supported: off: No filtering is done. moderate: Filters explicit content, like images and videos, but allows adult domains in the search results. strict: Drops all adult content from search results.
            freshness: Filters search results by when they were discovered. The following values are supported: - pd: Discovered within the last 24 hours. - pw: Discovered within the last 7 Days. - pm: Discovered within the last 31 Days. - py: Discovered within the last 365 Days… - YYYY-MM-DDtoYYYY-MM-DD: timeframe is also supported by specifying the date range e.g. 2022-04-01to2022-07-30.
            text_decorations: Whether display strings (e.g. result snippets) should include decoration markers (e.g. highlighting characters).
            spellcheck: Whether to spellcheck provided query. If the spellchecker is enabled, the modified query is always used for search. The modified query can be found in altered key from the query response model.
            result_filter: A comma delimited string of result types to include in the search response. Not specifying this parameter will return back all result types in search response where data is available and a plan with the corresponding option is subscribed. The response always includes query and type to identify any query modifications and response type respectively. Available result filter values are: - discussions - faq - infobox - news - query - summarizer - videos - web - locations. Example result filter param result_filter=discussions, videos returns only discussions, and videos responses. Another example where only location results are required, set the result_filter param to result_filter=locations.
            goggles_id: Goggles act as a custom re-ranking on top of Brave’s search index. For more details, refer to the Goggles repository (https://github.com/brave/goggles-quickstart)
            units: The measurement units. If not provided, units are derived from search country. Possible values are: - metric: The standardized measurement system - imperial: The British Imperial system of units.
            extra_snippets: A snippet is an excerpt from a page you get as a result of the query, and extra_snippets allow you to get up to 5 additional, alternative excerpts. Only available under Free AI, Base AI, Pro AI, Base Data, Pro Data and Custom plans.
            summary: This parameter enables summary key generation in web search results. This is required for summarizer to be enabled.
            dump_response = Whether to dump the original response. If enabled will be dumped into response.json in current working directory.
        Returns:
            WebSearchResponse: Top level response model for successful Web Search API requests. The response will include the relevant keys based on the plan subscribed, query relevance or applied result_filter as a query parameter. The API can also respond back with an error response based on invalid subscription keys and rate limit events (https://api.search.brave.com/app/documentation/web-search/responses#WebSearchApiResponse).

        Raises:
            ValueError: If query validation fails.
            BraveSearchError: If API request fails or returns an error.
        """

        request = WebSearchRequest(
            q=q,
            country=country,
            search_lang=search_lang,
            ui_lang=ui_lang,
            count=count,
            offset=offset,
            safesearch=safesearch,
            freshness=freshness,
            text_decorations=text_decorations,
            spellcheck=spellcheck,
            result_filter=result_filter,
            goggles_id=goggles_id,
            units=units,
            extra_snippets=extra_snippets,
            summary=summary,
        )

        # API request and response handling
        response = await self._get("web", params=request.model_dump(exclude_none=True))

        if dump_response:
            with open("response.json", "w") as f:
                f.write(response.text)

        return WebSearchApiResponse.model_validate(response.json())

    async def image_search(
        self,
        q: str,
        country: str = "US",
        search_lang: str = "en",
        count: int = 50,
        safesearch: ImageSafeSearchType = ImageSafeSearchType.strict,
        spellcheck: bool = True,
        dump_response: bool = False,
    ) -> ImageSearchApiResponse:
        """Execute an image search query using the Brave Search API.

        Args:
            q: The user’s search query term. Query can not be empty. Maximum of 400 characters and 50 words in the query.
            country: The search query country, where the results come from. The country string is limited to 2 character country codes of supported countries. For a list of supported values, see Country Codes (https://api.search.brave.com/app/documentation/web-search/codes#country-codes).
            search_lang: The search language preference. The 2 or more character language code for which the search results are provided. For a list of possible values, see Language Codes (https://api.search.brave.com/app/documentation/web-search/codes#language-codes).
            count: The number of search results returned in response. The maximum is 20. The actual number delivered may be less than requested. Combine this parameter with offset to paginate search results.
            safesearch: The following values are supported: off: No filtering is done. strict: Drops all adult content from search results.
            spellcheck: Whether to spellcheck provided query. If the spellchecker is enabled, the modified query is always used for search. The modified query can be found in altered key from the query response model.
            dump_response = Whether to dump the original response. If enabled will be dumped into response.json in current working directory.

        Returns:
            ImageSearchApiResponse: Top level response model for successful Image Search API requests. The API can also respond back with an error response based on invalid subscription keys and rate limit events (https://api.search.brave.com/app/documentation/image-search/responses).

        Raises:
            ValueError: If query validation fails.
            BraveSearchError: If API request fails or returns an error.
        """

        request = ImageSearchRequest(
            q=q,
            country=country,
            search_lang=search_lang,
            count=count,
            safesearch=safesearch,
            spellcheck=spellcheck,
        )

        response = await self._get(
            "images", params=request.model_dump(exclude_none=True)
        )

        if dump_response:
            with open("response.json", "w") as f:
                f.write(response.text)

        return ImageSearchApiResponse.model_validate(response.json())

    async def video_search(
        self,
        q: str,
        country: str = "US",
        search_lang: str = "en",
        ui_lang: str = "en-US",
        count: int = 20,
        offset: int = 0,
        spellcheck: bool = True,
        freshness: FreshnessType | None = None,
        dump_response: bool = False,
    ) -> VideoSearchApiResponse:
        """Execute a video search query using the Brave Search API.

        Args:
            q: The user’s search query term. Query can not be empty. Maximum of 400 characters and 50 words in the query.
            country: The search query country, where the results come from. The country string is limited to 2 character country codes of supported countries. For a list of supported values, see Country Codes (https://api.search.brave.com/app/documentation/web-search/codes#country-codes).
            search_lang: The search language preference. The 2 or more character language code for which the search results are provided. For a list of possible values, see Language Codes (https://api.search.brave.com/app/documentation/web-search/codes#language-codes).
            ui_lang: User interface language preferred in response. Usually of the format ‘<language_code>-<country_code>’. For more, see RFC 9110 (https://www.rfc-editor.org/rfc/rfc9110.html#name-accept-language). For a list of supported values, see UI Language Codes (https://api.search.brave.com/app/documentation/web-search/codes#market-codes)
            count: The number of search results returned in response. The maximum is 20. The actual number delivered may be less than requested. Combine this parameter with offset to paginate search results.
            offset: In order to paginate results use this parameter together with count. For example, if your user interface displays 20 search results per page, set count to 20 and offset to 0 to show the first page of results. To get subsequent pages, increment offset by 1 (e.g. 0, 1, 2). The results may overlap across multiple pages.
            spellcheck: Whether to spellcheck provided query. If the spellchecker is enabled, the modified query is always used for search. The modified query can be found in altered key from the query response model.
            freshness: Filters search results by when they were discovered. The following values are supported: - pd: Discovered within the last 24 hours. - pw: Discovered within the last 7 Days. - pm: Discovered within the last 31 Days. - py: Discovered within the last 365 Days… - YYYY-MM-DDtoYYYY-MM-DD: timeframe is also supported by specifying the date range e.g. 2022-04-01to2022-07-30.
            dump_response = Whether to dump the original response. If enabled will be dumped into response.json in current working directory.

        Returns:
            NewsSearchApiResponse: Top level response model for successful News Search API requests. The API can also respond back with an error response based on invalid subscription keys and rate limit events (https://api.search.brave.com/app/documentation/news-search/responses).

        Raises:
            ValueError: If query validation fails.
            BraveSearchError: If API request fails or returns an error.
        """

        request = VideoSearchRequest(
            q=q,
            country=country,
            search_lang=search_lang,
            ui_lang=ui_lang,
            count=count,
            offset=offset,
            spellcheck=spellcheck,
            freshness=freshness,
        )

        response = await self._get(
            "videos", params=request.model_dump(exclude_none=True)
        )

        if dump_response:
            with open("response.json", "w") as f:
                f.write(response.text)

        return VideoSearchApiResponse.model_validate(response.json())

    async def news_search(
        self,
        q: str,
        country: str = "US",
        search_lang: str = "en",
        ui_lang: str = "en-US",
        count: int = 20,
        offset: int = 0,
        spellcheck: bool = True,
        safesearch: NewsSafeSearchType = NewsSafeSearchType.moderate,
        freshness: FreshnessType | None = None,
        extra_snippets: bool = False,
        dump_response: bool = False,
    ) -> NewsSearchApiResponse:
        """Execute a news search query using the Brave Search API.

        Args:
            q: The user’s search query term. Query can not be empty. Maximum of 400 characters and 50 words in the query.
            country: The search query country, where the results come from. The country string is limited to 2 character country codes of supported countries. For a list of supported values, see Country Codes (https://api.search.brave.com/app/documentation/web-search/codes#country-codes).
            search_lang: The search language preference. The 2 or more character language code for which the search results are provided. For a list of possible values, see Language Codes (https://api.search.brave.com/app/documentation/web-search/codes#language-codes).
            ui_lang: User interface language preferred in response. Usually of the format ‘<language_code>-<country_code>’. For more, see RFC 9110 (https://www.rfc-editor.org/rfc/rfc9110.html#name-accept-language). For a list of supported values, see UI Language Codes (https://api.search.brave.com/app/documentation/web-search/codes#market-codes)
            count: The number of search results returned in response. The maximum is 20. The actual number delivered may be less than requested. Combine this parameter with offset to paginate search results.
            offset: In order to paginate results use this parameter together with count. For example, if your user interface displays 20 search results per page, set count to 20 and offset to 0 to show the first page of results. To get subsequent pages, increment offset by 1 (e.g. 0, 1, 2). The results may overlap across multiple pages.
            spellcheck: Whether to spellcheck provided query. If the spellchecker is enabled, the modified query is always used for search. The modified query can be found in altered key from the query response model.
            safesearch: Filters search results for adult content. The following values are supported: off: No filtering is done. moderate: Filters explicit content, like images and videos, but allows adult domains in the search results. strict: Drops all adult content from search results.
            freshness: Filters search results by when they were discovered. The following values are supported: - pd: Discovered within the last 24 hours. - pw: Discovered within the last 7 Days. - pm: Discovered within the last 31 Days. - py: Discovered within the last 365 Days… - YYYY-MM-DDtoYYYY-MM-DD: timeframe is also supported by specifying the date range e.g. 2022-04-01to2022-07-30.
            extra_snippets: A snippet is an excerpt from a page you get as a result of the query, and extra_snippets allow you to get up to 5 additional, alternative excerpts. Only available under Free AI, Base AI, Pro AI, Base Data, Pro Data and Custom plans.
            dump_response = Whether to dump the original response. If enabled will be dumped into response.json in current working directory.

        Returns:
            NewsSearchApiResponse: Top level response model for successful News Search API requests. The API can also respond back with an error response based on invalid subscription keys and rate limit events (https://api.search.brave.com/app/documentation/news-search/responses).

        Raises:
            ValueError: If query validation fails.
            BraveSearchError: If API request fails or returns an error.
        """

        request = NewsSearchRequest(
            q=q,
            country=country,
            search_lang=search_lang,
            ui_lang=ui_lang,
            count=count,
            offset=offset,
            spellcheck=spellcheck,
            safesearch=safesearch,
            freshness=freshness,
            extra_snippets=extra_snippets,
        )

        response = await self._get("news", params=request.model_dump(exclude_none=True))

        if dump_response:
            with open("response.json", "w") as f:
                f.write(response.text)

        return NewsSearchApiResponse.model_validate(response.json())
