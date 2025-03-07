"""Constants used throughout Brave Search Python Client's codebase ."""

import importlib.metadata
import pathlib

__project_name__ = __name__.split(".")[0]
__project_path__ = str(pathlib.Path(__file__).parent.parent.parent)
__version__ = importlib.metadata.version(__project_name__)

BASE_URL = "https://api.search.brave.com/res/v1/"
MAX_QUERY_LENGTH = 400
MAX_QUERY_TERMS = 50
DEFAULT_RETRY_WAIT_TIME = 2
MOCK_API_KEY = "MOCK"
MOCK_DATA_PATH = "src/brave_search_python_client/responses/fixtures/"
