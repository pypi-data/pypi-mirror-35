"""
A simple network configuration searcher
"""
from pathlib import Path

version_path = Path(__file__).parent.resolve() / "version"
__version__ = version_path.read_text().strip()

from . import core
from . import parse
