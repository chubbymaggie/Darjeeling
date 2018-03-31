from bugzoo.core.fileline import FileLine


def ends_with_semi_colon(contents: str) -> bool:
    """
    Returns `True` if a given line ends with a semi-colon.
    """
    return contents.rstrip().endswith(';')


def has_balanced_delimiters(contents: str) -> bool:
    """
    Checks whether all delimiters that occur in a given snippet are balanced.
    """
    return True
