from enum import StrEnum

from pydantic import BaseModel, Field, field_validator

from .constants import MAX_QUERY_LENGTH, MAX_QUERY_TERMS


class WebSafeSearchType(StrEnum):
    off = "off"
    moderate = "moderate"
    strict = "strict"


class NewsSafeSearchType(StrEnum):
    off = "off"
    moderate = "moderate"
    strict = "strict"


class ImageSafeSearchType(StrEnum):
    off = "off"
    strict = "strict"


class FreshnessType(StrEnum):
    pd = "pd"
    pw = "pw"
    pm = "pm"
    py = "py"


class UnitsType(StrEnum):
    metric = "metric"
    imperial = "imperial"


class BaseSearchRequest(BaseModel):
    q: str = Field(..., description="The search query to perform")
    country: str = Field("US", max_length=2, description="2-letter country code")
    search_lang: str | None = Field(None, description="Search language preference")
    spellcheck: bool = Field(True, description="Whether to spellcheck query")

    @field_validator("q")
    def validate_query(cls, v: str) -> str:
        if not v:
            raise ValueError("Query must not be empty")
        if len(v) > MAX_QUERY_LENGTH:
            raise ValueError(f"Query exceeding {MAX_QUERY_LENGTH} characters")
        if len(v.split()) > MAX_QUERY_TERMS:
            raise ValueError(f"Query exceeding {MAX_QUERY_TERMS} terms")
        return v


class WebSearchRequest(BaseSearchRequest):
    ui_lang: str = Field("en-US", description="UI language preference")
    count: int = Field(20, le=20, gt=0, description="Number of results (max 20)")
    offset: int = Field(0, le=9, ge=0, description="Result offset (max 9)")
    safesearch: WebSafeSearchType = Field(
        WebSafeSearchType.moderate, description="Safe search level"
    )
    freshness: FreshnessType | None = None
    text_decorations: bool = Field(True, description="Include text decorations")
    result_filter: str | None = None
    goggles_id: str | None = None
    units: UnitsType | None = None
    extra_snippets: bool = Field(False, description="Include extra snippets")
    summary: bool = Field(False, description="Enable summary generation")


class ImageSearchRequest(BaseSearchRequest):
    count: int = Field(50, le=100, gt=0, description="Number of results (max 100)")
    safesearch: ImageSafeSearchType = Field(
        ImageSafeSearchType.strict, description="Safe search level"
    )


class VideoSearchRequest(BaseSearchRequest):
    ui_lang: str = Field("en-US", description="UI language preference")
    count: int = Field(20, le=50, gt=0, description="Number of results (max 50)")
    offset: int = Field(0, le=9, ge=0, description="Result offset (max 9)")
    freshness: FreshnessType | None = None


class NewsSearchRequest(BaseSearchRequest):
    ui_lang: str = Field("en-US", description="UI language preference")
    count: int = Field(20, le=50, gt=0, description="Number of results (max 50)")
    offset: int = Field(0, le=9, ge=0, description="Result offset (max 9)")
    safesearch: NewsSafeSearchType = Field(
        NewsSafeSearchType.strict, description="Safe search level"
    )
    freshness: FreshnessType | None = None
    extra_snippets: bool = Field(False, description="Include extra snippets")
