"""Web input/output module."""

from typing import Union

import requests


def download_content(url: str, binary: bool = False) -> Union[str, bytes]:
    """
    Download content and return it.

    Args:
        url: URL
        binary: bytes content or text otherwise

    Returns:
        Union[str, bytes]: text or bytes content
    """
    responce = requests.get(url)
    return responce.content if binary else responce.text
