import re
from typing import Tuple

from pysecretary import InvalidPrefixError

PREFIX_PATTERN = re.compile(r"(^(\w+):\/\/)")
VALID_PREFIX = re.compile(r"^\w+")


def parse(v: str) -> Tuple[str, str]:
    elements = re.split(PREFIX_PATTERN, v, maxsplit=1)
    if len(elements) == 4:
        prefix = elements[2].casefold()
        value = elements[3]

        return prefix, value

    raise InvalidPrefixError(v)
