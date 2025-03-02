"""Tests for the Brave Search API client implementation."""

import json
from pathlib import Path
from typing import Never
from unittest.mock import AsyncMock, patch

import httpx
import pytest

from brave_search_python_client import (
    MOCK_API_KEY,
    BraveSearch,
    BraveSearchAPIError,
    BraveSearchClientError,
    ImageSearchApiResponse,
    ImagesSearchRequest,
    NewsSearchApiResponse,
    NewsSearchRequest,
    SearchType,
    VideoSearchApiResponse,
    VideosSearchRequest,
    WebSearchApiResponse,
    WebSearchRequest,
)

TEST_QUERY = "hello world"
TEST_API_KEY = "TEST_API_KEY"
RESPONSE_FILE = "response.json"
RETRY_COUNT = 3

with open("tests/fixtures/web.json", encoding="utf-8") as f:
    mock_web_search_response_data = json.load(f)
mock_web_search_response = WebSearchApiResponse.model_validate(
    mock_web_search_response_data,
)

with open("tests/fixtures/images.json", encoding="utf-8") as f:
    mock_image_search_response_data = json.load(f)
mock_image_search_response = ImageSearchApiResponse.model_validate(
    mock_image_search_response_data,
)

with open("tests/fixtures/videos.json", encoding="utf-8") as f:
    mock_video_search_response_data = json.load(f)
mock_video_search_response = VideoSearchApiResponse.model_validate(
    mock_video_search_response_data,
)

with open("tests/fixtures/news.json", encoding="utf-8") as f:
    mock_news_search_response_data = json.load(f)
mock_news_search_response = NewsSearchApiResponse.model_validate(
    mock_news_search_response_data,
)


def test_client_init_with_explicit_api_key(monkeypatch) -> None:
    """Test client initialization with explicitly provided API key."""
    arg_api_key = "ARG_API_KEY"
    monkeypatch.setenv("BRAVE_SEARCH_API_KEY", "ENV_API_KEY")
    client = BraveSearch(api_key=arg_api_key)
    assert client._api_key == arg_api_key


def test_client_init_with_env_var_api_key(monkeypatch) -> None:
    """Test client initialization using API key from environment variable."""
    monkeypatch.setenv("BRAVE_SEARCH_API_KEY", "ENV_API_KEY")
    client = BraveSearch()
    assert client._api_key == "ENV_API_KEY"


def test_client_init_error_without_api_key(monkeypatch) -> None:
    """Test client initialization fails when no API key is provided."""
    monkeypatch.delenv("BRAVE_SEARCH_API_KEY", raising=False)
    with pytest.raises(BraveSearchClientError):
        BraveSearch()


@pytest.mark.asyncio
async def test_client_get_works(monkeypatch) -> None:
    """Test successful HTTP GET request to API."""

    def mock_get(*args, **kwargs):
        # Create a Mock Response
        mock_response = httpx.Response(200, json={"data": "world"})
        # Setting the request attribute
        mock_response._request = httpx.Request(method="GET", url=args[0])
        return mock_response

    monkeypatch.setattr(httpx.AsyncClient, "get", AsyncMock(side_effect=mock_get))

    client = BraveSearch(api_key=TEST_API_KEY)
    response = await client._get(SearchType.web, params={"q": TEST_QUERY})
    assert response.json() == {"data": "world"}


@pytest.mark.asyncio
async def test_client_get_retries(monkeypatch) -> None:
    """Test HTTP GET request retry behavior."""
    call_count = 0

    def mock_get(*args, **kwargs):
        nonlocal call_count
        call_count += 1
        if call_count < RETRY_COUNT:
            msg = "Temporary failure"
            raise httpx.HTTPError(msg)
        # Create a Mock Response
        mock_response = httpx.Response(200, json={"data": "world"})
        # Setting the request attribute
        mock_response._request = httpx.Request(method="GET", url=args[0])
        return mock_response

    monkeypatch.setattr(httpx.AsyncClient, "get", AsyncMock(side_effect=mock_get))

    client = BraveSearch(api_key=TEST_API_KEY)
    response = await client._get(
        SearchType.web,
        params={"q": "hello"},
        retries=RETRY_COUNT,
    )
    assert call_count == RETRY_COUNT
    assert response.json() == {"data": "world"}


@pytest.mark.asyncio
async def test_client_get_fails_without_retries(monkeypatch) -> None:
    """Test HTTP GET request failure handling without retries."""
    monkeypatch.setattr(
        httpx.AsyncClient,
        "get",
        AsyncMock(side_effect=httpx.HTTPError("Permanent failure")),
    )

    client = BraveSearch(api_key=TEST_API_KEY)

    with pytest.raises(BraveSearchAPIError):
        await client._get(SearchType.web, params={"q": TEST_QUERY})


@pytest.mark.asyncio
async def test_client_get_fails_with_retries(monkeypatch) -> None:
    """Test HTTP GET request failure handling with retries."""
    monkeypatch.setattr(
        httpx.AsyncClient,
        "get",
        AsyncMock(side_effect=httpx.HTTPError("Permanent failure")),
    )

    client = BraveSearch(api_key=TEST_API_KEY)

    with pytest.raises(BraveSearchAPIError):
        await client._get(
            SearchType.web,
            params={"q": "hello world"},
            retries=RETRY_COUNT,
        )


@pytest.mark.asyncio
async def test_client_routing() -> None:
    """Test API endpoint routing logic."""
    client = BraveSearch(api_key=TEST_API_KEY)

    test_cases = [
        (
            client.web,
            mock_web_search_response_data,
            WebSearchRequest,
            WebSearchApiResponse,
        ),
        (
            client.images,
            mock_image_search_response_data,
            ImagesSearchRequest,
            ImageSearchApiResponse,
        ),
        (
            client.videos,
            mock_video_search_response_data,
            VideosSearchRequest,
            VideoSearchApiResponse,
        ),
        (
            client.news,
            mock_news_search_response_data,
            NewsSearchRequest,
            NewsSearchApiResponse,
        ),
    ]

    for search_method, fixtures, request_type, response_type in test_cases:
        # Bind fixtures using default argument
        def mock_get(*args, mock_response_data=fixtures, **kwargs):
            mock_response = httpx.Response(200, json=mock_response_data)
            mock_response._request = httpx.Request(method="GET", url=args[0])
            return mock_response

        with patch.object(BraveSearch, "_get", new=AsyncMock(side_effect=mock_get)):
            response = await search_method(request_type(q=TEST_QUERY))
            assert isinstance(response, response_type)


@pytest.mark.asyncio
async def test_client_dump_response() -> None:
    """Test response dumping functionality."""
    client = BraveSearch(api_key=TEST_API_KEY)

    test_cases = [
        (client.web, WebSearchRequest, mock_web_search_response_data),
        (client.images, ImagesSearchRequest, mock_image_search_response_data),
        (client.videos, VideosSearchRequest, mock_video_search_response_data),
        (client.news, NewsSearchRequest, mock_news_search_response_data),
    ]

    for search_method, request_type, fixtures in test_cases:
        # Bind fixtures using default argument
        def mock_get(*args, mock_response_data=fixtures, **kwargs):
            mock_response = httpx.Response(200, json=mock_response_data)
            mock_response._request = httpx.Request(method="GET", url=args[0])
            return mock_response

        with patch.object(BraveSearch, "_get", new=AsyncMock(side_effect=mock_get)):
            _ = await search_method(request_type(q=TEST_QUERY), dump_response=True)
            assert Path(RESPONSE_FILE).exists()
            with open(RESPONSE_FILE, encoding="utf-8") as f:
                assert json.load(f) == fixtures
            Path(RESPONSE_FILE).unlink()


@pytest.mark.asyncio
async def test_client_fixtures_handling() -> None:
    """Test that mock data is returned when MOCK_API_KEY is used."""
    client = BraveSearch(api_key=MOCK_API_KEY)

    # Web search
    web_response = await client.web(WebSearchRequest(q=TEST_QUERY))
    assert web_response == mock_web_search_response
    assert web_response.type == "search"

    # Image search
    image_response = await client.images(ImagesSearchRequest(q=TEST_QUERY))
    assert image_response == mock_image_search_response
    assert image_response.type == SearchType.images

    # Video search
    video_response = await client.videos(VideosSearchRequest(q=TEST_QUERY))
    assert video_response == mock_video_search_response
    assert video_response.type == SearchType.videos

    # News search
    news_response = await client.news(NewsSearchRequest(q=TEST_QUERY))
    assert news_response == mock_news_search_response
    assert news_response.type == SearchType.news


@pytest.mark.asyncio
async def test_client_is_connected_success(monkeypatch) -> None:
    """Test successful connection check."""

    def mock_head(*args, **kwargs):
        mock_response = httpx.Response(301)
        mock_response._request = httpx.Request("HEAD", args[0])
        return mock_response

    monkeypatch.setattr(httpx.AsyncClient, "head", AsyncMock(side_effect=mock_head))
    client = BraveSearch(api_key=TEST_API_KEY)
    assert await client.is_connected()

    # Should also work with redirect response
    def mock_head_redirect(*args, **kwargs):
        mock_response = httpx.Response(303)
        mock_response._request = httpx.Request("HEAD", args[0])
        return mock_response

    monkeypatch.setattr(
        httpx.AsyncClient,
        "head",
        AsyncMock(side_effect=mock_head_redirect),
    )
    assert await client.is_connected()


@pytest.mark.asyncio
async def test_client_is_connected_fail_status(monkeypatch) -> None:
    """Test connection check with unexpected status code."""

    def mock_head(*args, **kwargs):
        mock_response = httpx.Response(404)
        mock_response._request = httpx.Request("HEAD", args[0])
        return mock_response

    monkeypatch.setattr(httpx.AsyncClient, "head", AsyncMock(side_effect=mock_head))
    client = BraveSearch(api_key=TEST_API_KEY)
    assert not await client.is_connected()


@pytest.mark.asyncio
async def test_client_is_connected_fail_exception(monkeypatch) -> None:
    """Test connection check with raised exception."""

    def mock_head(*args, **kwargs) -> Never:
        msg = "Connection failed"
        raise httpx.RequestError(msg)

    monkeypatch.setattr(httpx.AsyncClient, "head", AsyncMock(side_effect=mock_head))
    client = BraveSearch(api_key=TEST_API_KEY)
    assert not await client.is_connected()
