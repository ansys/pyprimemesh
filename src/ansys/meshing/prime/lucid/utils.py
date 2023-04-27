"""Util functions for lucid modules."""
import re


def match_pattern(pattern: str, name: str) -> bool:
    """Pattern matching function for strings.

    Parameters
    ----------
    pattern : str
        Pattern you are looking for in the string.
    name : str
        String where you look for patterns.

    Returns
    -------
    bool
        True if the pattern is found.
    """
    pattern = "^" + pattern.replace("*", ".*").replace("?", ".") + "$"
    x = re.search(pattern, name)
    if x:
        return True
    else:
        return False


def check_name_pattern(name_patterns: str, name: str) -> bool:
    """Check several patterns in one string.

    Parameters
    ----------
    name_patterns : str
        Patterns to check, separated by commas.
        If pattern starts with !, it shouldn't be found.
    name : str
        String where you look for patterns.

    Returns
    -------
    bool
        True if all found.
    """
    patterns = []
    include_pattern = []
    exclude_pattern = []
    a = name_patterns.split(",")
    for aa in a:
        if len(aa) > 0:
            b = aa.split(" ")
            for bb in b:
                if len(bb) > 0:
                    patterns.append(bb)
    for pattern in patterns:
        pattern = pattern.strip()
        if pattern.startswith("!"):
            exclude_pattern.append(pattern[1:])
        else:
            include_pattern.append(pattern)

    for pattern in exclude_pattern:
        if match_pattern(pattern, name):
            return False

    for pattern in include_pattern:
        if match_pattern(pattern, name):
            return True

    return False
