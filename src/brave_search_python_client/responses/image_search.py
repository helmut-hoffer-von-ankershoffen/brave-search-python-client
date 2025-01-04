"""
Pydantic models for the Brave Image Search API response objects.

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


class MetaUrl(BaseModel):
    """Aggregated information about a URL."""

    scheme: str = Field(description="The protocol scheme extracted from the url")
    netloc: str = Field(description="The network location part extracted from the url")
    hostname: str = Field(
        description="The lowercased domain name extracted from the url",
    )
    favicon: str = Field(description="The favicon used for the url")
    path: str = Field(
        description="The hierarchical path of the url useful as a display string",
    )


class Properties(BaseModel):
    """Metadata on an image."""

    url: HttpUrl = Field(description="The image URL")
    placeholder: HttpUrl = Field(
        description="The lower resolution placeholder image url",
    )


class Thumbnail(BaseModel):
    """Aggregated details representing the image thumbnail."""

    src: HttpUrl = Field(description="The served url of the image")


class ImageResult(BaseModel):
    """A model representing an image result for the requested query."""

    type: Literal["image_result"] = Field(
        description=("The type of image search API result. The value is always image_result"),
    )
    title: str = Field(description="The title of the image")
    url: HttpUrl = Field(description="The original page url where the image was found")
    source: str = Field(
        description=("The source domain where the image was found"),
    )
    page_fetched: datetime = Field(
        description=("The iso date time when the page was last fetched. The format is YYYY-MM-DDTHH:MM:SSZ"),
    )
    thumbnail: Thumbnail = Field(description="The thumbnail for the image")
    properties: Properties = Field(description="Metadata for the image")
    meta_url: MetaUrl = Field(
        description=("Aggregated information on the url associated with the image search result"),
    )


class Query(BaseModel):
    """A model representing information gathered around the requested query."""

    original: str = Field(description="The original query that was requested")
    altered: str | None = Field(
        default=None,
        description=("The altered query by the spellchecker. This is the query that is used to search"),
    )
    spellcheck_off: bool = Field(
        description="Whether the spell checker is enabled or disabled",
    )
    show_strict_warning: bool = Field(
        description=(
            "The value is True if the lack of results is due to a 'strict' safesearch setting. "
            "Adult content relevant to the query was found, but was blocked by safesearch"
        ),
    )


class ImageSearchApiResponse(BaseModel):
    """
    Top level response model for successful Image Search API requests.

    The API can also respond back with an error response based on invalid subscription keys and rate limit events.
    """

    type: Literal["images"] = Field(
        description="The type of search API result. The value is always images",
    )
    query: Query = Field(description="Image search query string")
    results: list[ImageResult] = Field(
        description="The list of image results for the given query",
    )
