# [PRE-ALPHA] 🦁 Brave Search Python Client

[![License](https://img.shields.io/github/license/helmut-hoffer-von-ankershoffen/brave-search-python-client?logo=opensourceinitiative&logoColor=3DA639&labelColor=414042&color=A41831)
](https://github.com/helmut-hoffer-von-ankershoffen/brave-search-python-client/blob/main/LICENSE)
[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/brave-search-python-client.svg?logo=python&color=204361&labelColor=1E2933)](https://github.com/helmut-hoffer-von-ankershoffen/brave-search-python-client/blob/main/noxfile.py)
[![CI](https://github.com/helmut-hoffer-von-ankershoffen/brave-search-python-client/actions/workflows/test-and-report.yml/badge.svg)](https://github.com/helmut-hoffer-von-ankershoffen/brave-search-python-client/actions/workflows/test-and-report.yml)
[![Quality Gate](https://sonarcloud.io/api/project_badges/measure?project=helmut-hoffer-von-ankershoffen_brave-search-python-client&metric=alert_status)](https://sonarcloud.io/summary/new_code?id=helmut-hoffer-von-ankershoffen_brave-search-python-client)
[![Security](https://sonarcloud.io/api/project_badges/measure?project=helmut-hoffer-von-ankershoffen_brave-search-python-client&metric=security_rating)](https://sonarcloud.io/summary/new_code?id=helmut-hoffer-von-ankershoffen_brave-search-python-client)
[![Maintainability](https://sonarcloud.io/api/project_badges/measure?project=helmut-hoffer-von-ankershoffen_brave-search-python-client&metric=sqale_rating)](https://sonarcloud.io/summary/new_code?id=helmut-hoffer-von-ankershoffen_brave-search-python-client)
[![Technical Debt](https://sonarcloud.io/api/project_badges/measure?project=helmut-hoffer-von-ankershoffen_brave-search-python-client&metric=sqale_index)](https://sonarcloud.io/summary/new_code?id=helmut-hoffer-von-ankershoffen_brave-search-python-client)
[![Coverage](https://codecov.io/gh/helmut-hoffer-von-ankershoffen/brave-search-python-client/graph/badge.svg?token=SX34YRP30E)](https://codecov.io/gh/helmut-hoffer-von-ankershoffen/brave-search-python-client)
[![Ruff](https://img.shields.io/badge/style-Ruff-blue?color=D6FF65)](https://github.com/helmut-hoffer-von-ankershoffen/brave-search-python-client/blob/main/noxfile.py)
[![GitHub - Version](https://img.shields.io/github/v/release/helmut-hoffer-von-ankershoffen/brave-search-python-client?label=GitHub&style=flat&labelColor=1C2C2E&color=blue&logo=GitHub&logoColor=white)](https://github.com/helmut-hoffer-von-ankershoffen/brave-search-python-clientidge/releases)
![GitHub - Commits](https://img.shields.io/github/commit-activity/m/helmut-hoffer-von-ankershoffen/brave-search-python-client/main?label=commits&style=flat&labelColor=1C2C2E&color=blue&logo=GitHub&logoColor=white)
[![PyPI - Version](https://img.shields.io/pypi/v/brave-search-python-client.svg?label=PyPI&logo=pypi&logoColor=%23FFD243&labelColor=%230073B7&color=FDFDFD)](https://pypi.python.org/pypi/brave-search-python-client)
[![PyPI - Status](https://img.shields.io/pypi/status/brave-search-python-client?logo=pypi&logoColor=%23FFD243&labelColor=%230073B7&color=FDFDFD)](https://pypi.python.org/pypi/brave-search-python-client)
[![Docker - Version](https://img.shields.io/docker/v/helmuthva/brave-search-python-client?sort=semver&label=Docker&logo=docker&logoColor=white&labelColor=1354D4&color=10151B)](https://hub.docker.com/r/helmuthva/brave-search-python-client/tags)
[![Docker - Size](https://img.shields.io/docker/image-size/helmuthva/brave-search-python-client?sort=semver&arch=arm64&label=image&logo=docker&logoColor=white&labelColor=1354D4&color=10151B)](https://hub.docker.com/r/helmuthva/brave-search-python-client/)
<!---
[![ghcr.io - Version](https://ghcr-badge.egpl.dev/helmut-hoffer-von-ankershoffen/brave-search-python-client/tags?color=%2344cc11&ignore=0.0%2C0%2Clatest&n=3&label=ghcr.io&trim=)](https://github.com/helmut-hoffer-von-ankershoffen/brave-search-python-client/pkgs/container/brave-search-python-client)
[![ghcr.io - Sze](https://ghcr-badge.egpl.dev/helmut-hoffer-von-ankershoffen/brave-search-python-client/size?color=%2344cc11&tag=latest&label=size&trim=)](https://github.com/helmut-hoffer-von-ankershoffen/brave-search-python-client/pkgs/container/brave-search-python-client)
-->
> ⚠️ **WARNING**: This project is currently in pre-alpha phase, i.e. partly functional. Feel free to already watch or star the repository to stay updated on its progress.


## Overview

Brave Search Python Client supporting Web, Image, News and Video search.

* Modern async Python client for Web, Image, Video and News search powered by [Brave Search](https://brave.com/search/api/)
* Thorough validation of both requests and responess (powered by Pydantic)
* 100% test coverage (unit and E2E tests)
* 100% compliance modern linting and formatting standards (powered by Ruff)
* 100% up-to-date dependencies through automated updates (reported on Codecov)
* A-grade code quality ratings in security, maintainability, and reliability (verified by SonarQube)
* 1-liner for installation and execution of command line interface (CLI) via uv(x) or Docker
* Setup for developing in devcontainer included (supports VSCode and GitHub Codespaces)
* MCP Server to connect Brave Search with Claude Desktop and other MCP clients

## Python Client

Example:

```python
import asyncio
import json
import os

from dotenv import load_dotenv

from brave_search_python_client import (
    BraveSearch,
    CountryCode,
    ImagesSearchRequest,
    LanguageCode,
    NewsSearchRequest,
    VideosSearchRequest,
    WebSearchRequest,
)

# Load .env file and check for Brave Search API Key
load_dotenv()
api_key = os.getenv("BRAVE_SEARCH_API_KEY")
if not api_key:
    raise Exception("BRAVE_SEARCH_API_KEY found in environment")


async def search():
    """Run various searches using the Brave Search Python Client"""

    # Initialize the BraveSearch client, using the API key from the environment
    bs = BraveSearch()

    # Perform a web search
    response = await bs.web(WebSearchRequest(q="jupyter"))

    # Print results as JSON
    print("# Web search")
    print("## JSON response")
    print(json.dumps(response.model_dump(), indent=2))

    # Iterate over web hits and render links in markdown
    print("## Iterate and render")
    for result in response.web.results if response.web else []:
        print(f"[{result.title}]({result.url})")

    # Advanced search with parameters
    response = await bs.web(
        WebSearchRequest(
            q="python programming",
            country=CountryCode.DE,
            search_lang=LanguageCode.DE,
        )
    )

    print("# Advanced search results")
    for result in response.web.results if response.web else []:
        print(f"[{result.title}]({result.url})")

    # Search and render images
    print("# Images")
    response = await bs.images(ImagesSearchRequest(q="cute cats"))
    for image in response.results if response.results else []:
        print(f"![{image.source}]({image.url})")

    # Search and render videos
    print("# Videos")
    response = await bs.videos(VideosSearchRequest(q="singularity is close"))
    for video in response.results if response.results else []:
        print(f"![{video.title}]({video.url})")

    # Search and render news
    print("# News")
    response = await bs.news(NewsSearchRequest(q="AI"))
    for item in response.results if response.results else []:
        print(f"![{item.title}]({item.url})")


# Execute the search function
# Alternatively use await(search()) in an async function
asyncio.run(search())
```

## Command Line Interface (CLI)

### Run with uvx

Create `.env` file with API key:

```shell
./setup--dot-env YOUR_BRAVE_SEARCH_API_KEY
```

Show available commands:

```shell
uvx brave-search-python-client --help
```

Search the web for "hello world":

```shell
uvx brave-search-python-client web "hello world"
```

Show options for web search

```shell
uvx brave-search-python-client web --help
```

Search images:

```shell
uvx brave-search-python-client images "hello world"
```

Show options for image search

```shell
uvx brave-search-python-client images --help
```

Search videos:

```shell
uvx brave-search-python-client videos "hello world"
```

Show options for videos search

```shell
uvx brave-search-python-client videos --help
```

Search news:

```shell
uvx brave-search-python-client news "hello world"
```

Show options for news search

```shell
uvx brave-search-python-client news --help
```

### Run with Docker

Show options for news search

```shell
docker run helmuthva/brave-search-python-client news --help
```

### Docker

Note: Replace YOUR_BRAVE_SEARCH_API_KEY with your API key in the following examples.

Show available commands:

```bash
docker run helmuthva/brave-search-python-client --help
```

Search the web:

```bash
docker run --env BRAVE_SEARCH_API_KEY=YOUR_BRAVE_SEARCH_API_KEY helmuthva/brave-search-python-client web "hello world"
```

Show options for web search

```bash
docker run helmuthva/brave-search-python-client web --help
```

Search images:

```bash
docker run --env BRAVE_SEARCH_API_KEY=YOUR_BRAVE_SEARCH_API_KEY helmuthva/brave-search-python-client images "hello world"
```

Show options for image search

```bash
docker run helmuthva/brave-search-python-client images --help
```

Search videos:

```bash
docker run --env BRAVE_SEARCH_API_KEY=YOUR_BRAVE_SEARCH_API_KEY helmuthva/brave-search-python-client videos "hello world"
```

Show options for video search

```bash
docker run helmuthva/brave-search-python-client videos --help
```

Search news:

```bash
docker run --env BRAVE_SEARCH_API_KEY=YOUR_BRAVE_SEARCH_API_KEY helmuthva/brave-search-python-client news "hello world"
```

Show options for news search

```bash
docker run helmuthva/brave-search-python-client news --help
```

## Extra: MCP Server

TK

## Contributing

Please read our [Contributing Guidelines](CONTRIBUTING.md) for how to setup your development environment, and guidance for making pull requests.

## Resources

* [API](https://brave.com/search/api/)
* [MCP Specification and SDKs](https://github.com/modelcontextprotocol)

## Star History

<a href="https://star-history.com/#helmut-hoffer-von-ankershoffen/brave-search-python-client&Date">
 <picture>
   <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/svg?repos=helmut-hoffer-von-ankershoffen/brave-search-python-client&type=Date&theme=dark" />
   <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/svg?repos=helmut-hoffer-von-ankershoffen/brave-search-python-client&type=Date" />
   <img alt="Star History Chart" src="https://api.star-history.com/svg?repos=helmut-hoffer-von-ankershoffen/brave-search-python-client&type=Date" />
 </picture>
</a>
