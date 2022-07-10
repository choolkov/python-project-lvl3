"""Input/Output module."""

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


def write_content(path: Path, file_content: str):
    """
    Write content to file.

    Args:
        path: file path
        file_content: text content
    """
    with open(path, 'w') as file:  # NOQA: WPS110
        file.write(file_content)
