class PysecretaryError(Exception):
    pass


class UnsupportedPrefixError(PysecretaryError):
    """
    A value contains a prefix that is not supported
    """


class Error(PysecretaryError):
    """
    A value does not have a valid prefix
    """


class InvalidPrefixError(PysecretaryError):
    """
    A value does not have a valid prefix
    """
