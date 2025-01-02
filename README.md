# 🦁 Brave Search Python Client

[![License](https://img.shields.io/github/license/helmut-hoffer-von-ankershoffen/brave-search-python-client?logo=opensourceinitiative&logoColor=3DA639&labelColor=414042&color=A41831)
](https://github.com/helmut-hoffer-von-ankershoffen/brave-search-python-client/blob/main/LICENSE)
[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/brave-search-python-client.svg?logo=python&color=204361&labelColor=1E2933)](https://github.com/helmut-hoffer-von-ankershoffen/brave-search-python-client/blob/main/noxfile.py)
[![CI](https://github.com/helmut-hoffer-von-ankershoffen/brave-search-python-client/actions/workflows/test-and-report.yml/badge.svg)](https://github.com/helmut-hoffer-von-ankershoffen/brave-search-python-client/actions/workflows/test-and-report.yml)
[![Read the Docs](https://img.shields.io/readthedocs/brave-search-python-client)](https://brave-search-python-client.readthedocs.io/)
[![Quality Gate](https://sonarcloud.io/api/project_badges/measure?project=helmut-hoffer-von-ankershoffen_brave-search-python-client&metric=alert_status)](https://sonarcloud.io/summary/new_code?id=helmut-hoffer-von-ankershoffen_brave-search-python-client)
[![Security](https://sonarcloud.io/api/project_badges/measure?project=helmut-hoffer-von-ankershoffen_brave-search-python-client&metric=security_rating)](https://sonarcloud.io/summary/new_code?id=helmut-hoffer-von-ankershoffen_brave-search-python-client)
[![Maintainability](https://sonarcloud.io/api/project_badges/measure?project=helmut-hoffer-von-ankershoffen_brave-search-python-client&metric=sqale_rating)](https://sonarcloud.io/summary/new_code?id=helmut-hoffer-von-ankershoffen_brave-search-python-client)
[![Technical Debt](https://sonarcloud.io/api/project_badges/measure?project=helmut-hoffer-von-ankershoffen_brave-search-python-client&metric=sqale_index)](https://sonarcloud.io/summary/new_code?id=helmut-hoffer-von-ankershoffen_brave-search-python-client)
[![Code Smells](https://sonarcloud.io/api/project_badges/measure?project=helmut-hoffer-von-ankershoffen_brave-search-python-client&metric=code_smells)](https://sonarcloud.io/summary/new_code?id=helmut-hoffer-von-ankershoffen_brave-search-python-client)
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

The Brave Search Python Client provides Web, Image, News, and Video search capabilities.

Use Cases:
1) Integrate into your Python code to help users find what they're looking for.
2) Add to your AI applications to give LLMs access to current web information.
3) Use the built-in CLI in shell scripts to get search results in JSON format.

## Overview

Installation is as simple as:

```shell
uv add brave-search-python-client               # add dependency to your project
```

If you don't have uv installed follow [these instructions](https://docs.astral.sh/uv/getting-started/installation/). If you still prefer pip over the modern and fast package manager [uv](https://github.com/astral-sh/uv), you can install the library like this:

```shell
pip install brave-search-python-client          # add dependency to your project
```

Obtain your Brave Search API key by [signing up here](https://brave.com/search/api/) - the free tier includes 2,000 requests per month. For guidance on how to integrate the Brave Search Python client into your code base check out the examples below and explore the [reference documentation](https://brave-search-python-client.readthedocs.io/en/latest/reference_index.html). If you just want to try out the client without having to write code you can use the integrated CLI:

```shell
export BRAVE_SEARCH_API_KEY=YOUR_API_KEY         # replace YOUR_API_KEY
uvx brave-search-python-client web "hello world" # search for hello world
```

All advanced search options of Brave Search are supported [by the client](https://brave-search-python-client.readthedocs.io/en/latest/reference_index.html#brave_search_python_client.WebSearchRequest) and in the CLI:

```shell
# Find all German content about AI added in the last 24 hours
uvx brave-search-python-client web --country=DE --search-lang=de --units=metric --freshness=pd ai
```

The CLI provides extensive help:

```shell
uvx brave-search-python-client --help            # all CLI commands
uvx brave-search-python-client web --help        # all options for web search
uvx brave-search-python-client images --help     # all options image search
uvx brave-search-python-client videos --help     # all options video search
uvx brave-search-python-client news --help       # all options news search
```

![CLI](https://raw.githubusercontent.com/helmut-hoffer-von-ankershoffen/brave-search-python-client/refs/heads/main/cli-german-ai.png)

## Highlights

* Modern async Python client for Web, Image, Video and News search powered by [Brave Search](https://brave.com/search/api/)
* Various Examples:
  - [Streamlit web application](https://brave-search-python-client.streamlit.app/) deployed on [Streamlit Community Cloud](https://streamlit.io/cloud)
  - [Jupyter notebook](https://github.com/helmut-hoffer-von-ankershoffen/brave-search-python-client/blob/main/examples/jupyter.ipynb)
  - [Simple Python script](https://github.com/helmut-hoffer-von-ankershoffen/brave-search-python-client/blob/main/examples/script.py)
* Thorough validation of both [requests](https://github.com/helmut-hoffer-von-ankershoffen/brave-search-python-client/blob/main/src/brave_search_python_client/requests.py) and [responses](https://github.com/helmut-hoffer-von-ankershoffen/brave-search-python-client/tree/main/src/brave_search_python_client/responses) (powered by Pydantic)
* [Complete reference documenation](https://brave-search-python-client.readthedocs.io/en/latest/reference_index.html#brave_search_python_client.BraveSearch) on Read the Docs
* [100% test coverage](https://app.codecov.io/gh/helmut-hoffer-von-ankershoffen/brave-search-python-client) including unit and E2E tests (reported on Codecov)
* Matrix tested with [Python 3.11, 3.12 and 3.13](https://github.com/helmut-hoffer-von-ankershoffen/brave-search-python-client/blob/main/noxfile.py) to ensure compatibility (powered by [Nox](https://nox.thea.codes/en/stable/))
* 100% compliant with modern linting and formatting standards (powered by [Ruff](https://github.com/astral-sh/ruff))
* 100% up-to-date dependencies (monitored by [Renovate](https://github.com/renovatebot/renovate))
* [A-grade code quality](https://sonarcloud.io/summary/new_code?id=helmut-hoffer-von-ankershoffen_brave-search-python-client) in security, maintainability, and reliability with 0 technical debt and 0 codesmell (verified by SonarQube)
* 1-liner for installation and execution of command line interface (CLI) via [uv(x)](https://github.com/astral-sh/uv) or [Docker](https://hub.docker.com/r/helmuthva/brave-search-python-client/tags)
* Setup for developing inside a [devcontainer](https://code.visualstudio.com/docs/devcontainers/containers) included (supports VSCode and GitHub Codespaces)
* Later: [MCP server](https://www.anthropic.com/news/model-context-protocol) to connect Brave Search with Claude Desktop and other MCP clients

## Usage Examples

### Streamlit App

![Watch it](https://github.com/helmut-hoffer-von-ankershoffen/brave-search-python-client/raw/7f2a3a2e306c81c3487c0b0eda067f0440ec3f36/examples/streamlit.gif)

[Try it out!](https://brave-search-python-client.streamlit.app) - [Show the code](https://github.com/helmut-hoffer-von-ankershoffen/brave-search-python-client/blob/main/examples/streamlit.py)


### Minimal Python Script:

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

# Load .env file and get Brave Search API key from environment
load_dotenv()
api_key = os.getenv("BRAVE_SEARCH_API_KEY")
if not api_key:
    raise Exception("BRAVE_SEARCH_API_KEY not found in environment")


async def search():
    """Run various searches using the Brave Search Python Client (see https://brave-search-python-client.readthedocs.io/en/latest/reference_index.html)"""

    # Initialize the Brave Search Python client, using the API key from the environment
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


# Run the async search function
# Alternatively use await search() from an async function
asyncio.run(search())
```

[Show script code](https://github.com/helmut-hoffer-von-ankershoffen/brave-search-python-client/blob/main/examples/script.py) - [Read the reference documentation](https://brave-search-python-client.readthedocs.io/en/latest/reference_index.html#brave_search_python_client.BraveSearch)

## Jupyter Notebook

![Jupyter Notebook](https://raw.githubusercontent.com/helmut-hoffer-von-ankershoffen/brave-search-python-client/7f2a3a2e306c81c3487c0b0eda067f0440ec3f36/examples/jupyter.png)

[Show notebook code](https://github.com/helmut-hoffer-von-ankershoffen/brave-search-python-client/blob/main/examples/jupyter.ipynb)


## Command Line Interface (CLI)

### Run with [uvx](https://docs.astral.sh/uv/guides/tools/)

Add Brave Search API key to the environment

```shell
export BRAVE_SEARCH_API_KEY=YOUR_API_KEY
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

Please read our [Contributing Guidelines](https://brave-search-python-client.readthedocs.io/en/latest/contributing.html) for how to setup your development environment, and guidance for making pull requests.

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
