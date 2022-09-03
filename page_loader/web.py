"""Web module."""
from urllib.parse import urlparse


def in_same_domain(url1: str, url2: str) -> bool:
    """Check if links are in the same domain.

    Args:
        url1: first URL
        url2: second URL

    Returns:
        bool
    """
    first_domain = urlparse(url1).netloc
    second_domain = urlparse(url2).netloc
    return any(
        (
            not (first_domain and second_domain),
            first_domain == second_domain,
        ),
    )
