"""Filesystem input/output module."""

import os
from pathlib import Path


def load_content(path: Path) -> str:
    """
    Load content from file.

    Args:
        path: file path

    Returns:
        str
    """
    with open(path) as file:  # NOQA: WPS110
        return file.read()


def write_content(path: Path, file_content: str, bytes_=False):
    """
    Write content to file.

    Args:
        path: file path
        file_content: text content
    """
    if bytes_:
        with open(path, 'wb') as file:  # NOQA: WPS110
            file.write(file_content)
    else:
        with open(path, 'w') as file:  # NOQA: WPS110
            file.write(file_content)


def make_dir(path: Path):
    """
    Create directory.

    Args:
        path: directory path
    """
    if not path.is_dir():
        os.mkdir(path)
