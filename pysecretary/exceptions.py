class PysecretaryError(Exception):
    pass


class UnsupportedPrefixError(PysecretaryError):
    """
    A value contains a prefix that is not supported
    """

class NotFoundError(PysecretaryError):
    """
    Could not find value
    """

class InvalidPrefixError(PysecretaryError):
    """
    A value does not have a valid prefix
    """
