from gi.repository import Gtk

from .client import TestClient


def run() -> None:
    win = TestClient()
    win.connect("delete-event", Gtk.main_quit)
    win.show_all()
    Gtk.main()
