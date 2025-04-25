"""Static configuration of Brave Search Python Client."""

from pathlib import Path

# Configuration required by oe-python-template
API_VERSIONS: dict[str, str] = {}
MODULES_TO_INSTRUMENT: list[str] = []
NOTEBOOK_FOLDER = Path(__file__).parent.parent.parent / "examples"
NOTEBOOK_APP = Path(__file__).parent.parent.parent / "examples" / "notebook.py"

# Project specific configuration
BASE_URL = "https://api.search.brave.com/res/v1/"
DEFAULT_RETRY_WAIT_TIME = 2
MAX_QUERY_LENGTH = 400
MAX_QUERY_TERMS = 50
MOCK_API_KEY = "MOCK"
MOCK_DATA_PATH = "src/brave_search_python_client/responses/fixtures/"
