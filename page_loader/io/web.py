"""Web input/output module."""

from typing import Union

import requests
from page_loader.logging import errors_logger
from requests.exceptions import HTTPError


def download_content(url: str, binary: bool = False) -> Union[str, bytes]:
    """
    Download content and return it.

    Args:
        url: URL
        binary: bytes content or text otherwise

    Returns:
        Union[str, bytes]: text or bytes content

    Raises:
        HTTPError: if the response has an invalid status code
    """
    responce = requests.get(url)
    try:
        responce.raise_for_status()
    except HTTPError as error:
        errors_logger.error(
            'HTTP error, url: {0}, status code: {1}, reason: {2}'.format(
                url,
                error.response.status_code,
                error.response.reason,
            ),
        )
        raise
    return responce.content if binary else responce.text
