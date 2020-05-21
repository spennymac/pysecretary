"""Top-level package for PySecretary."""
from .exceptions import PysecretaryError, UnsupportedPrefixError, InvalidPrefixError
from .pysecretary import (
    get,
    register,
)

__author__ = """Spencer McCreary"""
__email__ = "spencer_mccreary@compulsivesoftware.com"
__version__ = "0.1.4"

__all__ = [
    "get",
    "register",
    "UnsupportedPrefixError",
    "InvalidPrefixError",
    "PysecretaryError",
]
