"""Filesystem input/output module."""

import os
from pathlib import Path

from page_loader.logging import errors_logger


def write_content(path: Path, file_content: str, binary=False):
    """
    Write content to file.

    Args:
        path: file path
        file_content: file content
        binary: type of content

    Raises:
        PermissionError: if access denied
    """
    mode = 'wb' if binary else 'w'
    try:
        with open(path, mode) as file:  # NOQA: WPS110
            file.write(file_content)
    except PermissionError as pe:
        errors_logger.error(
            'Unable to save file {0} ({1})'.format(path, pe.strerror),
        )
        raise


def make_dir(path: Path):
    """
    Create directory.

    Args:
        path: directory path

    Raises:
        PermissionError: if access denied
    """
    try:
        os.mkdir(path)
    except PermissionError as pe:
        errors_logger.error(
            'Unable to create directory {0} ({1})'.format(path, pe.strerror),
        )
        raise
