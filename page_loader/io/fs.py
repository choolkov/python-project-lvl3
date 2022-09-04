"""Filesystem input/output module."""

import os
from pathlib import Path


def write_content(path: Path, file_content: str, binary=False):
    """
    Write content to file.

    Args:
        path: file path
        file_content: file content
        binary: type of content
    """
    mode = 'wb' if binary else 'w'
    with open(path, mode) as file:  # NOQA: WPS110
        file.write(file_content)


def make_dir(path: Path):
    """
    Create directory.

    Args:
        path: directory path
    """
    if not path.is_dir():
        os.makedirs(path, exist_ok=True)
