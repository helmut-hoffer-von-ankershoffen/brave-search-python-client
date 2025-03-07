"""
Streamlit web application that demonstrates a simple interface for Brave Search Python Client.

This module creates a web interface using Streamlit to demonstrate the usage of the service provided by
Brave Search Python Client.
"""

import asyncio

import streamlit as st

from brave_search_python_client import (
    BraveSearch,
    WebSearchApiResponse,
    WebSearchRequest,
    __version__,
)

sidebar = st.sidebar
api_key = sidebar.text_input(
    "[Brave Search API key](https://brave.com/search/api/)",
    type="password",
)
sidebar.write(
    f" [Brave Search Python Client v{__version__}](https://brave-search-python-client.readthedocs.io/)",
)
sidebar.write("Built with love in Berlin 🐻")

st.title("🦁 Brave Search ")
q = st.text_input("Query")

if api_key and q:
    # Initialize the BraveSearch client
    bs = BraveSearch(api_key=api_key)

    @st.cache_data
    def search(q: str) -> WebSearchApiResponse:
        """
        Perform a synchronous web search using Brave Search API.

        This function wraps an asynchronous API call into a synchronous interface by
        using asyncio.run(). It executes a web search query through the Brave Search API.

        Returns:
            WebSearchApiResponse: The search results from the API.

        """
        return asyncio.run(bs.web(WebSearchRequest(q=q)))

    # Perform the search
    response = search(q)

    # Print the response as JSON
    cols = st.columns([0.1, 0.9])
    with cols[0]:
        st.write("JSON:")
    with cols[1]:
        st.json(response.model_dump(), expanded=False)

    # Print the search results of type web
    for result in response.web.results if response.web else []:
        st.write(f"[{result.title}]({result.url})")
elif q:
    st.write(
        "Please enter your [Brave Search API key](https://brave.com/search/api/) in the sidebar.",
    )
