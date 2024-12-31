import asyncio
from typing import Annotated

import typer
from dotenv import load_dotenv
from rich.console import Console

from brave_search_python_client import BraveSearch, __version__

from .requests import (
    FreshnessType,
    ImageSafeSearchType,
    NewsSafeSearchType,
    UnitsType,
    WebSafeSearchType,
)

load_dotenv()

console = Console()

cli = typer.Typer(name="Brave Search CLI")


@cli.command()
def web(
    q: Annotated[str, typer.Argument(..., help="The search query to perform")],
    country: Annotated[
        str,
        typer.Option(help="The country to search from (2-letter country code)"),
    ] = "US",
    search_lang: Annotated[
        str,
        typer.Option(help="The language to search in (2 letter language code)"),
    ] = "en",
    ui_lang: Annotated[str, typer.Option(help="The language to display")] = "en-US",
    count: Annotated[
        int, typer.Option(help="The number of results to return (max 20)")
    ] = 20,
    offset: Annotated[int, typer.Option(help="The offset to start from (max 9)")] = 0,
    safesearch: Annotated[
        WebSafeSearchType,
        typer.Option(help="Enable safe search (off, moderate, strict)"),
    ] = WebSafeSearchType.moderate,
    freshness: Annotated[
        FreshnessType | None,
        typer.Option(
            help="pd: Discovered within the last 24 hours. - pw: Discovered within the last 7 Days. - pm: Discovered within the last 31 Days. - py: Discovered within the last 365 Days… - YYYY-MM-DDtoYYYY-MM-DD: timeframe is also supported by specifying the date range e.g. 2022-04-01to2022-07-30",
        ),
    ] = None,
    text_decorations: Annotated[
        bool,
        typer.Option(
            help="Whether display strings (e.g. result snippets) should include decoration markers (e.g. highlighting characters).",
        ),
    ] = True,
    spellcheck: Annotated[bool, typer.Option(help="Enable spellcheck")] = True,
    result_filter: Annotated[
        str | None,
        typer.Option(
            help=" comma delimited string of result types to include in the search response. Not specifying this parameter will return back all result types in search response where data is available and a plan with the corresponding option is subscribed. The response always includes query and type to identify any query modifications and response type respectively. Available result filter values are: - discussions - faq - infobox - news - query - summarizer - videos - web - locations. Example result filter param result_filter=discussions, videos returns only discussions, and videos responses. Another example where only location results are required, set the result_filter param to result_filter=locations",
        ),
    ] = None,
    googles_id: Annotated[
        str | None,
        typer.Option(
            help="Goggles act as a custom re-ranking on top of Brave’s search index. For more details, refer to the Goggles repository (https://github.com/brave/goggles-quickstart)",
        ),
    ] = None,
    units: Annotated[
        UnitsType | None,
        typer.Option(
            help="The measurement units. If not provided, units are derived from search country. Possible values are: - metric: The standardized measurement system - imperial: The British Imperial system of units.",
        ),
    ] = None,
    extra_snippets: Annotated[
        bool,
        typer.Option(
            help="A snippet is an excerpt from a page you get as a result of the query, and extra_snippets allow you to get up to 5 additional, alternative excerpts. Only available under Free AI, Base AI, Pro AI, Base Data, Pro Data and Custom plans",
        ),
    ] = False,
    summary: Annotated[
        bool,
        typer.Option(
            help="This parameter enables summary key generation in web search results. This is required for summarizer to be enabled.",
        ),
    ] = False,
    dump_response: Annotated[
        bool,
        typer.Option(
            help="Dump the raw response from the API into a file (response.json in current working directory)"
        ),
    ] = False,
):
    """Perform a web search."""
    console.print_json(
        asyncio.run(
            BraveSearch().web_search(
                q,
                country=country,
                search_lang=search_lang,
                ui_lang=ui_lang,
                count=count,
                offset=offset,
                safesearch=safesearch,
                freshness=freshness,
                text_decorations=text_decorations,
                spellcheck=spellcheck,
                result_filter=result_filter,
                goggles_id=googles_id,
                units=units,
                extra_snippets=extra_snippets,
                summary=summary,
                dump_response=dump_response,
            )
        ).model_dump_json()
    )


@cli.command()
def image(
    q: Annotated[str, typer.Argument(..., help="The search query to perform")],
    country: Annotated[
        str,
        typer.Option(help="The country to search from (2-letter country code)"),
    ] = "US",
    search_lang: Annotated[
        str,
        typer.Option(help="The language to search in (2 letter language code)"),
    ] = "en",
    count: Annotated[
        int, typer.Option(help="The number of results to return (max 20)")
    ] = 20,
    safesearch: Annotated[
        ImageSafeSearchType,
        typer.Option(help="Enable safe search (off, strict)"),
    ] = ImageSafeSearchType.strict,
    spellcheck: Annotated[bool, typer.Option(help="Enable spellcheck")] = True,
    dump_response: Annotated[
        bool,
        typer.Option(
            help="Dump the raw response from the API into a file (response.json in current working directory)"
        ),
    ] = False,
):
    """Perform a image search."""
    console.print_json(
        asyncio.run(
            BraveSearch().image_search(
                q,
                country=country,
                search_lang=search_lang,
                count=count,
                safesearch=safesearch,
                spellcheck=spellcheck,
                dump_response=dump_response,
            )
        ).model_dump_json()
    )


@cli.command()
def video(
    q: Annotated[str, typer.Argument(..., help="The search query to perform")],
    country: Annotated[
        str,
        typer.Option(help="The country to search from (2-letter country code)"),
    ] = "US",
    search_lang: Annotated[
        str,
        typer.Option(help="The language to search in (2 letter language code)"),
    ] = "en",
    ui_lang: Annotated[str, typer.Option(help="The language to display")] = "en-US",
    count: Annotated[
        int, typer.Option(help="The number of results to return (max 20)")
    ] = 20,
    offset: Annotated[int, typer.Option(help="The offset to start from (max 9)")] = 0,
    freshness: Annotated[
        FreshnessType | None,
        typer.Option(
            help="pd: Discovered within the last 24 hours. - pw: Discovered within the last 7 Days. - pm: Discovered within the last 31 Days. - py: Discovered within the last 365 Days… - YYYY-MM-DDtoYYYY-MM-DD: timeframe is also supported by specifying the date range e.g. 2022-04-01to2022-07-30",
        ),
    ] = None,
    spellcheck: Annotated[bool, typer.Option(help="Enable spellcheck")] = True,
    dump_response: Annotated[
        bool,
        typer.Option(
            help="Dump the raw response from the API into a file (response.json in current working directory)"
        ),
    ] = False,
):
    """Perform a video search."""
    console.print_json(
        asyncio.run(
            BraveSearch().video_search(
                q,
                country=country,
                search_lang=search_lang,
                ui_lang=ui_lang,
                count=count,
                offset=offset,
                freshness=freshness,
                spellcheck=spellcheck,
                dump_response=dump_response,
            )
        ).model_dump_json()
    )


@cli.command()
def news(
    q: Annotated[str, typer.Argument(..., help="The search query to perform")],
    country: Annotated[
        str,
        typer.Option(help="The country to search from (2-letter country code)"),
    ] = "US",
    search_lang: Annotated[
        str,
        typer.Option(help="The language to search in (2 letter language code)"),
    ] = "en",
    ui_lang: Annotated[str, typer.Option(help="The language to display")] = "en-US",
    count: Annotated[
        int, typer.Option(help="The number of results to return (max 20)")
    ] = 20,
    offset: Annotated[int, typer.Option(help="The offset to start from (max 9)")] = 0,
    safesearch: Annotated[
        NewsSafeSearchType,
        typer.Option(help="Enable safe search (off, moderate, strict)"),
    ] = NewsSafeSearchType.moderate,
    freshness: Annotated[
        FreshnessType | None,
        typer.Option(
            help="pd: Discovered within the last 24 hours. - pw: Discovered within the last 7 Days. - pm: Discovered within the last 31 Days. - py: Discovered within the last 365 Days… - YYYY-MM-DDtoYYYY-MM-DD: timeframe is also supported by specifying the date range e.g. 2022-04-01to2022-07-30",
        ),
    ] = None,
    spellcheck: Annotated[bool, typer.Option(help="Enable spellcheck")] = True,
    extra_snippets: Annotated[
        bool,
        typer.Option(
            help="A snippet is an excerpt from a page you get as a result of the query, and extra_snippets allow you to get up to 5 additional, alternative excerpts. Only available under Free AI, Base AI, Pro AI, Base Data, Pro Data and Custom plans",
        ),
    ] = False,
    dump_response: Annotated[
        bool,
        typer.Option(
            help="Dump the raw response from the API into a file (response.json in current working directory)"
        ),
    ] = False,
):
    """Perform a news search."""
    console.print_json(
        asyncio.run(
            BraveSearch().news_search(
                q,
                country=country,
                search_lang=search_lang,
                ui_lang=ui_lang,
                count=count,
                offset=offset,
                safesearch=safesearch,
                freshness=freshness,
                spellcheck=spellcheck,
                extra_snippets=extra_snippets,
                dump_response=dump_response,
            )
        ).model_dump_json()
    )


def _apply_cli_settings(cli: typer.Typer, epilog: str):
    """Add epilog to all typers in the tree"""
    cli.info.epilog = epilog
    cli.info.no_args_is_help = True
    for command in cli.registered_commands:
        command.epilog = cli.info.epilog
        command.no_args_is_help = True


_apply_cli_settings(
    cli,
    f"🦁 Brave Search Python Client v{__version__} - built with love in Berlin 🐻",
)
