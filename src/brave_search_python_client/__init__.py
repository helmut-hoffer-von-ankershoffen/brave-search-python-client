import importlib.metadata
import pathlib

from .client import BraveSearch
from .responses import (
    BraveSearchAPIError,
    BraveSearchClientError,
    BraveSearchError,
    ImageSearchApiResponse,
    NewsSearchApiResponse,
    VideoSearchApiResponse,
    WebSearchApiResponse,
)

__project_name__ = __name__.split(".")[0]
__project_path__ = str(pathlib.Path(__file__).parent.parent.parent)
__version__ = importlib.metadata.version(__project_name__)

__all__ = [
    "__version__",
    "__project_name__",
    "__project_path__",
    "BraveSearch",
    "BraveSearchError",
    "BraveSearchClientError",
    "BraveSearchAPIError",
    "WebSearchApiResponse",
    "ImageSearchApiResponse",
    "NewsSearchApiResponse",
    "VideoSearchApiResponse",
]
