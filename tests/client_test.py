import json
from pathlib import Path
from unittest.mock import AsyncMock, patch

import httpx
import pytest
from pydantic import ValidationError

from brave_search_python_client import (
    BraveSearch,
    BraveSearchAPIError,
    BraveSearchClientError,
    ImageSearchApiResponse,
    NewsSearchApiResponse,
    VideoSearchApiResponse,
    WebSearchApiResponse,
)
from brave_search_python_client.constants import (
    MAX_QUERY_LENGTH,
    MAX_QUERY_TERMS,
    RETRY_COUNT,
)

with open("tests/fixtures/web_search_response.json") as f:
    mock_web_search_response_data = json.load(f)
mock_web_search_response = WebSearchApiResponse.model_validate(
    mock_web_search_response_data
)

with open("tests/fixtures/image_search_response.json") as f:
    mock_image_search_response_data = json.load(f)
mock_image_search_response = ImageSearchApiResponse.model_validate(
    mock_image_search_response_data
)

with open("tests/fixtures/video_search_response.json") as f:
    mock_video_search_response_data = json.load(f)
mock_video_search_response = VideoSearchApiResponse.model_validate(
    mock_video_search_response_data
)

with open("tests/fixtures/news_search_response.json") as f:
    mock_news_search_response_data = json.load(f)
mock_news_search_response = NewsSearchApiResponse.model_validate(
    mock_news_search_response_data
)


def test_client_init_with_explicit_api_key(monkeypatch):
    arg_api_key = "ARG_API_KEY"
    monkeypatch.setenv("BRAVE_SEARCH_API_KEY", "ENV_API_KEY")
    client = BraveSearch(api_key=arg_api_key)
    assert client._api_key == arg_api_key


def test_client_init_with_env_var_api_key(monkeypatch):
    monkeypatch.setenv("BRAVE_SEARCH_API_KEY", "ENV_API_KEY")
    client = BraveSearch()
    assert client._api_key == "ENV_API_KEY"


def test_client_init_error_without_api_key(monkeypatch):
    monkeypatch.delenv("BRAVE_SEARCH_API_KEY", raising=False)
    with pytest.raises(BraveSearchClientError):
        BraveSearch()


@pytest.mark.asyncio
async def test_client_get_works(monkeypatch):
    async def mock_get(*args, **kwargs):
        # Create a Mock Response
        mock_response = httpx.Response(200, json={"data": "world"})
        # Setting the request attribute
        mock_response._request = httpx.Request(method="GET", url=args[0])
        return mock_response

    monkeypatch.setattr(httpx.AsyncClient, "get", AsyncMock(side_effect=mock_get))

    client = BraveSearch(api_key="TEST_API_KEY")
    response = await client._get("web", params={"q": "hello"})
    assert response.json() == {"data": "world"}


@pytest.mark.asyncio
async def test_client_get_retries(monkeypatch):
    call_count = 0

    async def mock_get(*args, **kwargs):
        nonlocal call_count
        call_count += 1
        if call_count < RETRY_COUNT:
            raise httpx.HTTPError("Temporary failure")
        # Create a Mock Response
        mock_response = httpx.Response(200, json={"data": "world"})
        # Setting the request attribute
        mock_response._request = httpx.Request(method="GET", url=args[0])
        return mock_response

    monkeypatch.setattr(httpx.AsyncClient, "get", AsyncMock(side_effect=mock_get))

    client = BraveSearch(api_key="TEST_API_KEY")
    response = await client._get("web", params={"q": "hello"})
    assert call_count == RETRY_COUNT
    assert response.json() == {"data": "world"}


@pytest.mark.asyncio
async def test_client_get_fails(monkeypatch):
    monkeypatch.setattr(
        httpx.AsyncClient,
        "get",
        AsyncMock(side_effect=httpx.HTTPError("Permanent failure")),
    )

    client = BraveSearch(api_key="TEST_API_KEY")

    with pytest.raises(BraveSearchAPIError):
        await client._get("web", params={"q": "hello world"})


@pytest.mark.asyncio
async def test_client_search_routing():
    client = BraveSearch(api_key="TEST_API_KEY")

    test_cases = [
        (client.web_search, mock_web_search_response_data, WebSearchApiResponse),
        (client.image_search, mock_image_search_response_data, ImageSearchApiResponse),
        (client.video_search, mock_video_search_response_data, VideoSearchApiResponse),
        (client.news_search, mock_news_search_response_data, NewsSearchApiResponse),
    ]

    for search_method, mock_data, response_type in test_cases:
        # Bind mock_data using default argument
        async def mock_get(*args, mock_response_data=mock_data, **kwargs):
            mock_response = httpx.Response(200, json=mock_response_data)
            mock_response._request = httpx.Request(method="GET", url=args[0])
            return mock_response

        with patch.object(BraveSearch, "_get", new=AsyncMock(side_effect=mock_get)):
            response = await search_method("hello world")
            assert isinstance(response, response_type)


@pytest.mark.asyncio
async def test_client_search_dump_response():
    client = BraveSearch(api_key="TEST_API_KEY")

    test_cases = [
        (client.web_search, mock_web_search_response_data),
        (client.image_search, mock_image_search_response_data),
        (client.video_search, mock_video_search_response_data),
        (client.news_search, mock_news_search_response_data),
    ]

    for search_method, mock_data in test_cases:
        # Bind mock_data using default argument
        async def mock_get(*args, mock_response_data=mock_data, **kwargs):
            mock_response = httpx.Response(200, json=mock_response_data)
            mock_response._request = httpx.Request(method="GET", url=args[0])
            return mock_response

        with patch.object(BraveSearch, "_get", new=AsyncMock(side_effect=mock_get)):
            _ = await search_method("hello world", dump_response=True)
            assert Path("response.json").exists()
            with open("response.json") as f:
                assert json.load(f) == mock_data
            Path("response.json").unlink()


@pytest.mark.asyncio
async def test_client_response_validation(monkeypatch):
    async def mock_get(*args, **kwargs):
        mock_response = httpx.Response(200, json=mock_web_search_response_data)
        mock_response._request = httpx.Request(method="GET", url=args[0])
        return mock_response

    monkeypatch.setattr(httpx.AsyncClient, "get", AsyncMock(side_effect=mock_get))

    client = BraveSearch(api_key="TEST_API_KEY")
    response = await client.web_search("hello world")
    assert isinstance(response, WebSearchApiResponse)


@pytest.mark.asyncio
async def test_client_validation_errors():
    """Check validation errors are raised from request models."""
    client = BraveSearch(api_key="TEST_API_KEY")

    with pytest.raises(ValidationError, match="Query must not be empty"):
        await client.web_search("")

    with pytest.raises(
        ValidationError, match=f"Query exceeding {MAX_QUERY_LENGTH} characters"
    ):
        await client.web_search("a" * (MAX_QUERY_LENGTH + 1))

    with pytest.raises(
        ValidationError, match=f"Query exceeding {MAX_QUERY_TERMS} terms"
    ):
        await client.web_search("a " * (MAX_QUERY_TERMS + 1))

    with pytest.raises(
        ValidationError, match="Input should be less than or equal to 20"
    ):
        await client.web_search("test", count=21)

    with pytest.raises(
        ValidationError, match="Input should be less than or equal to 9"
    ):
        await client.web_search("test", offset=10)
