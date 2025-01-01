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


@pytest.mark.parametrize(
    "request_class,params",
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
def test_requests_base_search_request_validation(request_class, params):
    """Test base request validation for all request types."""
    # Test empty query
    with pytest.raises(
        ValidationError, match="String should have at least 1 character"
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
        ValidationError, match=f"Query exceeding {MAX_QUERY_TERMS} terms"
    ):
        request_class(q="a " * (MAX_QUERY_TERMS + 1), **params)

    # Test invalid country code
    with pytest.raises(
        ValidationError, match="Input should be 'ALL', 'AR', 'AU', 'AT', "
    ):
        params["country"] = "USA"
        request_class(q="test", **params)


def test_requests_web_search_request_validation():
    """Test specific WebSearchRequest validation."""
    base_params = {
        "q": "test",
        "country": "US",
        "search_lang": "en",
        "ui_lang": "en-US",
        "text_decorations": True,
        "spellcheck": True,
        "extra_snippets": False,
        "summary": False,
    }

    # Test count validation
    with pytest.raises(
        ValidationError, match="Input should be less than or equal to 20"
    ):
        WebSearchRequest(**base_params, count=21)

    with pytest.raises(ValidationError, match="Input should be greater than 0"):
        WebSearchRequest(**base_params, count=0)

    # Test offset validation
    with pytest.raises(
        ValidationError, match="Input should be less than or equal to 9"
    ):
        WebSearchRequest(**base_params, offset=10)

    with pytest.raises(
        ValidationError, match="Input should be greater than or equal to 0"
    ):
        WebSearchRequest(**base_params, offset=-1)

    # Test safesearch validation
    with pytest.raises(
        ValidationError, match="Input should be 'off', 'moderate' or 'strict'"
    ):
        WebSearchRequest(**base_params, safesearch="invalid")  # type: ignore

    # Test units validation
    with pytest.raises(ValidationError, match="Input should be 'metric' or 'imperial'"):
        WebSearchRequest(**base_params, units="invalid")  # type: ignore

    # Test freshness validation
    with pytest.raises(
        ValidationError,
        match="Freshness must be None, one of FreshnessType values",
    ):
        WebSearchRequest(**base_params, freshness="invalid")  # type: ignore

    # Test valid freshness values
    for freshness in ["pd", "pw", "pm", "py"]:
        request = WebSearchRequest(**base_params, freshness=FreshnessType(freshness))
        assert request.freshness == FreshnessType(freshness)

    # Test valid units values
    for unit in ["metric", "imperial"]:
        request = WebSearchRequest(**base_params, units=UnitsType(unit))
        assert request.units == UnitsType(unit)


def test_requests_image_search_request_validation():
    """Test specific ImageSearchRequest validation."""
    base_params = {
        "q": "test",
        "country": "US",
        "search_lang": "en",
        "spellcheck": True,
    }

    # Test count validation
    with pytest.raises(
        ValidationError, match="Input should be less than or equal to 100"
    ):
        ImagesSearchRequest(**base_params, count=101)

    with pytest.raises(ValidationError, match="Input should be greater than 0"):
        ImagesSearchRequest(**base_params, count=0)

    # Test safesearch validation
    with pytest.raises(ValidationError, match="Input should be 'off' or 'strict'"):
        ImagesSearchRequest(**base_params, safesearch="moderate")  # type: ignore


def test_requests_video_search_request_validation():
    """Test specific VideoSearchRequest validation."""
    base_params = {
        "q": "test",
        "country": "US",
        "search_lang": "en",
        "ui_lang": "en-US",
        "spellcheck": True,
    }

    # Test count validation
    with pytest.raises(
        ValidationError, match="Input should be less than or equal to 50"
    ):
        VideosSearchRequest(**base_params, count=51)

    with pytest.raises(ValidationError, match="Input should be greater than 0"):
        VideosSearchRequest(**base_params, count=0)

    # Test offset validation
    with pytest.raises(
        ValidationError, match="Input should be less than or equal to 9"
    ):
        VideosSearchRequest(**base_params, offset=10)

    with pytest.raises(
        ValidationError, match="Input should be greater than or equal to 0"
    ):
        VideosSearchRequest(**base_params, offset=-1)

    # Test freshness validation
    with pytest.raises(
        ValidationError,
        match="Freshness must be None, one of FreshnessType values",
    ):
        VideosSearchRequest(**base_params, freshness="invalid")  # type: ignore

    # Test valid freshness values
    for freshness in ["pd", "pw", "pm", "py"]:
        request = VideosSearchRequest(**base_params, freshness=FreshnessType(freshness))
        assert request.freshness == FreshnessType(freshness)


def test_requests_news_search_request_validation():
    """Test specific NewsSearchRequest validation."""
    base_params = {
        "q": "test",
        "country": "US",
        "search_lang": "en",
        "ui_lang": "en-US",
        "spellcheck": True,
        "extra_snippets": False,
    }

    # Test count validation
    with pytest.raises(
        ValidationError, match="Input should be less than or equal to 50"
    ):
        NewsSearchRequest(**base_params, count=51)

    with pytest.raises(ValidationError, match="Input should be greater than 0"):
        NewsSearchRequest(**base_params, count=0)

    # Test offset validation
    with pytest.raises(
        ValidationError, match="Input should be less than or equal to 9"
    ):
        NewsSearchRequest(**base_params, offset=10)

    with pytest.raises(
        ValidationError, match="Input should be greater than or equal to 0"
    ):
        NewsSearchRequest(**base_params, offset=-1)

    # Test safesearch validation
    with pytest.raises(
        ValidationError, match="Input should be 'off', 'moderate' or 'strict'"
    ):
        NewsSearchRequest(**base_params, safesearch="invalid")  # type: ignore

    # Test freshness validation
    with pytest.raises(
        ValidationError,
        match="Freshness must be None, one of FreshnessType values",
    ):
        NewsSearchRequest(**base_params, freshness="invalid")  # type: ignore

    # Test valid freshness values
    for freshness in ["pd", "pw", "pm", "py"]:
        request = NewsSearchRequest(**base_params, freshness=FreshnessType(freshness))
        assert request.freshness == FreshnessType(freshness)


def test_requests_search_request_success_cases():
    """Test valid request cases."""
    # Web search
    web_request = WebSearchRequest(
        q="test",
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
    assert web_request.q == "test"
    assert web_request.count == 20
    assert web_request.offset == 0
    assert web_request.safesearch == WebSafeSearchType.moderate
    assert web_request.freshness == FreshnessType.pd
    assert web_request.units == UnitsType.metric

    # Image search
    img_request = ImagesSearchRequest(
        q="test",
        country=CountryCode.US,
        search_lang=LanguageCode.EN,
        count=100,
        safesearch=ImagesSafeSearchType.strict,
        spellcheck=True,
    )
    assert img_request.q == "test"
    assert img_request.count == 100
    assert img_request.safesearch == ImagesSafeSearchType.strict

    # Video search
    video_request = VideosSearchRequest(
        q="test",
        country=CountryCode.US,
        search_lang=LanguageCode.EN,
        ui_lang=MarketCode.EN_US,
        count=50,
        offset=0,
        spellcheck=True,
    )
    assert video_request.q == "test"
    assert video_request.count == 50
    assert video_request.offset == 0
    assert video_request.ui_lang == "en-US"

    # News search
    news_request = NewsSearchRequest(
        q="test",
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
    assert news_request.q == "test"
    assert news_request.count == 20
    assert news_request.offset == 9
    assert news_request.safesearch == NewsSafeSearchType.moderate
    assert news_request.freshness == FreshnessType.pd


def test_requests_validate_freshness():
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
        _validate_freshness("invalid")  # Invalid value


def test_requests_validate_result_filter():
    """Test result filter validation."""
    from brave_search_python_client.requests import _validate_result_filter

    # Test None value
    assert _validate_result_filter(None) is None

    # Test single valid filter
    assert _validate_result_filter("web") == "web"

    # Test multiple valid filters
    assert _validate_result_filter("web,news,videos") == "web,news,videos"
    assert (
        _validate_result_filter("discussions,faq,infobox") == "discussions,faq,infobox"
    )

    # Test invalid filters
    with pytest.raises(ValueError):
        _validate_result_filter("invalid")
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


def test_requests_web_search_request_with_result_filter():
    """Test WebSearchRequest with result filter."""
    base_params = {
        "q": "test",
        "country": CountryCode.US,
        "search_lang": LanguageCode.EN,
        "ui_lang": MarketCode.EN_US,
    }

    # Test valid result filters
    request = WebSearchRequest(**base_params, result_filter="web,news,videos")
    assert request.result_filter == "web,news,videos"

    request = WebSearchRequest(**base_params, result_filter="discussions,faq,infobox")
    assert request.result_filter == "discussions,faq,infobox"

    # Test invalid result filters
    with pytest.raises(ValidationError):
        WebSearchRequest(**base_params, result_filter="invalid")

    with pytest.raises(ValidationError):
        WebSearchRequest(**base_params, result_filter="web,invalid,news")
