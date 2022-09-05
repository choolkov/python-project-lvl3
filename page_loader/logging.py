"""Logging module."""

import logging
from sys import stderr, stdout
from typing import TextIO


def get_logger(name: str, stream: TextIO) -> logging.Logger:
    """Return logger instance.

    Args:
        name: logger name
        stream: output stream

    Returns:
        logging.Logger
    """
    logger = logging.getLogger(name)
    stream_handler = logging.StreamHandler(stream)
    formatter = logging.Formatter('{levelname}: {message}', style='{')

    stream_handler.setFormatter(formatter)
    logger.addHandler(stream_handler)
    logger.setLevel('DEBUG')
    return logger


logger = get_logger('log', stdout)
errors_logger = get_logger('error', stderr)
