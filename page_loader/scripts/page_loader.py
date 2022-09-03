"""Page loader script."""
import argparse
import pathlib

from page_loader.load import DEFAULT_PATH, download

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


def main():
    """Run download and print full path to downloaded file."""
    print(download(args.url, args.output))


if __name__ == '__main__':
    main()
