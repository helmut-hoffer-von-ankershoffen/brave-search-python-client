import marimo

__generated_with = "0.11.17"
app = marimo.App(width="medium")


@app.cell
def _():
    from brave_search_python_client import BraveSearch, WebSearchRequest
    return BraveSearch, WebSearchRequest


@app.cell
def _():
    import os

    from dotenv import load_dotenv

    load_dotenv()
    api_key = os.getenv("BRAVE_SEARCH_API_KEY")
    if not api_key:
        msg = "BRAVE_SEARCH_API_KEY is not set in .env file"
        raise ValueError(msg)
    return api_key, load_dotenv, msg, os


@app.cell
async def _(BraveSearch, WebSearchRequest):
    bs = BraveSearch()
    response = await bs.web(WebSearchRequest(q="jupyter"))

    response.model_dump()
    return bs, response


if __name__ == "__main__":
    app.run()
