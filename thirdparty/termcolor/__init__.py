"""ANSI color formatting for output in terminal."""
from __future__ import annotations

try:
    from termcolor.termcolor import ATTRIBUTES, COLORS, HIGHLIGHTS, RESET, colored, cprint

except:
    from .termcolor import ATTRIBUTES, COLORS, HIGHLIGHTS, RESET, colored, cprint
__all__ = [
    "ATTRIBUTES",
    "COLORS",
    "HIGHLIGHTS",
    "RESET",
    "colored",
    "cprint",
]
