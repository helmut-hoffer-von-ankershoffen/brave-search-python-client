"""Graphical User Interface (GUI) of Brave Search Python Client."""

from brave_search_python_client.utils import gui_run

# For development run via `uv run watch_gui.py`
gui_run(native=False, show=True, watch=True)
