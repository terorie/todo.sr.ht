import re

# Property with a quoted value, e.g.: label:"help wanted"
TERM_PROPERTY_QUOTED = re.compile(r"(\w+):\"(.+?)\"")

# Property with an unquoted value, e.g.: status:closed
TERM_PROPERTY_UNQUOTED = re.compile(r"(\w+):(\w+)")

# Quoted search string, e.g.: "some thing"
TERM_SEARCH_QUOTED = re.compile(r"\"(.+?)\"")

# Unquoted search string, e.g.: foo
TERM_SEARCH_UNQUOTED = re.compile(r"(\w+)")

TERM_PATTERNS = (
    TERM_PROPERTY_QUOTED,
    TERM_PROPERTY_UNQUOTED,
    TERM_SEARCH_QUOTED,
    TERM_SEARCH_UNQUOTED
)

def _process_term_match(match):
    """Parses a matched search term.

    Returns (prop, value) for properties, and (None, value) for other terms.
    """
    groups = match.groups()
    if len(groups) == 2:
        prop, term = groups
        return prop.strip().lower(), term.strip()

    return None, groups[0].strip()

def find_search_terms(search):
    """Extracts search terms from a search string"""
    for pattern in TERM_PATTERNS:
        m = re.search(pattern, search)
        while m:
            yield _process_term_match(m)
            # Remove matched term from search string
            start, end = m.span()
            search = search[:start] + search[end:]
            m = re.search(pattern, search)
