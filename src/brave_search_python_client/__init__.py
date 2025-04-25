"""Brave Search Python Client supporting Web, Image, News and Video search."""

from .client import BraveSearch
from .constants import (
    BASE_URL,
    DEFAULT_RETRY_WAIT_TIME,
    MAX_QUERY_LENGTH,
    MAX_QUERY_TERMS,
    MOCK_API_KEY,
)
from .requests import (
    CountryCode,
    FreshnessType,
    ImagesSafeSearchType,
    ImagesSearchRequest,
    LanguageCode,
    MarketCode,
    NewsSafeSearchType,
    NewsSearchRequest,
    SearchType,
    UnitsType,
    VideosSearchRequest,
    WebSafeSearchType,
    WebSearchRequest,
)
from .responses import (
    BraveSearchAPIError,
    BraveSearchClientError,
    BraveSearchError,
    ImageSearchApiResponse,
    NewsSearchApiResponse,
    VideoSearchApiResponse,
    WebSearchApiResponse,
)
from .utils.boot import boot

__all__ = [
    "BASE_URL",
    "DEFAULT_RETRY_WAIT_TIME",
    "MAX_QUERY_LENGTH",
    "MAX_QUERY_TERMS",
    "MOCK_API_KEY",
    "BraveSearch",
    "BraveSearchAPIError",
    "BraveSearchClientError",
    "BraveSearchError",
    "CountryCode",
    "FreshnessType",
    "ImageSearchApiResponse",
    "ImagesSafeSearchType",
    "ImagesSearchRequest",
    "LanguageCode",
    "MarketCode",
    "NewsSafeSearchType",
    "NewsSearchApiResponse",
    "NewsSearchRequest",
    "SearchType",
    "UnitsType",
    "VideoSearchApiResponse",
    "VideosSearchRequest",
    "WebSafeSearchType",
    "WebSearchApiResponse",
    "WebSearchRequest",
]

boot()
