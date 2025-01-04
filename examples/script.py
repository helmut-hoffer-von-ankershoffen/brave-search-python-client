"""
Example script demonstrating the usage of the Brave Search Python Client.

For web, image, video and news search.
"""

import asyncio
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
    msg = "BRAVE_SEARCH_API_KEY not found in environment"
    raise ValueError(msg)


async def search() -> None:
    """Run various searches using the Brave Search Python Client (see https://brave-search-python-client.readthedocs.io/en/latest/reference_index.html)."""
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
