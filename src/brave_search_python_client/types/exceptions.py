from __future__ import annotations


class BraveSearchError(Exception):
    """Error when accessing ."""


class BraveSearchClientError(BraveSearchError):
    """Error when when interacting with Brave Search Pythoon Client ."""


class BraveSearchAPIError(BraveSearchError):
    """Error when accessing Brave Search API ."""
