"""Naming module."""
from functools import partial
from pathlib import Path
from urllib.parse import urlparse


def normalize(string: str) -> str:
    """
    Return a string with non-alphabetic and non-numeric characters replaced.

    Args:
        string: string

    Returns:
        str
    """
    return ''.join(char if char.isalnum() else '-' for char in string)


def get_extension(url: str) -> str:
    """
    Return the extension from URL, or empty string otherwise.

    Args:
        url: URL

    Returns:
        str
    """
    path = urlparse(url).path
    return Path(path).suffix


def remove_extension(path: str) -> str:
    """
    Return path without extension, if any.

    Args:
        path: path

    Returns:
        str
    """
    return path.replace(Path(path).suffix, '')


def get_name(url: str, postfix: str = '') -> str:
    """
    Return name builded from URL.

    Args:
        url: URL
        postfix: directory postfix or extension

    Returns:
        str
    """
    parse_result = urlparse(url)
    return (
        ''.join(
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
        + postfix
    )


get_html_name = partial(get_name, postfix='.html')
get_directory_name = partial(get_name, postfix='_files')
