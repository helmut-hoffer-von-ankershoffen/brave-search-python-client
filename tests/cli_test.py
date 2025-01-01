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


@pytest.fixture
def runner():
    return CliRunner()


def test_cli_built_with_love(runner):
    """Check epilog shown."""
    result = runner.invoke(cli, ["--help"])
    assert result.exit_code == 0
    assert "built with love in Berlin" in result.output
    assert __version__ in result.output


def test_cli_commands(runner: CliRunner):
    """Check commands exist and show help and epilog."""
    for command in ["web", "images", "videos", "news"]:
        result = runner.invoke(cli, [command, "--help"])
        assert result.exit_code == 0
        assert "The search query to perform" in result.output
        assert (
            f"Search {command}" in result.output
            or f"Search the {command}" in result.output
        )
        assert __version__ in result.output


def test_cli_search(runner: CliRunner):
    """Check search triggered"""
    with patch.object(BraveSearch, "web", return_value=mock_web_search_response):
        result = runner.invoke(cli, ["web", "hello world"])
        assert result.exit_code == 0
        response = json.loads(result.output)
        assert response["type"] == "search"

    with patch.object(BraveSearch, "images", return_value=mock_image_search_response):
        result = runner.invoke(cli, ["images", "hello world"])
        assert result.exit_code == 0
        response = json.loads(result.output)
        assert response["type"] == "images"

    with patch.object(BraveSearch, "videos", return_value=mock_video_search_response):
        result = runner.invoke(cli, ["videos", "hello world"])
        assert result.exit_code == 0
        response = json.loads(result.output)
        assert response["type"] == "videos"

    with patch.object(BraveSearch, "news", return_value=mock_news_search_response):
        result = runner.invoke(cli, ["news", "hello world"])
        assert result.exit_code == 0
        response = json.loads(result.output)
        assert response["type"] == "news"
