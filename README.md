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

### Basic Web Search

```python
from brave_search import BraveSearch

# Initialize client with your API key
client = BraveSearch(api_key="YOUR-API-KEY")

# Perform a web search
results = client.web_search("brave browser")

# Access search results
for result in results.web:
    print(f"Title: {result.title}")
    print(f"URL: {result.url}")
    print(f"Description: {result.description}")
```

### Image Search

```python
# Search for images
image_results = client.image_search("cute cats")

for image in image_results.images:
    print(f"Image URL: {image.url}")
    print(f"Source: {image.source}")
```

### News Search

```python
# Search for news articles
news_results = client.news_search("technology")

for article in news_results.news:
    print(f"Title: {article.title}")
    print(f"Published: {article.published}")
```

### Video Search

```python
# Search for videos
video_results = client.video_search("python tutorials")

for video in video_results.videos:
    print(f"Title: {video.title}")
    print(f"URL: {video.url}")
```

### Using Search Parameters

```python
# Advanced search with parameters
results = client.web_search(
    "python programming",
    country="US",
    search_lang="en",
)
```

## Command Line Interface (CLI)

### Run with uvx

Create `.env` file with API key:

```shell
./setup--dot-env YOUR_BRAVE_SEARCH_API_KEY

Show available commands:

```shell
uvx brave-search-python-client --help
```

Execute web search:

```shell
uvx brave-search-python-client web "hello world"
```

Show options for web search

```shell
uvx brave-search-python-client web --help
```

Execute image search:

```shell
uvx brave-search-python-client image "hello world"
```

Show options for image search

```shell
uvx brave-search-python-client image --help
```

Execute videos search:

```shell
uvx brave-search-python-client video "hello world"
```

Show options for videos search

```shell
uvx brave-search-python-client video --help
```

Execute news search:

```shell
uvx brave-search-python-client video "hello world"
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

Execute web search:

```bash
docker run --env BRAVE_SEARCH_API_KEY=YOUR_BRAVE_SEARCH_API_KEY helmuthva/brave-search-python-client web "hello world"
```

Show options for web search

```bash
docker run helmuthva/brave-search-python-client web --help
```

Execute image search:

```bash
docker run --env BRAVE_SEARCH_API_KEY=YOUR_BRAVE_SEARCH_API_KEY helmuthva/brave-search-python-client image "hello world"
```

Show options for image search

```bash
docker run helmuthva/brave-search-python-client image --help
```

Execute videos search:

```bash
docker run --env BRAVE_SEARCH_API_KEY=YOUR_BRAVE_SEARCH_API_KEY helmuthva/brave-search-python-client video "hello world"
```

Show options for videos search

```bash
docker run helmuthva/brave-search-python-client video --help
```

Execute news search:

```bash
docker run --env BRAVE_SEARCH_API_KEY=YOUR_BRAVE_SEARCH_API_KEY helmuthva/brave-search-python-client video "hello world"
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
