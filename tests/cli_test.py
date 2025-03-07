"""Tests to verify the CLI functionality of Brave Search Python Client."""

import json
from unittest.mock import patch

import pytest
from typer.testing import CliRunner

from brave_search_python_client import (
    BraveSearch,
    ImageSearchApiResponse,
    NewsSearchApiResponse,
    VideoSearchApiResponse,
    WebSearchApiResponse,
    __version__,
)
from brave_search_python_client.cli import cli

TEST_QUERY = "hello world"
BUILT_WITH_LOVE = "built with love in Berlin"
SEARCH_QUERY_HELP = "The search query to perform"

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


@pytest.fixture
def runner() -> CliRunner:
    """Provide a CLI test runner fixture."""
    return CliRunner()


def test_cli_built_with_love(runner) -> None:
    """Check epilog shown."""
    result = runner.invoke(cli, ["--help"])
    assert result.exit_code == 0
    assert BUILT_WITH_LOVE in result.output
    assert __version__ in result.output


def test_cli_commands(runner: CliRunner) -> None:
    """Check commands exist and show help and epilog."""
    for command in ["web", "images", "videos", "news"]:
        result = runner.invoke(cli, [command, "--help"])
    assert result.exit_code == 0
    assert SEARCH_QUERY_HELP in result.output
    assert f"Search {command}" in result.output or f"Search the {command}" in result.output
    assert __version__ in result.output


def test_cli_search(runner: CliRunner) -> None:
    """Check search triggered."""
    with patch.object(BraveSearch, "web", return_value=mock_web_search_response):
        result = runner.invoke(cli, ["web", TEST_QUERY])
        assert result.exit_code == 0
        response = json.loads(result.output)
        assert response["type"] == "search"

    with patch.object(BraveSearch, "images", return_value=mock_image_search_response):
        result = runner.invoke(cli, ["images", TEST_QUERY])
        assert result.exit_code == 0
        response = json.loads(result.output)
        assert response["type"] == "images"

    with patch.object(BraveSearch, "videos", return_value=mock_video_search_response):
        result = runner.invoke(cli, ["videos", TEST_QUERY])
        assert result.exit_code == 0
        response = json.loads(result.output)
        assert response["type"] == "videos"

    with patch.object(BraveSearch, "news", return_value=mock_news_search_response):
        result = runner.invoke(cli, ["news", TEST_QUERY])
        assert result.exit_code == 0
        response = json.loads(result.output)
        assert response["type"] == "news"
