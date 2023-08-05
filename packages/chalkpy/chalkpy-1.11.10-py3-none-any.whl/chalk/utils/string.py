import re


def to_snake_case(name: str):
    name = re.sub("(.)([A-Z][a-z]+)", r"\1_\2", name)
    name = re.sub("__([A-Z])", r"_\1", name)
    name = re.sub("([a-z0-9])([A-Z])", r"\1_\2", name)
    return name.lower()


def removeprefix(text: str, prefix: str):
    """
    This functionality is available in Python 3.9 as text.removeprefix(prefix),
    but we're supporting down to 3.8, where it is not available.
    """
    return text[len(prefix) :] if text.startswith(prefix) else text


def comma_whitespace_split(value: str):
    return re.split(r"\s*,\s*", value)


def normalize_string_for_matching(name: str) -> str:
    """
    1. Case insensitive
    2. Strip non-alphanumeric, so e.g. `first_name` matches `firstname`
    """
    return re.sub("[^0-9a-z]", "", name.lower())
