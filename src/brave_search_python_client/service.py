"""Service of Brave Search Python Client."""

import os

from dotenv import load_dotenv

load_dotenv()
THE_VAR = os.getenv("THE_VAR", "not defined")


class Service:
    """Service of Brave Search Python Client."""

    def __init__(self) -> None:
        """Initialize service."""

    @staticmethod
    def get_hello_world() -> str:
        """
        Get a hello world message.

        Returns:
            str: Hello world message.
        """
        return f"Hello, world! The value of THE_VAR is {THE_VAR}"
