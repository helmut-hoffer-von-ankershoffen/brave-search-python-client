"""Custom exceptions for the Brave Search Python Client."""

from __future__ import annotations


class BraveSearchError(Exception):
    """Error when accessing."""


class BraveSearchClientError(BraveSearchError):
    """Error when when interacting with Brave Search Python Client."""


class BraveSearchAPIError(BraveSearchError):
    """Error when accessing Brave Search API."""
