"""Paths to fixtures."""
from pathlib import Path

TESTS = Path(__file__).parent

FIXTURES = Path(TESTS, 'fixtures')

HTML_PAGE = Path(FIXTURES, 'page.html')
OUTPUT_FOLDER = Path(FIXTURES, 'output')

EXPECTED_FILENAME1 = 'test-com-page-user-developer-filter-false.html'
EXPECTED_FILENAME2 = 'test-com-page.html'

EXPECTED_PATH1 = Path(OUTPUT_FOLDER, EXPECTED_FILENAME1)
EXPECTED_PATH2 = Path(OUTPUT_FOLDER, EXPECTED_FILENAME2)
