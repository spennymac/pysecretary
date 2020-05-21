class PysecretaryError(Exception):
    pass


class UnsupportedPrefixError(PysecretaryError):
    """
    A value contains a prefix that is not supported
    """


class InvalidPrefixError(PysecretaryError):
    """
    A value does not have a valid prefix
    """
