"""Loader module."""
import os
from pathlib import Path
from urllib.parse import urlparse

import requests
from page_loader.io import write_content

DEFAULT_PATH = os.getcwd()


def normalize(string: str) -> str:
    """
    Return a string with non-alphabetic and non-numeric characters replaced.

    Args:
        string: string

    Returns:
        str
    """
    return ''.join(char if char.isalnum() else '-' for char in string)


def remove_extension(path: str) -> str:
    """
    Return the URL path without extension, if any.

    Args:
        path: URL path

    Returns:
        str
    """
    extensions = [
        '.htm',
        '.html',
        '.shtml',
        '.asp',
        '.aspx',
        '.cgi',
        '.jsp',
        '.php',
    ]
    for extension in extensions:
        if path.endswith(extension):
            return path.replace(extension, '')
    return path


def get_html_name(url: str) -> str:
    """
    Return filename builded from URL.

    Args:
        url: URL

    Returns:
        str
    """
    parse_result = urlparse(url)
    name = ''.join(
        map(
            normalize,
            (
                parse_result.netloc,
                remove_extension(parse_result.path),
                '-' if parse_result.query else '',
                parse_result.query if parse_result.query else '',
                '-' if parse_result.fragment else '',
                parse_result.fragment if parse_result.fragment else '',
            ),
        ),
    )
    return '{0}.html'.format(name)


def download(url: str, path=DEFAULT_PATH) -> str:
    """
    Download the html page and save it to the output path.

    Args:
        url: URL
        path: path to directory

    Returns:
        str: the path to the saved file
    """
    resonce = requests.get(url)
    html_name = get_html_name(url)
    html_path = Path(path, html_name)
    write_content(html_path, resonce.text)
    return html_path
