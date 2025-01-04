"""Tests for request validation in the Brave Search Python client."""

import pytest
from pydantic import ValidationError

from brave_search_python_client.constants import MAX_QUERY_LENGTH, MAX_QUERY_TERMS
from brave_search_python_client.requests import (
    CountryCode,
    FreshnessType,
    ImagesSafeSearchType,
    ImagesSearchRequest,
    LanguageCode,
    MarketCode,
    NewsSafeSearchType,
    NewsSearchRequest,
    UnitsType,
    VideosSearchRequest,
    WebSafeSearchType,
    WebSearchRequest,
)

# Constants for test values
TEST_QUERY = "test"
INVALID_VALUE = "invalid"
COUNTRY_US = "US"
LANG_EN = "en"
UI_LANG_EN_US = "en-US"
SPELLCHECK_TRUE = True
EXTRA_SNIPPETS_FALSE = False

# Constants for error messages
ERROR_GREATER_THAN_ZERO = "Input should be greater than 0"
ERROR_LESS_EQUAL_20 = "Input should be less than or equal to 20"
ERROR_LESS_EQUAL_9 = "Input should be less than or equal to 9"
ERROR_LESS_EQUAL_50 = "Input should be less than or equal to 50"
ERROR_LESS_EQUAL_100 = "Input should be less than or equal to 100"
ERROR_GTE_ZERO = "Input should be greater than or equal to 0"
ERROR_FRESHNESS = "Freshness must be None, one of FreshnessType values"
WEB_NEWS_VIDEOS_NO_SPACES = "web,news,videos"
DISCUSSIONS_FAW_INFOBOX_NO_SPACES = "discussions,faq,infobox"


@pytest.mark.parametrize(
    ("request_class", "params"),
    [
        (
            WebSearchRequest,
            {
                "country": "ALL",
                "search_lang": "en",
                "ui_lang": "en-US",
                "text_decorations": True,
                "spellcheck": True,
                "extra_snippets": False,
                "summary": False,
            },
        ),
        (
            ImagesSearchRequest,
            {
                "country": "ALL",
                "search_lang": "en",
                "spellcheck": True,
            },
        ),
        (
            VideosSearchRequest,
            {
                "country": "ALL",
                "search_lang": "en",
                "ui_lang": "en-US",
                "spellcheck": True,
            },
        ),
        (
            NewsSearchRequest,
            {
                "country": "ALL",
                "search_lang": "en",
                "ui_lang": "en-US",
                "safesearch": "moderate",
                "spellcheck": True,
                "extra_snippets": False,
            },
        ),
    ],
)
def test_requests_base_search_request_validation(request_class, params) -> None:
    """Test base request validation for all request types."""
    # Test empty query
    with pytest.raises(
        ValidationError,
        match="String should have at least 1 character",
    ):
        request_class(q="", **params)

    # Test query too long
    with pytest.raises(
        ValidationError,
        match=f"String should have at most {MAX_QUERY_LENGTH} characters",
    ):
        request_class(q="a" * (MAX_QUERY_LENGTH + 1), **params)

    # Test too many terms
    with pytest.raises(
        ValidationError,
        match=f"Query exceeding {MAX_QUERY_TERMS} terms",
    ):
        request_class(q="a " * (MAX_QUERY_TERMS + 1), **params)

    # Test invalid country code
    with pytest.raises(
        ValidationError,
        match="Input should be 'ALL', 'AR', 'AU', 'AT', ",
    ):
        params["country"] = "USA"
        request_class(q=TEST_QUERY, **params)


def test_requests_web_search_request_validation() -> None:
    """Test specific WebSearchRequest validation."""
    base_params = {
        "q": TEST_QUERY,
        "country": COUNTRY_US,
        "search_lang": LANG_EN,
        "ui_lang": UI_LANG_EN_US,
        "text_decorations": True,
        "spellcheck": SPELLCHECK_TRUE,
        "extra_snippets": EXTRA_SNIPPETS_FALSE,
        "summary": False,
    }

    # Test count validation
    with pytest.raises(ValidationError, match=ERROR_LESS_EQUAL_20):
        WebSearchRequest(**base_params, count=21)

    with pytest.raises(ValidationError, match=ERROR_GREATER_THAN_ZERO):
        WebSearchRequest(**base_params, count=0)

    # Test offset validation
    with pytest.raises(ValidationError, match=ERROR_LESS_EQUAL_9):
        WebSearchRequest(**base_params, offset=10)

    with pytest.raises(ValidationError, match=ERROR_GTE_ZERO):
        WebSearchRequest(**base_params, offset=-1)

    # Test safesearch validation
    with pytest.raises(
        ValidationError,
        match="Input should be 'off', 'moderate' or 'strict'",
    ):
        WebSearchRequest(**base_params, safesearch=INVALID_VALUE)  # type: ignore

    # Test units validation
    with pytest.raises(ValidationError, match="Input should be 'metric' or 'imperial'"):
        WebSearchRequest(**base_params, units=INVALID_VALUE)  # type: ignore

    # Test freshness validation
    with pytest.raises(
        ValidationError,
        match=ERROR_FRESHNESS,
    ):
        WebSearchRequest(**base_params, freshness=INVALID_VALUE)  # type: ignore

    # Test valid freshness values
    for freshness in ["pd", "pw", "pm", "py"]:
        request = WebSearchRequest(**base_params, freshness=FreshnessType(freshness))
        assert request.freshness == FreshnessType(freshness)

    # Test valid units values
    for unit in ["metric", "imperial"]:
        request = WebSearchRequest(**base_params, units=UnitsType(unit))
        assert request.units == UnitsType(unit)


def test_requests_image_search_request_validation() -> None:
    """Test specific ImageSearchRequest validation."""
    base_params = {
        "q": TEST_QUERY,
        "country": COUNTRY_US,
        "search_lang": LANG_EN,
        "spellcheck": SPELLCHECK_TRUE,
    }

    # Test count validation
    with pytest.raises(ValidationError, match=ERROR_LESS_EQUAL_100):
        ImagesSearchRequest(**base_params, count=101)

    with pytest.raises(ValidationError, match=ERROR_GREATER_THAN_ZERO):
        ImagesSearchRequest(**base_params, count=0)

    # Test safesearch validation
    with pytest.raises(ValidationError, match="Input should be 'off' or 'strict'"):
        ImagesSearchRequest(**base_params, safesearch=INVALID_VALUE)  # type: ignore


def test_requests_video_search_request_validation() -> None:
    """Test specific VideoSearchRequest validation."""
    base_params = {
        "q": TEST_QUERY,
        "country": COUNTRY_US,
        "search_lang": LANG_EN,
        "ui_lang": UI_LANG_EN_US,
        "spellcheck": SPELLCHECK_TRUE,
    }

    # Test count validation
    with pytest.raises(ValidationError, match=ERROR_LESS_EQUAL_50):
        VideosSearchRequest(**base_params, count=51)

    with pytest.raises(ValidationError, match=ERROR_GREATER_THAN_ZERO):
        VideosSearchRequest(**base_params, count=0)

    # Test offset validation
    with pytest.raises(ValidationError, match=ERROR_LESS_EQUAL_9):
        VideosSearchRequest(**base_params, offset=10)

    with pytest.raises(ValidationError, match=ERROR_GTE_ZERO):
        VideosSearchRequest(**base_params, offset=-1)

    # Test freshness validation
    with pytest.raises(
        ValidationError,
        match=ERROR_FRESHNESS,
    ):
        VideosSearchRequest(**base_params, freshness=INVALID_VALUE)  # type: ignore

    # Test valid freshness values
    for freshness in ["pd", "pw", "pm", "py"]:
        request = VideosSearchRequest(**base_params, freshness=FreshnessType(freshness))
        assert request.freshness == FreshnessType(freshness)


def test_requests_news_search_request_validation() -> None:
    """Test specific NewsSearchRequest validation."""
    base_params = {
        "q": TEST_QUERY,
        "country": COUNTRY_US,
        "search_lang": LANG_EN,
        "ui_lang": UI_LANG_EN_US,
        "spellcheck": SPELLCHECK_TRUE,
        "extra_snippets": EXTRA_SNIPPETS_FALSE,
    }

    # Test count validation
    with pytest.raises(ValidationError, match=ERROR_LESS_EQUAL_50):
        NewsSearchRequest(**base_params, count=51)

    with pytest.raises(ValidationError, match=ERROR_GREATER_THAN_ZERO):
        NewsSearchRequest(**base_params, count=0)

    # Test offset validation
    with pytest.raises(ValidationError, match=ERROR_LESS_EQUAL_9):
        NewsSearchRequest(**base_params, offset=10)

    with pytest.raises(ValidationError, match=ERROR_GTE_ZERO):
        NewsSearchRequest(**base_params, offset=-1)

    # Test safesearch validation
    with pytest.raises(
        ValidationError,
        match="Input should be 'off', 'moderate' or 'strict'",
    ):
        NewsSearchRequest(**base_params, safesearch=INVALID_VALUE)  # type: ignore

    # Test freshness validation
    with pytest.raises(
        ValidationError,
        match=ERROR_FRESHNESS,
    ):
        NewsSearchRequest(**base_params, freshness=INVALID_VALUE)  # type: ignore

    # Test valid freshness values
    for freshness in ["pd", "pw", "pm", "py"]:
        request = NewsSearchRequest(**base_params, freshness=FreshnessType(freshness))
        assert request.freshness == FreshnessType(freshness)


def test_requests_search_request_success_cases() -> None:
    """Test valid request cases."""
    # Web search
    web_request = WebSearchRequest(
        q=TEST_QUERY,
        country=CountryCode.ALL,
        search_lang=LanguageCode.EN,
        ui_lang=MarketCode.EN_US,
        count=20,
        offset=0,
        safesearch=WebSafeSearchType.moderate,
        freshness=FreshnessType.pd,
        units=UnitsType.metric,
        text_decorations=True,
        spellcheck=True,
        extra_snippets=False,
        summary=False,
    )
    assert web_request.q == TEST_QUERY
    assert web_request.count == 20
    assert web_request.offset == 0
    assert web_request.safesearch == WebSafeSearchType.moderate
    assert web_request.freshness == FreshnessType.pd
    assert web_request.units == UnitsType.metric

    # Image search
    img_request = ImagesSearchRequest(
        q=TEST_QUERY,
        country=CountryCode.US,
        search_lang=LanguageCode.EN,
        count=100,
        safesearch=ImagesSafeSearchType.strict,
        spellcheck=True,
    )
    assert img_request.q == TEST_QUERY
    assert img_request.count == 100
    assert img_request.safesearch == ImagesSafeSearchType.strict

    # Video search
    video_request = VideosSearchRequest(
        q=TEST_QUERY,
        country=CountryCode.US,
        search_lang=LanguageCode.EN,
        ui_lang=MarketCode.EN_US,
        count=50,
        offset=0,
        spellcheck=True,
    )
    assert video_request.q == TEST_QUERY
    assert video_request.count == 50
    assert video_request.offset == 0
    assert video_request.ui_lang == "en-US"

    # News search
    news_request = NewsSearchRequest(
        q=TEST_QUERY,
        country=CountryCode.US,
        search_lang=LanguageCode.EN,
        ui_lang=MarketCode.EN_US,
        count=20,
        offset=9,
        safesearch=NewsSafeSearchType.moderate,
        freshness=FreshnessType.pd,
        spellcheck=True,
        extra_snippets=False,
    )
    assert news_request.q == TEST_QUERY
    assert news_request.count == 20
    assert news_request.offset == 9
    assert news_request.safesearch == NewsSafeSearchType.moderate
    assert news_request.freshness == FreshnessType.pd


def test_requests_validate_freshness() -> None:
    """Test freshness validation including date ranges."""
    from brave_search_python_client.requests import _validate_freshness

    # Test None value
    assert _validate_freshness(None) is None

    # Test valid FreshnessType values
    assert _validate_freshness("pd") == "pd"
    assert _validate_freshness("pw") == "pw"
    assert _validate_freshness("pm") == "pm"
    assert _validate_freshness("py") == "py"

    # Test valid date ranges
    assert _validate_freshness("2023-01-01to2023-12-31") == "2023-01-01to2023-12-31"
    assert _validate_freshness("2022-12-31to2023-01-01") == "2022-12-31to2023-01-01"

    # Test invalid date ranges
    with pytest.raises(ValueError):
        _validate_freshness("2023-01-01")  # Missing 'to' part
    with pytest.raises(ValueError):
        _validate_freshness("2023-01-01to")  # Incomplete range
    with pytest.raises(ValueError):
        _validate_freshness("2023-13-01to2023-12-31")  # Invalid month
    with pytest.raises(ValueError):
        _validate_freshness("2023-01-32to2023-12-31")  # Invalid day
    with pytest.raises(ValueError):
        _validate_freshness("2023/01/01to2023/12/31")  # Wrong format
    with pytest.raises(ValueError):
        _validate_freshness(INVALID_VALUE)  # Invalid value


def test_requests_validate_result_filter() -> None:
    """Test result filter validation."""
    from brave_search_python_client.requests import _validate_result_filter

    # Test None value
    assert _validate_result_filter(None) is None

    # Test single valid filter
    assert _validate_result_filter("web") == "web"

    # Test multiple valid filters
    assert _validate_result_filter(WEB_NEWS_VIDEOS_NO_SPACES) == WEB_NEWS_VIDEOS_NO_SPACES
    assert _validate_result_filter(DISCUSSIONS_FAW_INFOBOX_NO_SPACES) == DISCUSSIONS_FAW_INFOBOX_NO_SPACES

    # Test invalid filters
    with pytest.raises(ValueError):
        _validate_result_filter(INVALID_VALUE)
    with pytest.raises(ValueError):
        _validate_result_filter("web,invalid")
    with pytest.raises(ValueError):
        _validate_result_filter("web,news,invalid,videos")

    # Test empty string
    with pytest.raises(ValueError):
        _validate_result_filter("")

    # Test whitespace handling
    assert _validate_result_filter("web, news, videos") == "web, news, videos"
    assert _validate_result_filter(" web,news,videos ") == " web,news,videos "


def test_requests_web_search_request_with_result_filter() -> None:
    """Test WebSearchRequest with result filter."""
    base_params = {
        "q": TEST_QUERY,
        "country": CountryCode.US,
        "search_lang": LanguageCode.EN,
        "ui_lang": MarketCode.EN_US,
    }

    # Test valid result filters
    request = WebSearchRequest(**base_params, result_filter=WEB_NEWS_VIDEOS_NO_SPACES)
    assert request.result_filter == WEB_NEWS_VIDEOS_NO_SPACES

    request = WebSearchRequest(
        **base_params,
        result_filter=DISCUSSIONS_FAW_INFOBOX_NO_SPACES,
    )
    assert request.result_filter == DISCUSSIONS_FAW_INFOBOX_NO_SPACES

    # Test invalid result filters
    with pytest.raises(ValidationError):
        WebSearchRequest(**base_params, result_filter=INVALID_VALUE)

    with pytest.raises(ValidationError):
        WebSearchRequest(**base_params, result_filter="web,invalid,news")
