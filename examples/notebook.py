# /// script
# requires-python = ">=3.13"
# dependencies = [
#     "marimo",
#     "brave-search-python-client",
#     "python-dotenv==1.1.0",
# ]
# ///

from brave_search_python_client.utils import __version__
import marimo

__generated_with = "0.13.2"
app = marimo.App(app_title=f"🦁 Brave Search Python Client v{__version__}", width="full")


@app.cell
def _():
    from brave_search_python_client import BraveSearch, WebSearchRequest
    return BraveSearch, WebSearchRequest


@app.cell
def _():
    import os

    from dotenv import load_dotenv

    load_dotenv()
    api_key = os.getenv("BRAVE_SEARCH_PYTHON_CLIENT_API_KEY")
    if not api_key:
        msg = "BRAVE_SEARCH_PYTHON_CLIENT_API_KEY is not set in .env file"
        raise ValueError(msg)
    return


@app.cell
async def _(BraveSearch, WebSearchRequest):
    bs = BraveSearch()
    response = await bs.web(WebSearchRequest(q="jupyter"))

    response.model_dump()
    return


if __name__ == "__main__":
    app.run()
