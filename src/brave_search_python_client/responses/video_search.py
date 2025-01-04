"""
Pydantic models for video search API responses.

Contains metadata, thumbnails, and related information for video search results.

Generated using Claude (Sonnet 3.5 new) to create pydantic models and Fields:
1) Must cover all object types and fields
2) Must have descriptions for all generated classes and Fields
3) Must be expertly engineered code
"""

from datetime import datetime
from typing import Literal

from pydantic import BaseModel, Field, HttpUrl


class Query(BaseModel):
    """
    A model representing information gathered around the requested query.

    Includes original query, any alterations, and spell check information.
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
            "Adult content relevant to the query was found, but was blocked by "
            "safesearch"
        ),
    )


class Thumbnail(BaseModel):
    """
    Aggregated details representing the video thumbnail.

    Includes both served and original URLs.
    """

    src: HttpUrl = Field(
        description="The served url of the thumbnail associated with the video",
    )
    original: HttpUrl = Field(
        description="The original url of the thumbnail associated with the video",
    )


class Profile(BaseModel):
    """
    A profile of an entity (usually a creator or publisher) associated with the video.

    Includes identification and visual information.
    """

    name: str = Field(description="The name of the profile")
    long_name: str | None = Field(None, description="The long name of the profile")
    url: HttpUrl = Field(description="The original url where the profile is available")
    img: HttpUrl | None = Field(
        default=None,
        description="The served image url representing the profile",
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


class VideoData(BaseModel):
    """
    A comprehensive model representing metadata gathered for a video.

    Includes duration, viewership, creator information, and tags.
    """

    duration: str | None = Field(
        default=None,
        description="A time string representing the duration of the video",
    )
    views: int | None = Field(None, description="The number of views of the video")
    creator: str | None = Field(None, description="The creator of the video")
    publisher: str | None = Field(None, description="The publisher of the video")
    requires_subscription: bool | None = Field(
        default=None,
        description="Whether the video requires a subscription",
    )
    tags: list[str] = Field([], description="A list of tags relevant to the video")
    author: Profile | None = Field(
        default=None,
        description="A profile associated with the video",
    )


class VideoResult(BaseModel):
    """
    A comprehensive model representing a video result for the requested query.

    Includes metadata, thumbnails, and associated information.
    """

    type: Literal["video_result"] = Field(
        description="The type of video search API result. Always 'video_result'",
    )
    url: HttpUrl = Field(description="The source url of the video")
    title: str = Field(description="The title of the video")
    description: str = Field(description="The description for the video")
    age: str | None = Field(
        default=None,
        description="A human readable representation of the page age",
    )
    page_age: str | None = Field(
        default=None,
        description="The page age found from the source web page",
    )
    page_fetched: datetime | None = Field(
        default=None,
        description=("The ISO date time when the page was last fetched (format: YYYY-MM-DDTHH:MM:SSZ)"),
    )
    thumbnail: Thumbnail = Field(description="The thumbnail for the video")
    video: VideoData = Field(description="Metadata for the video")
    meta_url: MetaUrl = Field(
        description=("Aggregated information on the url associated with the video search result"),
    )


class VideoSearchApiResponse(BaseModel):
    """
    Top level response model for successful Video Search API requests.

    Contains the query information and a list of video results.
    """

    type: Literal["videos"] = Field(
        description="The type of search API result. Always 'videos'",
    )
    query: Query = Field(
        description="Video search query string and related information",
    )
    results: list[VideoResult] = Field(
        description="The list of video results for the given query",
    )
