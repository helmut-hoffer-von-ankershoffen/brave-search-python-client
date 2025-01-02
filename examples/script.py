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
