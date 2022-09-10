"""Web module."""
from collections import namedtuple
from urllib.parse import urlparse

from bs4 import BeautifulSoup, Tag

TAGS = ('img', 'link', 'script')
tag_attrs = {
    'img': 'src',
    'link': 'href',
    'script': 'src',
}
Asset = namedtuple('Asset', ['tag', 'url_attr', 'url'])


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


def make_asset(tag: Tag) -> Asset:
    """Create asset from BeautifulSoup tag.

    Args:
        tag: BeautifulSoup tag

    returns:
        Asset
    """
    url_attr = tag_attrs[tag.name]
    url = tag[url_attr]
    return Asset(tag, url_attr, url)


def get_assets(html_page: BeautifulSoup) -> list:
    """Return list of assets.

    Args:
        html_page: BeautifulSoup object

    Returns:
        list
    """

    def has_url(tag: Tag):  # NOQA WPS430
        return tag.name in TAGS and tag.has_attr(tag_attrs[tag.name])

    tags = html_page.find_all(has_url)
    return [make_asset(tag) for tag in tags]
