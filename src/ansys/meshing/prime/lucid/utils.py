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
    a = name_patterns.split(",")
    for aa in a:
        patterns.append(aa)

    for pattern in patterns:
        bb = pattern.split("!")
        if match_pattern(bb[0].strip(), name):
            if len(bb) > 1:
                nv = False
                for nvbb in bb[1:]:
                    if match_pattern(nvbb.strip(), name):
                        nv = True
                        break
                if not nv:
                    return True
            else:
                return True

    return False
