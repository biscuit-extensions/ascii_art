from __future__ import annotations

import typing

from biscuit.extensions import Extension

if typing.TYPE_CHECKING:
    from biscuit.api import ExtensionsAPI


class AsciiArt(Extension):
    """Generate ASCII art text banners and box drawings"""

    def __init__(self, api: "ExtensionsAPI") -> None:
        super().__init__(api)
        self.api = api
        self.api.logger.info("ASCII Art extension initialised.")

    def install(self) -> None:
        """Run when extension is loaded."""
        self.api.logger.info("ASCII Art installed successfully.")
