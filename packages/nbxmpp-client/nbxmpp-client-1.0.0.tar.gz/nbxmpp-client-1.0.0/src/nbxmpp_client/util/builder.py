from __future__ import annotations

from typing import cast

import importlib.resources
from pathlib import Path

from gi.repository import Gtk
from nbxmpp import Any


class Builder:
    def __init__(self, filename: str) -> None:
        base_dir = cast(Path, importlib.resources.files("nbxmpp_client"))
        ui_file_path = base_dir / "data" / filename
        self._builder = Gtk.Builder()
        self._builder.add_from_file(str(ui_file_path))

    def __getattr__(self, name: str) -> Any:
        try:
            return getattr(self._builder, name)
        except AttributeError:
            return self._builder.get_object(name)
