"""Paths to fixtures."""
from pathlib import Path

TESTS = Path(__file__).parent

FIXTURES = Path(TESTS, 'fixtures')

PAGE = Path(FIXTURES, 'example.html')
EXPECTED_PAGE = Path(FIXTURES, 'expected_example.html')

IMAGE = Path(FIXTURES, 'python.png')
IMAGE2 = Path(FIXTURES, 'ruby.png')

OUTPUT_FOLDER = Path(TESTS, 'output')
EXPECTED_FILENAME = 'test-com-page.html'

EXPECTED_PATH = Path(OUTPUT_FOLDER, EXPECTED_FILENAME)
