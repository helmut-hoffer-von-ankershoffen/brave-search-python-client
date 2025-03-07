"""
Pydantic models representing Brave Web Search API response objects.

This module provides a complete type-safe interface for working with Brave Search
API responses.
"""

from typing import Any, Literal

from pydantic import BaseModel, Field

# Common field descriptions
DESC_INFOBOX_SUBTYPE = "The infobox subtype identifier"
DESC_THUMBNAIL = "A thumbnail associated with the"  # Note: Usually followed by entity type
DESC_TYPE_IDENTIFIER = "The type identifier for"  # Note: Usually followed by entity type
DESC_AGGREGATED_INFO = "Aggregated information on"  # Note: Usually followed by entity type


class Language(BaseModel):
    """A model representing a language."""

    main: str = Field(description="The main language seen in the string")


class Profile(BaseModel):
    """A profile of an entity."""

    name: str = Field(description="The name of the profile")
    long_name: str = Field(description="The long name of the profile")
    url: str | None = Field(
        default=None,
        description="The original url where the profile is available",
    )
    img: str | None = Field(
        default=None,
        description="The served image url representing the profile",
    )


class Result(BaseModel):
    """A model representing a web search result."""

    title: str = Field(description="The title of the web page")
    url: str = Field(description="The url where the page is served")
    is_source_local: bool = Field(
        default=False,
        description="Indicates if the source is local",
    )  # Added default value
    is_source_both: bool = Field(
        default=False,
        description="Indicates if the source is both local and non-local",
    )  # Added default value
    description: str | None = Field(
        default=None,
        description="A description for the web page",
    )
    page_age: str | None = Field(
        default=None,
        description="A date representing the age of the web page",
    )
    page_fetched: str | None = Field(
        default=None,
        description="A date representing when the web page was last fetched",
    )
    profile: Profile | None = Field(
        default=None,
        description="A profile associated with the web page",
    )
    language: str | None = Field(
        default=None,
        description="A language classification for the web page",
    )
    family_friendly: bool = Field(
        default=False,
        description="Whether the web page is family friendly",
    )  # Added default value


class MetaUrl(BaseModel):
    """Aggregated information about a url."""

    scheme: str = Field(description="The protocol scheme extracted from the url")
    netloc: str = Field(description="The network location part extracted from the url")
    hostname: str | None = Field(
        default=None,
        description="The lowercased domain name extracted from the url",
    )
    favicon: str = Field(description="The favicon used for the url")
    path: str = Field(
        description="The hierarchical path of the url useful as a display string",
    )


class Thumbnail(BaseModel):
    """Aggregated details representing a picture thumbnail."""

    src: str = Field(description="The served url of the picture thumbnail")
    original: str | None = Field(
        default=None,
        description="The original url of the image",
    )


class ImageProperties(BaseModel):
    """Metadata on an image."""

    url: str = Field(description="The original image URL")
    resized: str = Field(description="The url for a better quality resized image")
    placeholder: str = Field(description="The placeholder image url")
    height: int | None = Field(default=None, description="The image height")
    width: int | None = Field(default=None, description="The image width")
    format: str | None = Field(default=None, description="The image format")
    content_size: str | None = Field(default=None, description="The image size")


class Image(BaseModel):
    """A model describing an image."""

    thumbnail: Thumbnail = Field(description="The thumbnail associated with the image")
    url: str | None = Field(default=None, description="The url of the image")
    properties: ImageProperties | None = Field(
        default=None,
        description="Metadata on the image",
    )


class VideoData(BaseModel):
    """A model representing metadata gathered for a video."""

    duration: str | None = Field(
        default=None,
        description="The duration of the video (HH:MM:SS or MM:SS)",
    )
    views: str | None = Field(
        default=None,
        description="The number of views of the video",
    )
    creator: str | None = Field(default=None, description="The creator of the video")
    publisher: str | None = Field(
        default=None,
        description="The publisher of the video",
    )
    thumbnail: Thumbnail | None = Field(
        default=None,
        description="A thumbnail associated with the video",
    )
    tags: list[str] | None = Field(
        default=None,
        description="A list of tags associated with the video",
    )
    author: Profile | None = Field(default=None, description="Author of the video")
    requires_subscription: bool | None = Field(
        default=None,
        description="Whether the video requires a subscription to watch",
    )


class Rating(BaseModel):
    """The rating associated with an entity."""

    ratingValue: float = Field(description="The current value of the rating")
    bestRating: float = Field(description="Best rating received")
    reviewCount: int | None = Field(
        default=None,
        description="The number of reviews associated with the rating",
    )
    profile: Profile | None = Field(
        default=None,
        description="The profile associated with the rating",
    )
    is_tripadvisor: bool = Field(
        description="Whether the rating is coming from Tripadvisor",
    )


class Person(BaseModel):
    """A model describing a person entity."""

    type: Literal["person"] = Field(description="A type identifying a person")
    name: str = Field(description="The name of the person")
    url: str | None = Field(default=None, description="A url for the person")
    thumbnail: Thumbnail | None = Field(
        default=None,
        description="Thumbnail associated with the person",
    )


class Organization(BaseModel):
    """An entity responsible for another entity."""

    type: Literal["organization"] = Field(
        description="A type string identifying an organization",
    )
    name: str = Field(description="The name of the organization")
    url: str | None = Field(default=None, description="A url for the organization")
    contact_points: list["ContactPoint"] | None = Field(
        default=None,
        description="A list of contact points for the organization",
    )


class ContactPoint(BaseModel):
    """A way to contact an entity."""

    type: Literal["contact_point"] = Field(
        description="A type string identifying a contact point",
    )
    telephone: str | None = Field(
        default=None,
        description="The telephone number of the entity",
    )
    email: str | None = Field(
        default=None,
        description="The email address of the entity",
    )


class PostalAddress(BaseModel):
    """A model representing a postal address of a location."""

    type: Literal["PostalAddress"] = Field(
        description="The type identifying a postal address",
    )
    country: str | None = Field(
        default=None,
        description="The country associated with the location",
    )
    postalCode: str | None = Field(
        default=None,
        description="The postal code associated with the location",
    )
    streetAddress: str | None = Field(
        default=None,
        description="The street address associated with the location",
    )
    addressRegion: str | None = Field(
        default=None,
        description="The region associated with the location (usually a state)",
    )
    addressLocality: str | None = Field(
        default=None,
        description="The address locality or subregion associated with the location",
    )
    displayAddress: str = Field(description="The displayed address string")


class DayOpeningHours(BaseModel):
    """
    A model representing the opening hours.

    Opening hours are for a particular day for a business at a particular location.
    Contains the opening and closing hours for a specific day of the week.
    """

    abbr_name: str = Field(
        description="A short string representing the day of the week",
    )
    full_name: str = Field(description="A full string representing the day of the week")
    opens: str = Field(
        description="A 24 hr clock time string for the opening time of the business",
    )
    closes: str = Field(
        description="A 24 hr clock time string for the closing time of the business",
    )


class OpeningHours(BaseModel):
    """Opening hours of a business at a particular location."""

    current_day: list[DayOpeningHours] | None = Field(
        default=None,
        description="The current day opening hours",
    )
    days: list[list[DayOpeningHours]] | None = Field(
        default=None,
        description="The opening hours for the whole week",
    )


class Unit(BaseModel):
    """A model representing a unit of measurement."""

    value: float = Field(description="The quantity of the unit")
    units: str = Field(description="The name of the unit associated with the quantity")


class DataProvider(BaseModel):
    """A model representing the data provider associated with the entity."""

    type: Literal["external"] = Field(
        description="The type representing the source of data",
    )
    name: str = Field(description="The name of the data provider")
    url: str = Field(description="The url where the information is coming from")
    long_name: str | None = Field(
        default=None,
        description="The long name for the data provider",
    )
    img: str | None = Field(
        default=None,
        description="The served url for the image data",
    )


class LocationWebResult(Result):
    """A model representing a web result related to a location."""

    meta_url: MetaUrl = Field(description="Aggregated information about the url")


class PictureResults(BaseModel):
    """A model representing a list of pictures."""

    viewMoreUrl: str | None = Field(
        default=None,
        description="A url to view more pictures",
    )
    results: list[Thumbnail] = Field(description="A list of thumbnail results")


class Reviews(BaseModel):
    """The reviews associated with an entity."""

    results: list["TripAdvisorReview"] = Field(
        description="A list of trip advisor reviews for the entity",
    )
    viewMoreUrl: str = Field(
        description=("A url to a web page where more information on the result can be seen"),
    )
    reviews_in_foreign_language: bool = Field(
        description="Any reviews available in a foreign language",
    )


class TripAdvisorReview(BaseModel):
    """A model representing a Tripadvisor review."""

    title: str = Field(description="The title of the review")
    description: str = Field(description="A description seen in the review")
    date: str = Field(description="The date when the review was published")
    rating: Rating = Field(description="A rating given by the reviewer")
    author: Person = Field(description="The author of the review")
    review_url: str = Field(
        description="A url link to the page where the review can be found",
    )
    language: str = Field(description="The language of the review")


class LocationResult(Result):
    """A result that is location relevant."""

    type: Literal["location_result"] = Field(
        description="Location result type identifier",
    )
    id: str | None = Field(
        default=None,
        description="A Temporary id associated with this result (valid for 8 hours)",
    )
    provider_url: str = Field(description="The complete url of the provider")
    coordinates: list[float] | None = Field(
        default=None,
        description="A list of coordinates associated with the location",
    )
    zoom_level: int = Field(description="The zoom level on the map")
    thumbnail: Thumbnail | None = Field(
        default=None,
        description="The thumbnail associated with the location",
    )
    postal_address: PostalAddress | None = Field(
        default=None,
        description="The postal address associated with the location",
    )
    opening_hours: OpeningHours | None = Field(
        default=None,
        description="The opening hours associated with the location",
    )
    contact: ContactPoint | None = Field(
        default=None,
        description="The contact of the business associated with the location",
    )
    price_range: str | None = Field(
        default=None,
        description="A display string used to show the price classification",
    )
    rating: Rating | None = Field(
        default=None,
        description="The ratings of the business",
    )
    distance: Unit | None = Field(
        default=None,
        description="The distance of the location from the client",
    )
    profiles: list[DataProvider] | None = Field(
        default=None,
        description="Profiles associated with the business",
    )
    reviews: Reviews | None = Field(
        default=None,
        description="Aggregated reviews from various sources",
    )
    pictures: PictureResults | None = Field(
        default=None,
        description="Pictures associated with the business",
    )
    serves_cuisine: list[str] | None = Field(
        default=None,
        description="A list of cuisine categories served",
    )
    categories: list[str] | None = Field(
        default=None,
        description="A list of categories",
    )
    icon_category: str | None = Field(default=None, description="An icon category")
    results: LocationWebResult | None = Field(
        default=None,
        description="Web results related to this location",
    )
    timezone: str | None = Field(default=None, description="IANA timezone identifier")
    timezone_offset: str | None = Field(
        default=None,
        description="The utc offset of the timezone",
    )


class Locations(BaseModel):
    """A model representing location results."""

    type: Literal["locations"] = Field(description="Location type identifier")
    results: list[LocationResult] = Field(
        description="An aggregated list of location sensitive results",
    )


class LocationDescription(BaseModel):
    """AI generated description of a location result."""

    type: Literal["local_description"] = Field(
        description="The type of a location description",
    )
    id: str = Field(description="A Temporary id of the location with this description")
    description: str | None = Field(
        default=None,
        description="AI generated description of the location",
    )


class QA(BaseModel):
    """A question answer result."""

    question: str = Field(description="The question being asked")
    answer: str = Field(description="The answer to the question")
    title: str = Field(description="The title of the post")
    url: str = Field(description="The url pointing to the post")
    meta_url: MetaUrl | None = Field(
        default=None,
        description="Aggregated information about the url",
    )


class FAQ(BaseModel):
    """Frequently asked questions relevant to the search query term."""

    type: Literal["faq"] = Field(description="The FAQ result type identifier")
    results: list[QA] = Field(
        description="A list of aggregated question answer results",
    )


class ForumData(BaseModel):
    """Defines a result from a discussion forum."""

    forum_name: str = Field(description="The name of the forum")
    num_answers: int | None = Field(
        default=None,
        description="The number of answers to the post",
    )
    score: str | None = Field(
        default=None,
        description="The score of the post on the forum",
    )
    title: str | None = Field(
        default=None,
        description="The title of the post on the forum",
    )
    question: str | None = Field(
        default=None,
        description="The question asked in the forum post",
    )
    top_comment: str | None = Field(
        default=None,
        description="The top-rated comment under the forum post",
    )


class Answer(BaseModel):
    """A response representing an answer to a question on a forum."""

    text: str = Field(description="The main content of the answer")
    author: str | None = Field(
        default=None,
        description="The name of the author of the answer",
    )
    upvoteCount: int | None = Field(
        default=None,
        description="Number of upvotes on the answer",
    )
    downvoteCount: int | None = Field(
        default=None,
        description="The number of downvotes on the answer",
    )


class QAPage(BaseModel):
    """Aggregated result from a question answer page."""

    question: str = Field(description="The question that is being asked")
    answer: Answer = Field(description="An answer to the question")


class DiscussionResult(Result):
    """
    A discussion result.

    These are forum posts and discussions that are relevant to the search query.
    """

    type: Literal["discussion"] = Field(
        description="The discussion result type identifier",
    )
    data: ForumData | None = Field(
        default=None,
        description="The enriched aggregated data for the relevant forum post",
    )


class Discussions(BaseModel):
    """A model representing a discussion cluster relevant to the query."""

    type: Literal["search"] = Field(
        description="The type identifying a discussion cluster",
    )
    results: list[DiscussionResult] = Field(description="A list of discussion results")
    mutated_by_goggles: bool = Field(
        description="Whether the discussion results are changed by a Goggle",
    )


class Query(BaseModel):
    """A model representing information gathered around the requested query."""

    original: str = Field(description="The original query that was requested")
    show_strict_warning: bool | None = Field(
        default=None,
        description=("Whether there is more content available for query, but restricted due to safesearch"),
    )
    altered: str | None = Field(
        default=None,
        description="The altered query for which the search was performed",
    )
    safesearch: bool | None = Field(
        default=None,
        description="Whether safesearch was enabled",
    )
    is_navigational: bool | None = Field(
        default=None,
        description="Whether the query is a navigational query to a domain",
    )
    is_geolocal: bool | None = Field(
        default=None,
        description="Whether the query has location relevance",
    )
    local_decision: str | None = Field(
        default=None,
        description="Whether the query was decided to be location sensitive",
    )
    local_locations_idx: int | None = Field(
        default=None,
        description="The index of the location",
    )
    is_trending: bool | None = Field(
        default=None,
        description="Whether the query is trending",
    )
    is_news_breaking: bool | None = Field(
        default=None,
        description="Whether the query has news breaking articles relevant to it",
    )
    ask_for_location: bool | None = Field(
        default=None,
        description=("Whether the query requires location information for better results"),
    )
    language: Language | None = Field(
        default=None,
        description="The language information gathered from the query",
    )
    spellcheck_off: bool | None = Field(
        default=None,
        description="Whether the spellchecker was off",
    )
    country: str | None = Field(default=None, description="The country that was used")
    bad_results: bool | None = Field(
        default=None,
        description="Whether there are bad results for the query",
    )
    should_fallback: bool | None = Field(
        default=None,
        description="Whether the query should use a fallback",
    )
    lat: str | None = Field(
        default=None,
        description="The gathered location latitude associated with the query",
    )
    long: str | None = Field(
        default=None,
        description="The gathered location longitude associated with the query",
    )
    postal_code: str | None = Field(
        default=None,
        description="The gathered postal code associated with the query",
    )
    city: str | None = Field(
        default=None,
        description="The gathered city associated with the query",
    )
    state: str | None = Field(
        default=None,
        description="The gathered state associated with the query",
    )
    header_country: str | None = Field(
        default=None,
        description="The country for the request origination",
    )
    more_results_available: bool | None = Field(
        default=None,
        description="Whether more results are available for the given query",
    )
    custom_location_label: str | None = Field(
        default=None,
        description="Any custom location labels attached to the query",
    )
    reddit_cluster: str | None = Field(
        default=None,
        description="Any reddit cluster associated with the query",
    )


class VideoResult(Result):
    """A model representing a video result."""

    type: Literal["video_result"] = Field(
        description="The type identifying the video result",
    )
    video: VideoData = Field(description="Meta data for the video")
    meta_url: MetaUrl | None = Field(
        default=None,
        description="Aggregated information on the URL",
    )
    thumbnail: Thumbnail | None = Field(
        default=None,
        description="The thumbnail of the video",
    )
    age: str | None = Field(
        default=None,
        description="A string representing the age of the video",
    )


class Videos(BaseModel):
    """A model representing video results."""

    type: Literal["videos"] = Field(description="The type representing the videos")
    results: list[VideoResult] = Field(description="A list of video results")
    mutated_by_goggles: bool | None = Field(
        default=False,
        description="Whether the video results are changed by a Goggle",
    )


class NewsResult(Result):
    """A model representing news results."""

    meta_url: MetaUrl | None = Field(
        default=None,
        description="The aggregated information on the url representing a news result",
    )
    source: str | None = Field(default=None, description="The source of the news")
    breaking: bool = Field(
        description="Whether the news result is currently a breaking news",
    )
    is_live: bool = Field(description="Whether the news result is currently live")
    thumbnail: Thumbnail | None = Field(
        default=None,
        description="The thumbnail associated with the news result",
    )
    age: str | None = Field(
        default=None,
        description="A string representing the age of the news article",
    )
    extra_snippets: list[str] | None = Field(
        default=None,
        description="A list of extra alternate snippets for the news search result",
    )


class News(BaseModel):
    """A model representing news results."""

    type: Literal["news"] = Field(description="The type representing the news")
    results: list[NewsResult] = Field(description="A list of news results")
    mutated_by_goggles: bool | None = Field(
        default=False,
        description="Whether the news results are changed by a Goggle",
    )


class ButtonResult(BaseModel):
    """A result which can be used as a button."""

    type: Literal["button_result"] = Field(
        description="A type identifying button result",
    )
    title: str = Field(description="The title of the result")
    url: str = Field(description="The url for the button result")


class DeepResult(BaseModel):
    """Aggregated deep results from news, social, videos and images."""

    news: list[NewsResult] | None = Field(
        default=None,
        description="A list of news results associated with the result",
    )
    buttons: list[ButtonResult] | None = Field(
        default=None,
        description="A list of buttoned results associated with the result",
    )
    videos: list[VideoResult] | None = Field(
        default=None,
        description="Videos associated with the result",
    )
    images: list[Image] | None = Field(
        default=None,
        description="Images associated with the result",
    )


class Price(BaseModel):
    """A model representing the price for an entity."""

    price: str = Field(description="The price value in a given currency")
    price_currency: str = Field(description="The currency of the price value")


class Offer(BaseModel):
    """An offer associated with a product."""

    url: str = Field(description="The url where the offer can be found")
    priceCurrency: str = Field(description="The currency in which the offer is made")
    price: str = Field(description="The price of the product currently on offer")


class Product(BaseModel):
    """A model representing a product."""

    type: Literal["Product"] = Field(description="A string representing a product type")
    name: str = Field(description="The name of the product")
    category: str | None = Field(
        default=None,
        description="The category of the product",
    )
    price: str = Field(description="The price of the product")
    thumbnail: Thumbnail = Field(description="A thumbnail associated with the product")
    description: str | None = Field(
        default=None,
        description="The description of the product",
    )
    offers: list[Offer] | None = Field(
        default=None,
        description="A list of offers available on the product",
    )
    rating: Rating | None = Field(
        default=None,
        description="A rating associated with the product",
    )


class Review(BaseModel):
    """A model representing a review for an entity."""

    type: Literal["review"] = Field(description="A string representing review type")
    name: str = Field(description="The review title for the review")
    thumbnail: Thumbnail = Field(
        description="The thumbnail associated with the reviewer",
    )
    description: str = Field(
        description="A description of the review (the text of the review itself)",
    )
    rating: Rating = Field(description="The ratings associated with the review")


class Software(BaseModel):
    """A model representing a software entity."""

    name: str | None = Field(
        default=None,
        description="The name of the software product",
    )
    author: str | None = Field(
        default=None,
        description="The author of software product",
    )
    version: str | None = Field(
        default=None,
        description="The latest version of the software product",
    )
    codeRepository: str | None = Field(
        default=None,
        description="The code repository where the software product is maintained",
    )
    homepage: str | None = Field(
        default=None,
        description="The home page of the software product",
    )
    datePublisher: str | None = Field(
        default=None,
        description="The date when the software product was published",
    )
    is_npm: bool | None = Field(
        default=None,
        description="Whether the software product is available on npm",
    )
    is_pypi: bool | None = Field(
        default=None,
        description="Whether the software product is available on pypi",
    )
    stars: int | None = Field(
        default=None,
        description="The number of stars on the repository",
    )
    forks: int | None = Field(
        default=None,
        description="The numbers of forks of the repository",
    )
    ProgrammingLanguage: str | None = Field(
        default=None,
        description="The programming language used in the software product",
    )


class HowTo(BaseModel):
    """Aggregated information on a how to."""

    text: str = Field(description="The how to text")
    name: str | None = Field(default=None, description="A name for the how to")
    url: str | None = Field(
        default=None,
        description="A url associated with the how to",
    )
    image: list[str] | None = Field(
        default=None,
        description="A list of image urls associated with the how to",
    )


class Recipe(BaseModel):
    """Aggregated information on a recipe."""

    title: str = Field(description="The title of the recipe")
    description: str = Field(description="The description of the recipe")
    thumbnail: Thumbnail = Field(description="A thumbnail associated with the recipe")
    url: str = Field(description="The url of the web page where the recipe was found")
    domain: str = Field(
        description="The domain of the web page where the recipe was found",
    )
    favicon: str = Field(
        description=("The url for the favicon of the web page where the recipe was found"),
    )
    time: str | None = Field(
        default=None,
        description="The total time required to cook the recipe",
    )
    prep_time: str | None = Field(
        default=None,
        description="The preparation time for the recipe",
    )
    cook_time: str | None = Field(
        default=None,
        description="The cooking time for the recipe",
    )
    ingredients: str | None = Field(
        default=None,
        description="Ingredients required for the recipe",
    )
    instructions: list[HowTo] | None = Field(
        default=None,
        description="List of instructions for the recipe",
    )
    servings: int | None = Field(
        default=None,
        description="How many people the recipe serves",
    )
    calories: int | None = Field(
        default=None,
        description="Calorie count for the recipe",
    )
    rating: Rating | None = Field(
        default=None,
        description="Aggregated information on the ratings",
    )
    recipeCategory: str | None = Field(
        default=None,
        description="The category of the recipe",
    )
    recipeCuisine: str | None = Field(
        default=None,
        description="The cuisine classification for the recipe",
    )
    video: VideoData | None = Field(
        default=None,
        description="Aggregated information on the cooking video",
    )


class Book(BaseModel):
    """A model representing a book result."""

    title: str = Field(description="The title of the book")
    author: list[Person] = Field(description="The author of the book")
    date: str | None = Field(
        default=None,
        description="The publishing date of the book",
    )
    price: Price | None = Field(default=None, description="The price of the book")
    pages: int | None = Field(
        default=None,
        description="The number of pages in the book",
    )
    publisher: Person | None = Field(
        default=None,
        description="The publisher of the book",
    )
    rating: Rating | None = Field(
        default=None,
        description="A gathered rating from different sources",
    )


class Article(BaseModel):
    """A model representing an article."""

    author: list[Person] | None = Field(
        default=None,
        description="The author of the article",
    )
    date: str | None = Field(
        default=None,
        description="The date when the article was published",
    )
    publisher: Organization | None = Field(
        default=None,
        description="The name of the publisher for the article",
    )
    thumbnail: Thumbnail | None = Field(
        default=None,
        description="A thumbnail associated with the article",
    )
    isAccessibleForFree: bool | None = Field(
        default=None,
        description="Whether the article is free to read or behind a paywall",
    )


class CreativeWork(BaseModel):
    """A creative work relevant to the query."""

    name: str = Field(description="The name of the creative work")
    thumbnail: Thumbnail = Field(
        description="A thumbnail associated with the creative work",
    )
    rating: Rating | None = Field(
        default=None,
        description="A rating that is given to the creative work",
    )


class MusicRecording(BaseModel):
    """Result classified as a music label or a song."""

    name: str = Field(description="The name of the song or album")
    thumbnail: Thumbnail | None = Field(
        default=None,
        description="A thumbnail associated with the music",
    )
    rating: Rating | None = Field(default=None, description="The rating of the music")


class MovieData(BaseModel):
    """Aggregated data for a movie result."""

    name: str | None = Field(default=None, description="Name of the movie")
    description: str | None = Field(
        default=None,
        description="A short plot summary for the movie",
    )
    url: str | None = Field(
        default=None,
        description="A url serving a movie profile page",
    )
    thumbnail: Thumbnail | None = Field(
        default=None,
        description="A thumbnail for a movie poster",
    )
    release: str | None = Field(
        default=None,
        description="The release date for the movie",
    )
    directors: list[Person] | None = Field(
        default=None,
        description="A list of people responsible for directing the movie",
    )
    actors: list[Person] | None = Field(
        default=None,
        description="A list of actors in the movie",
    )
    rating: Rating | None = Field(
        default=None,
        description="Rating provided to the movie from various sources",
    )
    duration: str | None = Field(
        default=None,
        description="The runtime of the movie (format: HH:MM:SS)",
    )
    genre: list[str] | None = Field(
        default=None,
        description="List of genres in which the movie can be classified",
    )
    query: str | None = Field(
        default=None,
        description="The query that resulted in the movie result",
    )


class SearchResult(Result):
    """Aggregated information on a web search result, relevant to the query."""

    type: Literal["search_result"] = Field(
        description="A type identifying a web search result",
    )
    subtype: str = Field(
        description="A sub type identifying the web search result type",
    )  # changed from Literal["generic'] to str]
    is_live: bool = Field(
        default=False,
        description="Whether the web search result is currently live",
    )
    deep_results: DeepResult | None = Field(
        default=None,
        description="Gathered information on a web search result",
    )
    schemas: list[list[Any]] | None = Field(
        default=None,
        description="A list of schemas (structured data) extracted from the page",
    )
    meta_url: MetaUrl | None = Field(
        default=None,
        description="Aggregated information on the url associated with the result",
    )
    thumbnail: Thumbnail | None = Field(
        default=None,
        description="The thumbnail of the web search result",
    )
    age: str | None = Field(
        default=None,
        description="A string representing the age of the web search result",
    )
    language: str | None = Field(
        default=None,
        description="The main language on the web search result",
    )
    location: LocationResult | None = Field(
        default=None,
        description="The location details if the query relates to a restaurant",
    )
    video: VideoData | None = Field(
        default=None,
        description="The video associated with the web search result",
    )
    movie: MovieData | None = Field(
        default=None,
        description="The movie associated with the web search result",
    )
    faq: FAQ | None = Field(
        default=None,
        description=("Any frequently asked questions associated with the web search result"),
    )
    qa: QAPage | None = Field(
        default=None,
        description="Any question answer information associated with the result page",
    )
    book: Book | None = Field(
        default=None,
        description="Any book information associated with the web search result page",
    )
    rating: Rating | None = Field(
        default=None,
        description="Rating found for the web search result page",
    )
    article: Article | None = Field(
        default=None,
        description="An article found for the web search result page",
    )
    product: Product | Review | None = Field(
        default=None,
        description="The main product and review found on the page",
    )
    product_cluster: list[Product | Review] | None = Field(
        default=None,
        description="A list of products and reviews",
    )
    cluster_type: str | None = Field(
        default=None,
        description="A type representing a cluster",
    )
    cluster: list[Result] | None = Field(
        default=None,
        description="A list of web search results",
    )
    creative_work: CreativeWork | None = Field(
        default=None,
        description="Aggregated information on the creative work",
    )
    music_recording: MusicRecording | None = Field(
        default=None,
        description="Aggregated information on music recording",
    )
    review: Review | None = Field(
        default=None,
        description="Aggregated information on the review",
    )
    software: Software | None = Field(
        default=None,
        description="Aggregated information on a software product",
    )
    recipe: Recipe | None = Field(
        default=None,
        description="Aggregated information on a recipe",
    )
    organization: Organization | None = Field(
        default=None,
        description="Aggregated information on an organization",
    )
    content_type: str | None = Field(
        default=None,
        description="The content type associated with the search result page",
    )
    extra_snippets: list[str] | None = Field(
        default=None,
        description="A list of extra alternate snippets for the web search result",
    )


class Search(BaseModel):
    """A model representing a collection of web search results."""

    type: Literal["search"] = Field(description="A type identifying web search results")
    results: list[SearchResult] = Field(description="A list of search results")
    family_friendly: bool = Field(description="Whether the results are family friendly")


class ResultReference(BaseModel):
    """The ranking order of results on a search result page."""

    type: str = Field(description="The type of the result")
    index: int | None = Field(
        default=None,
        description="The 0th based index where the result should be placed",
    )
    all: bool = Field(
        description="Whether to put all the results from the type at specific position",
    )


class MixedResponse(BaseModel):
    """The ranking order of results on a search result page."""

    type: Literal["mixed"] = Field(description="The type representing the model mixed")
    main: list[ResultReference] | None = Field(
        default=None,
        description="The ranking order for the main section",
    )
    top: list[ResultReference] | None = Field(
        default=None,
        description="The ranking order for the top section",
    )
    side: list[ResultReference] | None = Field(
        default=None,
        description="The ranking order for the side section",
    )


class AbstractGraphInfobox(Result):
    """Shared aggregated information on an entity from a knowledge graph."""

    type: Literal["infobox"] = Field(description="The infobox result type identifier")
    position: int = Field(description="The position on a search result page")
    label: str | None = Field(
        default=None,
        description="Any label associated with the entity",
    )
    category: str | None = Field(
        default=None,
        description="Category classification for the entity",
    )
    long_desc: str | None = Field(
        default=None,
        description="A longer description for the entity",
    )
    thumbnail: Thumbnail | None = Field(
        default=None,
        description="The thumbnail associated with the entity",
    )
    attributes: list[list[str]] | None = Field(
        default=None,
        description="A list of attributes about the entity",
    )
    profiles: list[Profile] | list[DataProvider] | None = Field(
        default=None,
        description="The profiles associated with the entity",
    )
    website_url: str | None = Field(
        default=None,
        description="The official website pertaining to the entity",
    )
    ratings: list[Rating] | None = Field(
        default=None,
        description="Any ratings given to the entity",
    )
    providers: list[DataProvider] | None = Field(
        default=None,
        description="A list of data sources for the entity",
    )
    distance: Unit | None = Field(
        default=None,
        description="A unit representing quantity relevant to the entity",
    )
    images: list[Thumbnail] | None = Field(
        default=None,
        description="A list of images relevant to the entity",
    )
    movie: MovieData | None = Field(
        default=None,
        description="Any movie data relevant to the entity",
    )


class GenericInfobox(AbstractGraphInfobox):
    """Aggregated information on a generic entity from a knowledge graph."""

    subtype: Literal["generic"] = Field(description=DESC_INFOBOX_SUBTYPE)
    found_in_urls: list[str] | None = Field(
        default=None,
        description="List of urls where the entity was found",
    )


class EntityInfobox(AbstractGraphInfobox):
    """Aggregated information on an entity from a knowledge graph."""

    subtype: Literal["entity"] = Field(description=DESC_INFOBOX_SUBTYPE)


class QAInfobox(AbstractGraphInfobox):
    """A question answer infobox."""

    subtype: Literal["code"] = Field(description=DESC_INFOBOX_SUBTYPE)
    data: QAPage = Field(description="The question and relevant answer")
    meta_url: MetaUrl | None = Field(
        default=None,
        description="Detailed information on the page containing the QA",
    )


class InfoboxWithLocation(AbstractGraphInfobox):
    """An infobox with location."""

    subtype: Literal["location"] = Field(description=DESC_INFOBOX_SUBTYPE)
    is_location: bool = Field(description="Whether the entity a location")
    coordinates: list[float] | None = Field(
        default=None,
        description="The coordinates of the location",
    )
    zoom_level: int = Field(description="The map zoom level")
    location: LocationResult | None = Field(
        default=None,
        description="The location result",
    )


class InfoboxPlace(AbstractGraphInfobox):
    """An infobox for a place, such as a business."""

    subtype: Literal["place"] = Field(description=DESC_INFOBOX_SUBTYPE)
    location: LocationResult = Field(description="The location result")


class GraphInfobox(BaseModel):
    """Aggregated information on an entity shown as an infobox."""

    type: Literal["graph"] = Field(description=f"{DESC_TYPE_IDENTIFIER} infoboxes")
    results: GenericInfobox | QAInfobox | InfoboxPlace | InfoboxWithLocation | EntityInfobox = Field(
        description="A list of infoboxes associated with the query"
    )


class Summarizer(BaseModel):
    """Details on getting the summary."""

    type: Literal["summarizer"] = Field(description="The value is always summarizer")
    key: str = Field(description="The key for the summarizer API")


class WebSearchApiResponse(BaseModel):
    """Top level response model for successful Web Search API requests."""

    type: Literal["search"] = Field(description="The type of web search API result")
    discussions: Discussions | None = Field(
        default=None,
        description="Discussions clusters from forum posts",
    )
    faq: FAQ | None = Field(
        default=None,
        description="Frequently asked questions relevant to the query",
    )
    infobox: GraphInfobox | None = Field(
        default=None,
        description="Aggregated information on an entity as infobox",
    )
    locations: Locations | None = Field(
        default=None,
        description="Places of interest relevant to location queries",
    )
    mixed: MixedResponse | None = Field(
        default=None,
        description="Preferred ranked order of search results",
    )
    news: News | None = Field(
        default=None,
        description="News results relevant to the query",
    )
    query: Query | None = Field(
        default=None,
        description="Search query string and its modifications",
    )
    videos: Videos | None = Field(
        default=None,
        description="Videos relevant to the query",
    )
    web: Search | None = Field(
        default=None,
        description="Web search results relevant to the query",
    )
    summarizer: Summarizer | None = Field(
        default=None,
        description="Summary key to get summary results",
    )


class LocalPoiSearchApiResponse(BaseModel):
    """
    Top level response model for successful Local Search API request.

    Contains location information and related metadata.
    """

    type: Literal["local_pois"] = Field(
        description="The type of local POI search API result",
    )
    results: list[LocationResult] | None = Field(
        default=None,
        description="Location results matching the ids in the request",
    )


class LocalDescriptionsSearchApiResponse(BaseModel):
    """
    Top level response model for successful Local Search API request.

    Contains AI generated location descriptions and related metadata.
    """

    type: Literal["local_descriptions"] = Field(
        description="The type of local description search API result",
    )
    results: list[LocationDescription] | None = Field(
        default=None,
        description="Location descriptions matching the ids",
    )


# Update forward references
Organization.model_rebuild()
Reviews.model_rebuild()
