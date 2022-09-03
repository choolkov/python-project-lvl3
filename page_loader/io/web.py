"""Web input/output module."""

from typing import Union

import requests


def download_content(url: str, text=True) -> Union[str, bytes]:
    """
    Download content and return it.

    Args:
        url: URL
        text: text content or bytes otherwise

    Returns:
        Union[str, bytes]: text or bytes content
    """
    responce = requests.get(url)
    return responce.text if text else responce.content
