"""
Pydantic models for the Brave News Search API response objects.

This module provides a complete type-safe representation of the API's response
structure with comprehensive documentation for all models and fields.

Generated using Claude (Sonnet 3.5 new) to create pydantic models and Fields that:
1) Cover all object types and fields
2) Have descriptions for all generated classes and Fields
3) Are expertly engineered
"""

from datetime import datetime
from typing import Literal

from pydantic import BaseModel, Field, HttpUrl


class Thumbnail(BaseModel):
    """
    Aggregated details representing the news thumbnail.

    Provides both served and original URLs for the article's associated image.
    """

    src: HttpUrl = Field(
        description="The served url of the thumbnail associated with the news article",
    )
    original: HttpUrl | None = Field(
        default=None,
        description=("The original url of the thumbnail associated with the news article"),
    )


class MetaUrl(BaseModel):
    """Aggregated information about a URL."""

    scheme: str = Field(description="The protocol scheme extracted from the url")
    netloc: str = Field(description="The network location part extracted from the url")
    hostname: str = Field(
        description="The lowercased domain name extracted from the url",
    )
    favicon: HttpUrl = Field(description="The favicon used for the url")
    path: str = Field(
        description="The hierarchical path of the url useful as a display string",
    )


class Query(BaseModel):
    """
    A model representing information gathered around the requested query.

    Includes any alterations or cleaning performed by the spellchecker.
    """

    original: str = Field(description="The original query that was requested")
    altered: str | None = Field(
        default=None,
        description=("The altered query by the spellchecker. This is the query that is used to search if any"),
    )
    cleaned: str | None = Field(
        default=None,
        description=(
            "The cleaned normalized query by the spellchecker. This is the query that is used to search if any"
        ),
    )
    spellcheck_off: bool = Field(
        description="Whether the spell checker is enabled or disabled",
    )
    show_strict_warning: bool = Field(
        description=(
            "True if the lack of results is due to a 'strict' safesearch setting. "
            "Adult content relevant to the query was found, but was blocked by safesearch"
        ),
    )


class NewsResult(BaseModel):
    """
    A model representing a news result for the requested query.

    Contains comprehensive information about a single news article including
    its metadata, content snippets, and associated media.
    """

    type: Literal["news_result"] = Field(
        description=("The type of news search API result. The value is always news_result"),
    )
    url: HttpUrl = Field(description="The source url of the news article")
    title: str = Field(description="The title of the news article")
    description: str = Field(description="The description for the news article")
    age: str = Field(description="A human readable representation of the page age")
    page_age: str | None = Field(
        default=None,
        description="The page age found from the source web page",
    )
    page_fetched: datetime | None = Field(
        default=None,
        description="The iso date time when the page was last fetched",
    )
    breaking: bool = Field(
        default=False,
        description="Whether the result includes breaking news",
    )
    thumbnail: Thumbnail | None = Field(
        default=None,
        description="The thumbnail for the news article",
    )
    meta_url: MetaUrl = Field(
        description=("Aggregated information on the url associated with the news search result"),
    )
    extra_snippets: list[str] = Field(
        [],
        description="A list of extra alternate snippets for the news search result",
    )


class NewsSearchApiResponse(BaseModel):
    """
    Top level response model for successful News Search API requests.

    This model represents the complete structure of a successful API response,
    containing the query information and resulting news articles.

    Note: The API can also respond back with an error response based on
    invalid subscription keys and rate limit events.
    """

    type: Literal["news"] = Field(
        description="The type of search API result. The value is always news",
    )
    query: Query = Field(description="News search query string and related metadata")
    results: list[NewsResult] = Field(
        description="The list of news results for the given query",
    )
