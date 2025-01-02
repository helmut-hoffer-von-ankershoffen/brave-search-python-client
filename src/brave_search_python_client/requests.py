import re
from datetime import datetime
from enum import StrEnum

from pydantic import BaseModel, Field, field_validator

from .constants import MAX_QUERY_LENGTH, MAX_QUERY_TERMS


def _validate_date_range(date_range: str) -> bool:
    """Validate date range format YYYY-MM-DDtoYYYY-MM-DD"""
    pattern = r"^\d{4}-\d{2}-\d{2}to\d{4}-\d{2}-\d{2}$"
    if not re.match(pattern, date_range):
        return False
    try:
        start, end = date_range.split("to")
        datetime.strptime(start, "%Y-%m-%d")
        datetime.strptime(end, "%Y-%m-%d")
        return True
    except ValueError:
        return False


def _validate_freshness(v: str | None) -> str | None:
    """Validate freshness value is either None, a FreshnessType, or valid date range"""
    if v is None:
        return v
    if v in {t.value for t in FreshnessType}:
        return v
    if _validate_date_range(v):
        return v
    raise ValueError(
        "Freshness must be None, one of FreshnessType values "
        f"({[t.value for t in FreshnessType]}), or format YYYY-MM-DDtoYYYY-MM-DD"
    )


def _validate_query(v: str) -> str:
    """Validate search query length and term count"""
    if len(v.split()) > MAX_QUERY_TERMS:
        raise ValueError(f"Query exceeding {MAX_QUERY_TERMS} terms")
    return v


def _validate_result_filter(v: str | None) -> str | None:
    """Validate result filter is either None or comma-separated list of valid WebResultType values"""
    if v is None:
        return v
    filters = [f.strip() for f in v.split(",")]
    valid_types = {t.value for t in WebResultType}
    invalid = [f for f in filters if f not in valid_types]
    if invalid:
        raise ValueError(
            f"Invalid result filter types: {invalid}. Must be one of: {valid_types}"
        )
    return v


class SearchType(StrEnum):
    web = "web"
    images = "images"
    videos = "videos"
    news = "news"


class WebSafeSearchType(
    StrEnum
):  # https://api.search.brave.com/app/documentation/web-search/query#WebSearchAPIQueryParameters
    off = "off"
    moderate = "moderate"
    strict = "strict"


class NewsSafeSearchType(
    StrEnum
):  # https://api.search.brave.com/app/documentation/news-search/query#NewsSearchSearchAPI
    off = "off"
    moderate = "moderate"
    strict = "strict"


class ImagesSafeSearchType(
    StrEnum
):  # https://api.search.brave.com/app/documentation/image-search/query#ImageSearchSearchAPI
    off = "off"
    strict = "strict"


class FreshnessType(
    StrEnum
):  # https://api.search.brave.com/app/documentation/web-search/query#WebSearchAPIQueryParameters
    pd = "pd"
    pw = "pw"
    pm = "pm"
    py = "py"


class UnitsType(
    StrEnum
):  # https://api.search.brave.com/app/documentation/web-search/query#WebSearchAPIQueryParameters
    metric = "metric"
    imperial = "imperial"


class WebResultType(
    StrEnum
):  # https://api.search.brave.com/app/documentation/web-search/query#WebSearchAPIQueryParameters
    discussions = "discussions"
    faq = "faq"
    infobox = "infobox"
    news = "news"
    query = "query"
    summarizer = "summarizer"
    videos = "videos"
    web = "web"
    locations = "locations"


class CountryCode(
    StrEnum
):  # https://api.search.brave.com/app/documentation/web-search/codes#country-codes
    ALL = "ALL"  # All Regions
    AR = "AR"  # Argentina
    AU = "AU"  # Australia
    AT = "AT"  # Austria
    BE = "BE"  # Belgium
    BR = "BR"  # Brazil
    CA = "CA"  # Canada
    CL = "CL"  # Chile
    DK = "DK"  # Denmark
    FI = "FI"  # Finland
    FR = "FR"  # France
    DE = "DE"  # Germany
    HK = "HK"  # Hong Kong
    IN = "IN"  # India
    ID = "ID"  # Indonesia
    IT = "IT"  # Italy
    JP = "JP"  # Japan
    KR = "KR"  # Korea
    MY = "MY"  # Malaysia
    MX = "MX"  # Mexico
    NL = "NL"  # Netherlands
    NZ = "NZ"  # New Zealand
    NO = "NO"  # Norway
    CN = "CN"  # Peoples Republic of China
    PL = "PL"  # Poland
    PT = "PT"  # Portugal
    PH = "PH"  # Republic of the Philippines
    RU = "RU"  # Russia
    SA = "SA"  # Saudi Arabia
    ZA = "ZA"  # South Africa
    ES = "ES"  # Spain
    SE = "SE"  # Sweden
    CH = "CH"  # Switzerland
    TW = "TW"  # Taiwan
    TR = "TR"  # Turkey
    GB = "GB"  # United Kingdom
    US = "US"  # United States


class LanguageCode(
    StrEnum
):  # https://api.search.brave.com/app/documentation/web-search/codes#language-codes
    AR = "ar"  # Arabic
    EU = "eu"  # Basque
    BN = "bn"  # Bengali
    BG = "bg"  # Bulgarian
    CA = "ca"  # Catalan
    ZH_HANS = "zh-hans"  # Chinese Simplified
    ZH_HANT = "zh-hant"  # Chinese Traditional
    HR = "hr"  # Croatian
    CS = "cs"  # Czech
    DA = "da"  # Danish
    NL = "nl"  # Dutch
    EN = "en"  # English
    EN_GB = "en-gb"  # English United Kingdom
    ET = "et"  # Estonian
    FI = "fi"  # Finnish
    FR = "fr"  # French
    GL = "gl"  # Galician
    DE = "de"  # German
    GU = "gu"  # Gujarati
    HE = "he"  # Hebrew
    HI = "hi"  # Hindi
    HU = "hu"  # Hungarian
    IS = "is"  # Icelandic
    IT = "it"  # Italian
    JP = "jp"  # Japanese
    KN = "kn"  # Kannada
    KO = "ko"  # Korean
    LV = "lv"  # Latvian
    LT = "lt"  # Lithuanian
    MS = "ms"  # Malay
    ML = "ml"  # Malayalam
    MR = "mr"  # Marathi
    NB = "nb"  # Norwegian Bokmål
    PL = "pl"  # Polish
    PT_BR = "pt-br"  # Portuguese Brazil
    PT_PT = "pt-pt"  # Portuguese Portugal
    PA = "pa"  # Punjabi
    RO = "ro"  # Romanian
    RU = "ru"  # Russian
    SR = "sr"  # Serbian Cyrylic
    SK = "sk"  # Slovak
    SL = "sl"  # Slovenian
    ES = "es"  # Spanish
    SV = "sv"  # Swedish
    TA = "ta"  # Tamil
    TE = "te"  # Telugu
    TH = "th"  # Thai
    TR = "tr"  # Turkish
    UK = "uk"  # Ukrainian
    VI = "vi"  # Vietnamese


class MarketCode(
    StrEnum
):  # RFC 9110 (https://www.rfc-editor.org/rfc/rfc9110.html#name-accept-language); https://api.search.brave.com/app/documentation/web-search/codes#market-codes
    ES_AR = "es-AR"  # Argentina (Spanish)
    EN_AU = "en-AU"  # Australia (English)
    DE_AT = "de-AT"  # Austria (German)
    NL_BE = "nl-BE"  # Belgium (Dutch)
    FR_BE = "fr-BE"  # Belgium (French)
    PT_BR = "pt-BR"  # Brazil (Portuguese)
    EN_CA = "en-CA"  # Canada (English)
    FR_CA = "fr-CA"  # Canada (French)
    ES_CL = "es-CL"  # Chile (Spanish)
    DA_DK = "da-DK"  # Denmark (Danish)
    FI_FI = "fi-FI"  # Finland (Finnish)
    FR_FR = "fr-FR"  # France (French)
    DE_DE = "de-DE"  # Germany (German)
    ZH_HK = "zh-HK"  # Hong Kong SAR (Traditional Chinese)
    EN_IN = "en-IN"  # India (English)
    EN_ID = "en-ID"  # Indonesia (English)
    IT_IT = "it-IT"  # Italy (Italian)
    JA_JP = "ja-JP"  # Japan (Japanese)
    KO_KR = "ko-KR"  # Korea (Korean)
    EN_MY = "en-MY"  # Malaysia (English)
    ES_MX = "es-MX"  # Mexico (Spanish)
    NL_NL = "nl-NL"  # Netherlands (Dutch)
    EN_NZ = "en-NZ"  # New Zealand (English)
    NO_NO = "no-NO"  # Norway (Norwegian)
    ZH_CN = "zh-CN"  # People's Republic of China (Chinese)
    PL_PL = "pl-PL"  # Poland (Polish)
    EN_PH = "en-PH"  # Republic of the Philippines (English)
    RU_RU = "ru-RU"  # Russia (Russian)
    EN_ZA = "en-ZA"  # South Africa (English)
    ES_ES = "es-ES"  # Spain (Spanish)
    SV_SE = "sv-SE"  # Sweden (Swedish)
    FR_CH = "fr-CH"  # Switzerland (French)
    DE_CH = "de-CH"  # Switzerland (German)
    ZH_TW = "zh-TW"  # Taiwan (Traditional Chinese)
    TR_TR = "tr-TR"  # Turkey (Turkish)
    EN_GB = "en-GB"  # United Kingdom (English)
    EN_US = "en-US"  # United States (English)
    ES_US = "es-US"  # United States (Spanish)


class BaseSearchRequest(BaseModel):
    """A base class for Brave Search API requests.

    This class defines the common parameters used in Brave Search API requests, including
    the search query, country code, search language, and spellcheck settings.
    """

    q: str = Field(
        ...,
        min_length=1,
        max_length=MAX_QUERY_LENGTH,
        description=f"The user’s or assistant's search query terms. Query can not be empty. Maximum of {MAX_QUERY_LENGTH} characters and {MAX_QUERY_TERMS} terms in the query.",
    )
    country: CountryCode | None = Field(
        default=None,
        description='The search query country, where the results come from. The country string is limited to 2 character country codes of supported countries, and "ALL" representing all regions.',
    )
    search_lang: str | None = Field(
        default=None,
        description="The search language preference. The 2 or more character language code for which the search results are provided.",
    )
    spellcheck: bool | None = Field(
        default=None,
        description="Whether to spellcheck the provided query. If the spellchecker is enabled, the modified query is always used for search. The modified query can be found in altered key from the query response model.",
    )

    @field_validator("q")
    def validate_query(cls, v: str) -> str:
        return _validate_query(v)

    def model_post_init(self, *args, **kwargs):
        """Set default values for optional fields if not provided."""
        if self.country is None:
            self.country = CountryCode.ALL
        if self.search_lang is None:
            self.search_lang = LanguageCode.EN
        if self.spellcheck is None:
            self.spellcheck = True


class WebSearchRequest(BaseSearchRequest):
    """This class defines the parameters useable in web search."""

    ui_lang: MarketCode | None = Field(
        default=None,
        min_length=5,
        max_length=5,
        description="User interface language preferred in response.",
    )
    count: int | None = Field(
        default=None,
        le=20,
        gt=0,
        description="The number of search results returned in response. The maximum is 20. The actual number delivered may be less than requested. Combine this parameter with offset to paginate search results.",
    )
    offset: int | None = Field(
        default=None,
        le=9,
        ge=0,
        description="In order to paginate results use this parameter together with count. For example, if your user interface displays 20 search results per page, set count to 20 and offset to 0 to show the first page of results. To get subsequent pages, increment offset by 1 (e.g. 0, 1, 2). The results may overlap across multiple pages.",
    )
    safesearch: WebSafeSearchType | None = Field(
        default=None,
        description="Filters search results for adult content. The following values are supported: off: No filtering is done. moderate: Filters explicit content, like images and videos, but allows adult domains in the search results. strict: Drops all adult content from search results.",
    )
    freshness: str | None = Field(
        default=None,
        description="Filters search results by when they were discovered. Values: pd (24h), pw (7d), pm (31d), py (365d), or YYYY-MM-DDtoYYYY-MM-DD for custom range.",
    )
    text_decorations: bool | None = Field(
        default=None,
        description="Whether display strings (e.g. result snippets) should include decoration markers (e.g. highlighting characters).",
    )
    result_filter: str | None = Field(
        default=None,
        description="A comma delimited string of result types to include in the search response. Available values are: discussions, faq, infobox, news, query, summarizer, videos, web, locations.",
    )
    goggles_id: str | None = Field(
        default=None,
        description="Goggles act as a custom re-ranking on top of Brave’s search index. For more details, refer to the Goggles repository (https://github.com/brave/goggles-quickstart).",
    )
    units: UnitsType | None = Field(
        default=None,
        description="The measurement units. If not provided, units are derived from search country. Possible values are: - metric: The standardized measurement system - imperial: The British Imperial system of units.",
    )
    extra_snippets: bool | None = Field(
        default=None,
        description="A snippet is an excerpt from a page you get as a result of the query, and extra_snippets allow you to get up to 5 additional, alternative excerpts. Only available under Free AI, Base AI, Pro AI, Base Data, Pro Data and Custom plans.",
    )
    summary: bool | None = Field(
        default=None,
        description="This parameter enables summary key generation in web search results. This is required for summarizer to be enabled.",
    )

    def model_post_init(self, *args, **kwargs):
        """Set default values for optional fields if not provided."""
        super().model_post_init(*args, **kwargs)
        if self.ui_lang is None:
            self.ui_lang = MarketCode.EN_US
        if self.count is None:
            self.count = 20
        if self.offset is None:
            self.offset = 0
        if self.safesearch is None:
            self.safesearch = WebSafeSearchType.moderate
        if self.text_decorations is None:
            self.text_decorations = True
        if self.extra_snippets is None:
            self.extra_snippets = False
        if self.summary is None:
            self.summary = False

    @field_validator("result_filter")
    def validate_result_filter(cls, v: str | None) -> str | None:
        return _validate_result_filter(v)

    @field_validator("freshness")
    def validate_freshness(cls, v: str | None) -> str | None:
        return _validate_freshness(v)


class ImagesSearchRequest(BaseSearchRequest):
    """This class defines the parameters useable in image search."""

    count: int | None = Field(
        default=None,
        le=100,
        gt=0,
        description="The number of search results returned in response. The maximum is 100. The actual number delivered may be less than requested. Combine this parameter with offset to paginate search results.",
    )
    safesearch: ImagesSafeSearchType | None = Field(
        default=None,
        description="The following values are supported: off: No filtering is done. strict: Drops all adult content from search results.",
    )

    def model_post_init(self, *args, **kwargs):
        """Set default values for optional fields if not provided."""
        super().model_post_init(*args, **kwargs)
        if self.count is None:
            self.count = 50
        if self.safesearch is None:
            self.safesearch = ImagesSafeSearchType.strict


class VideosSearchRequest(BaseSearchRequest):
    """This class defines the parameters useable in videos search."""

    ui_lang: str | None = Field(
        default=None,
        description="User interface language preferred in response. Usually of the format ‘<language_code>-<country_code>’.",
    )
    count: int | None = Field(
        default=None,
        le=50,
        gt=0,
        description="The number of search results returned in response. The maximum is 50. The actual number delivered may be less than requested. Combine this parameter with offset to paginate search results.",
    )
    offset: int | None = Field(
        default=None,
        le=9,
        ge=0,
        description="In order to paginate results use this parameter together with count. For example, if your user interface displays 20 search results per page, set count to 20 and offset to 0 to show the first page of results. To get subsequent pages, increment offset by 1 (e.g. 0, 1, 2). The results may overlap across multiple pages.",
    )
    freshness: str | None = Field(
        default=None,
        description="Filters search results by when they were discovered. Values: pd (24h), pw (7d), pm (31d), py (365d), or YYYY-MM-DDtoYYYY-MM-DD for custom range.",
    )

    def model_post_init(self, *args, **kwargs):
        """Set default values for optional fields if not provided."""
        super().model_post_init(*args, **kwargs)
        if self.ui_lang is None:
            self.ui_lang = MarketCode.EN_US
        if self.count is None:
            self.count = 20
        if self.offset is None:
            self.offset = 0

    @field_validator("freshness")
    def validate_freshness(cls, v: str | None) -> str | None:
        return _validate_freshness(v)


class NewsSearchRequest(BaseSearchRequest):
    """This class defines the parameters useable in news search."""

    ui_lang: MarketCode | None = Field(
        default=None,
        description="User interface language preferred in response. Usually of the format ‘<language_code>-<country_code>’.",
    )
    count: int | None = Field(
        default=None,
        le=50,
        gt=0,
        description="The number of search results returned in response. The maximum is 50. The actual number delivered may be less than requested. Combine this parameter with offset to paginate search results.",
    )
    offset: int | None = Field(
        default=None,
        le=9,
        ge=0,
        description="In order to paginate results use this parameter together with count. For example, if your user interface displays 20 search results per page, set count to 20 and offset to 0 to show the first page of results. To get subsequent pages, increment offset by 1 (e.g. 0, 1, 2). The results may overlap across multiple pages.",
    )
    safesearch: NewsSafeSearchType | None = Field(
        default=None,
        description="Filters search results for adult content. The following values are supported: off: No filtering is done. moderate: Filters explicit content, like images and videos, but allows adult domains in the search results. strict: Drops all adult content from search results.",
    )
    freshness: str | None = Field(
        default=None,
        description="Filters search results by when they were discovered. Values: pd (24h), pw (7d), pm (31d), py (365d), or YYYY-MM-DDtoYYYY-MM-DD for custom range.",
    )
    extra_snippets: bool | None = Field(
        default=None,
        description="A snippet is an excerpt from a page you get as a result of the query, and extra_snippets allow you to get up to 5 additional, alternative excerpts. Only available under Free AI, Base AI, Pro AI, Base Data, Pro Data and Custom plans.",
    )

    def model_post_init(self, *args, **kwargs):
        """Set default values for optional fields if not provided."""
        super().model_post_init(*args, **kwargs)
        if self.ui_lang is None:
            self.ui_lang = MarketCode.EN_US
        if self.count is None:
            self.count = 20
        if self.offset is None:
            self.offset = 0
        if self.safesearch is None:
            self.safesearch = NewsSafeSearchType.strict
        if self.extra_snippets is None:
            self.extra_snippets = False

    @field_validator("freshness")
    def validate_freshness(cls, v: str | None) -> str | None:
        return _validate_freshness(v)
