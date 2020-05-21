"""Top-level package for PySecretary."""
from .pysecretary import (
    get,
    UnsupportedPrefixError,
    InvalidPrefixError,
    PysecretaryError,
    register,
)

__author__ = """Spencer McCreary"""
__email__ = "spencer_mccreary@compulsivesoftware.com"
__version__ = "0.1.0"

__all__ = [
    "get",
    "register",
    "UnsupportedPrefixError",
    "InvalidPrefixError",
    "PysecretaryError",
]
