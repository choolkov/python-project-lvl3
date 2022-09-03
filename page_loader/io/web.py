"""Web input/output module."""

from typing import Union

import requests


def download_content(url: str, bytes_: bool = False) -> Union[str, bytes]:
    """
    Download content and return it.

    Args:
        url: URL
        bytes_: bytes content or text otherwise

    Returns:
        Union[str, bytes]: text or bytes content
    """
    responce = requests.get(url)
    return responce.content if bytes_ else responce.text
