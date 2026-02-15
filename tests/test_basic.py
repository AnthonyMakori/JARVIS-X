from jarvis import __version__
from jarvis.core import greet


def test_version():
    assert __version__ == "0.1.0"


def test_greet():
    assert greet("World") == "Hello, World!"
