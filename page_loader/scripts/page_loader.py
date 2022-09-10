"""Page loader script."""
import argparse
import pathlib
import sys

from page_loader.loader import DEFAULT_PATH, download
from page_loader.logging import errors_logger
from requests.exceptions import RequestException

OK_CODE = 0
REQUESTS_ERROR_CODE = 1
PERMISSION_ERROR_CODE = 2
UNKNOWN_ERROR_CODE = 3

parser = argparse.ArgumentParser(
    description='Loads the HTML page.',
)

parser.add_argument(
    '-o',
    '--output',
    metavar='OUTPUT',
    help='set output path',
    type=pathlib.Path,
    default=DEFAULT_PATH,
)
parser.add_argument('url', help='page URL', type=str)
args = parser.parse_args()


def handle_exception(exception: Exception, message: str, code: int):
    """Exception handler.

    Args:
        exception: raised exception
        message: message for user
        code: exit code
    """
    errors_logger.error(exception)
    print(message)
    sys.exit(code)


def main():
    """Run download and print full path to downloaded file."""
    try:
        print(download(args.url, args.output))

    except RequestException as exception:
        handle_exception(
            exception,
            'Unable to download content from {0}'.format(args.url),
            REQUESTS_ERROR_CODE,
        )

    except PermissionError as exception:
        handle_exception(
            exception,
            'Access denied to output directory {0}'.format(args.output),
            PERMISSION_ERROR_CODE,
        )

    except Exception as exception:
        handle_exception(
            exception,
            'Unknown error',
            UNKNOWN_ERROR_CODE,
        )


if __name__ == '__main__':
    main()
