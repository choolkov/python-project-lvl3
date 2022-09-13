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
    """
    mode = 'wb' if binary else 'w'
    with open(path, mode) as file:  # NOQA: WPS110
        file.write(file_content)


def make_dir(path: Path):
    """
    Create directory.

    Args:
        path: directory path

    Raises:
        PermissionError: if access denied
        FileNotFoundError: if output directory does not exist
    """
    try:
        os.mkdir(path)
    except PermissionError as error:
        errors_logger.error(
            'Unable to create directory {0} ({1})'.format(path, error.strerror),
        )
        raise
    except FileNotFoundError as error:
        errors_logger.error(
            'Output directory {0} does not exist ({1})'.format(
                path, error.strerror,
            ),
        )
        raise
