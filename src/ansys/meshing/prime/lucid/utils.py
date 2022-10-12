import re


def match_pattern(pattern: str, name: str) -> bool:
    pattern = "^" + pattern.replace("*", ".*").replace("?", ".") + "$"
    x = re.search(pattern, name)
    if x:
        return True
    else:
        return False


def check_name_pattern(name_patterns: str, name: str) -> bool:
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
