"""Web input/output module."""

from typing import Union

import requests
from page_loader.logging import logger


def download_content(url: str, binary: bool = False) -> Union[str, bytes]:
    """
    Download content and return it.

    Args:
        url: URL
        binary: bytes content or text otherwise

    Returns:
        Union[str, bytes]: text or bytes content
    """
    logger.info('Downloading content from {0}'.format(url))
    responce = requests.get(url)
    logger.info('Content downloaded successfully.')
    return responce.content if binary else responce.text
