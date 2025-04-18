Brave Search Python Client supporting Web, Image, News and Video search.

Use Cases:

1. Integrate into your Python code to help users find what they're looking for.
2. Add to your AI applications to give LLMs access to current web information.
3. Use the built-in CLI in shell scripts to get search results in JSON format.

## Overview

Adding Brave Search Python Client to your project as a dependency is easy.

```shell
uv add brave-search-python-client             # add dependency to your project
```

If you don't have uv installed follow
[these instructions](https://docs.astral.sh/uv/getting-started/installation/).
If you still prefer pip over the modern and fast package manager
[uv](https://github.com/astral-sh/uv), you can install the library like this:

```shell
pip install brave-search-python-client        # add dependency to your project
```

Obtain your Brave Search API key by
[signing up here](https://brave.com/search/api/) - the free tier includes 2,000
requests per month. For guidance on how to integrate the Brave Search Python
client into your code base check out the examples below and explore the
[reference documentation](https://brave-search-python-client.readthedocs.io/en/latest/lib_reference.html).
If you just want to try out the client without having to write code you can use
the integrated CLI:

```shell
export BRAVE_SEARCH_API_KEY=YOUR_API_KEY         # replace YOUR_API_KEY
uvx brave-search-python-client web "hello world" # search for hello world
```

All advanced search options of Brave Search are supported
[by the client](https://brave-search-python-client.readthedocs.io/en/latest/lib_reference.html#brave_search_python_client.WebSearchRequest)
and in the CLI:

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

## Operational Excellence

This project is designed with operational excellence in mind, using modern
Python tooling and practices. It includes:

1. Various examples demonstrating usage: a.
   [Simple Python script](https://github.com/helmut-hoffer-von-ankershoffen/brave-search-python-client/blob/main/examples/script.py)
   b.
   [Streamlit web application](https://brave-search-python-client.streamlit.app/)
   deployed on [Streamlit Community Cloud](https://streamlit.io/cloud) c.
   [Jupyter](https://github.com/helmut-hoffer-von-ankershoffen/brave-search-python-client/blob/main/examples/notebook.ipynb)
   and
   [Marimo](https://github.com/helmut-hoffer-von-ankershoffen/brave-search-python-client/blob/main/examples/notebook.py)
   notebook
2. [Complete reference documentation](https://brave-search-python-client.readthedocs.io/en/latest/lib_reference.html)
   on Read the Docs
3. [Transparent test coverage](https://app.codecov.io/gh/helmut-hoffer-von-ankershoffen/brave-search-python-client)
   including unit and E2E tests (reported on Codecov)
4. Matrix tested with
   [multiple python versions](https://github.com/helmut-hoffer-von-ankershoffen/brave-search-python-client/blob/main/noxfile.py)
   to ensure compatibility (powered by [Nox](https://nox.thea.codes/en/stable/))
5. Compliant with modern linting and formatting standards (powered by
   [Ruff](https://github.com/astral-sh/ruff))
6. Up-to-date dependencies (monitored by
   [Renovate](https://github.com/renovatebot/renovate) and
   [Dependabot](https://github.com/helmut-hoffer-von-ankershoffen/brave-search-python-client/security/dependabot))
7. [A-grade code quality](https://sonarcloud.io/summary/new_code?id=helmut-hoffer-von-ankershoffen_brave-search-python-client)
   in security, maintainability, and reliability with low technical debt and
   codesmell (verified by SonarQube)
8. Additional code security checks using
   [CodeQL](https://github.com/helmut-hoffer-von-ankershoffen/brave-search-python-client/security/code-scanning)
9. [Security Policy](SECURITY.md)
10. [License](LICENSE) compliant with the Open Source Initiative (OSI)
11. 1-liner for installation and execution of command line interface (CLI) via
    [uv(x)](https://github.com/astral-sh/uv) or
    [Docker](https://hub.docker.com/r/helmuthva/brave-search-python-client/tags)
12. Setup for developing inside a
    [devcontainer](https://code.visualstudio.com/docs/devcontainers/containers)
    included (supports VSCode and GitHub Codespaces)

## Usage Examples

### Streamlit App

![Watch it](https://raw.githubusercontent.com/helmut-hoffer-von-ankershoffen/brave-search-python-client/main/examples/streamlit.gif)

[Try it out!](https://brave-search-python-client.streamlit.app) -
[Show the code](https://github.com/helmut-hoffer-von-ankershoffen/brave-search-python-client/blob/main/examples/streamlit.py)

### Minimal Python Script:

```python
"""
Example script demonstrating the usage of the Brave Search Python Client.

For web, image, video and news search.
"""

import asyncio
import os

from dotenv import load_dotenv
from rich.console import Console

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
    msg = "BRAVE_SEARCH_API_KEY not found in environment"
    raise ValueError(msg)


async def search() -> None:
    """Run various searches using the Brave Search Python Client (see https://brave-search-python-client.readthedocs.io/en/latest/lib_reference.html)."""
    # Initialize the Brave Search Python client, using the API key from the environment
    bs = BraveSearch()

    # Perform a web search
    response = await bs.web(WebSearchRequest(q="jupyter"))

    # Print results as JSON

    # Iterate over web hits and render links in markdown
    for _result in response.web.results if response.web else []:
        pass

    # Advanced search with parameters
    response = await bs.web(
        WebSearchRequest(
            q="python programming",
            country=CountryCode.DE,
            search_lang=LanguageCode.DE,
        ),
    )
    for _result in response.web.results if response.web else []:
        pass

    # Search and render images
    response = await bs.images(ImagesSearchRequest(q="cute cats"))
    for _image in response.results or []:
        pass

    # Search and render videos
    response = await bs.videos(VideosSearchRequest(q="singularity is close"))
    for _video in response.results or []:
        pass

    # Search and render news
    response = await bs.news(NewsSearchRequest(q="AI"))
    for _item in response.results or []:
        pass


# Run the async search function
# Alternatively use await search() from an async function
asyncio.run(search())
```

[Show script code](https://github.com/helmut-hoffer-von-ankershoffen/brave-search-python-client/blob/main/examples/script.py) -

[Read the library reference documentation](https://brave-search-python-client.readthedocs.io/en/latest/lib_reference.html#brave_search_python_client.BraveSearch)
for an explanation of available classes and methods.

## Jupyter Notebook

![Jupyter Notebook](https://raw.githubusercontent.com/helmut-hoffer-von-ankershoffen/brave-search-python-client/main/examples/notebook.png)

[Show notebook code](https://github.com/helmut-hoffer-von-ankershoffen/brave-search-python-client/blob/main/examples/notebook.ipynb)

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

[Read the CLI reference documentation](https://brave-search-python-client.readthedocs.io/en/latest/cli_reference.html)
for an explanation of all commands and options.

### Run with Docker

Note: Replace YOUR_BRAVE_SEARCH_API_KEY with your API key in the following
examples.

Show available commands:

```shell
docker run helmuthva/brave-search-python-client --help
```

Search the web:

```shell
docker run --env BRAVE_SEARCH_API_KEY=YOUR_BRAVE_SEARCH_API_KEY helmuthva/brave-search-python-client web "hello world"
```

Show options for web search

```shell
docker run helmuthva/brave-search-python-client web --help
```

Search images:

```shell
docker run --env BRAVE_SEARCH_API_KEY=YOUR_BRAVE_SEARCH_API_KEY helmuthva/brave-search-python-client images "hello world"
```

Show options for image search

```shell
docker run helmuthva/brave-search-python-client images --help
```

Search videos:

```shell
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

Or use docker compose

File .env is passed through

```shell
docker compose up
docker compose run brave-search-python-client --help
```
