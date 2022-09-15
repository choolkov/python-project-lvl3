"""Paths to fixtures."""
from pathlib import Path

TESTS = Path(__file__).parent

FIXTURES = Path(TESTS, 'fixtures')

PAGE = Path(FIXTURES, 'example.html')
EXPECTED_PAGE = Path(FIXTURES, 'expected_example.html')

IMAGE = Path(FIXTURES, 'python.png')
STYLE = Path(FIXTURES, 'style.css')
SCRIPT = Path(FIXTURES, 'script.js')

EXPECTED_FILENAME = 'test-com-page.html'
EXPECTED_RESOURCES_DIR_NAME = 'test-com-page_files'