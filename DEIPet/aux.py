"""General-purpose auxiliary functions"""

from urllib.parse import urlparse


def filter_url_list(
    lst: list[str], fallback: str, ok_schemes: list[str] = ["http", "https", "data"]
) -> list[str]:
    """Filter a list of URLs, ensuring at least one and that all are using an OK scheme."""
    if not lst:
        return [fallback]
    nl = []
    for url in lst:
        scheme = urlparse(url).scheme
        if scheme and scheme in ok_schemes:
            nl += [url]
        else:
            nl += [fallback]
    return nl