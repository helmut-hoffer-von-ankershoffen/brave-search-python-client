import json
from pathlib import Path
from unittest.mock import AsyncMock, patch

import httpx
import pytest

from brave_search_python_client import (
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

RETRY_COUNT = 3

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
    response = await client._get(SearchType.web, params={"q": "hello"})
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
    response = await client._get(
        SearchType.web, params={"q": "hello"}, retries=RETRY_COUNT
    )
    assert call_count == RETRY_COUNT
    assert response.json() == {"data": "world"}


@pytest.mark.asyncio
async def test_client_get_fails_without_retries(monkeypatch):
    monkeypatch.setattr(
        httpx.AsyncClient,
        "get",
        AsyncMock(side_effect=httpx.HTTPError("Permanent failure")),
    )

    client = BraveSearch(api_key="TEST_API_KEY")

    with pytest.raises(BraveSearchAPIError):
        await client._get(SearchType.web, params={"q": "hello world"})


@pytest.mark.asyncio
async def test_client_get_fails_with_retries(monkeypatch):
    monkeypatch.setattr(
        httpx.AsyncClient,
        "get",
        AsyncMock(side_effect=httpx.HTTPError("Permanent failure")),
    )

    client = BraveSearch(api_key="TEST_API_KEY")

    with pytest.raises(BraveSearchAPIError):
        await client._get(
            SearchType.web, params={"q": "hello world"}, retries=RETRY_COUNT
        )


@pytest.mark.asyncio
async def test_client_routing():
    client = BraveSearch(api_key="TEST_API_KEY")

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

    for search_method, mock_data, request_type, response_type in test_cases:
        # Bind mock_data using default argument
        async def mock_get(*args, mock_response_data=mock_data, **kwargs):
            mock_response = httpx.Response(200, json=mock_response_data)
            mock_response._request = httpx.Request(method="GET", url=args[0])
            return mock_response

        with patch.object(BraveSearch, "_get", new=AsyncMock(side_effect=mock_get)):
            response = await search_method(request_type(q="hello world"))
            assert isinstance(response, response_type)


@pytest.mark.asyncio
async def test_client_dump_response():
    client = BraveSearch(api_key="TEST_API_KEY")

    test_cases = [
        (client.web, WebSearchRequest, mock_web_search_response_data),
        (client.images, ImagesSearchRequest, mock_image_search_response_data),
        (client.videos, VideosSearchRequest, mock_video_search_response_data),
        (client.news, NewsSearchRequest, mock_news_search_response_data),
    ]

    for search_method, request_type, mock_data in test_cases:
        # Bind mock_data using default argument
        async def mock_get(*args, mock_response_data=mock_data, **kwargs):
            mock_response = httpx.Response(200, json=mock_response_data)
            mock_response._request = httpx.Request(method="GET", url=args[0])
            return mock_response

        with patch.object(BraveSearch, "_get", new=AsyncMock(side_effect=mock_get)):
            _ = await search_method(request_type(q="hello world"), dump_response=True)
            assert Path("response.json").exists()
            with open("response.json") as f:
                assert json.load(f) == mock_data
            Path("response.json").unlink()
