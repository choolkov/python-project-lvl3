"""Test for download function."""
import os
import time

import pook
import pytest
from page_loader import download
from page_loader.io import load_content
from tests.fixtures_paths import EXPECTED_PATH1, EXPECTED_PATH2, OUTPUT_FOLDER
from tests.fixtures_urls import MOCK_URL1, MOCK_URL2


@pytest.fixture(autouse=True)
def clean_files():
    """Clean output files before test."""
    if os.path.isfile(EXPECTED_PATH1):
        os.remove(EXPECTED_PATH1)
    if os.path.isfile(EXPECTED_PATH2):
        os.remove(EXPECTED_PATH2)


@pytest.mark.parametrize(
    'mock_url,output_folder,expected_path,html_body',
    [
        (MOCK_URL1, OUTPUT_FOLDER, EXPECTED_PATH1, '<body>One</body>'),
        (MOCK_URL2, OUTPUT_FOLDER, EXPECTED_PATH2, '<body>Two</body>'),
    ],
)
@pook.on
def test_download(mock_url, output_folder, expected_path, html_body):
    """
    Test for download function.

    Args:
        mock_url: mocked url
        output_folder: output folder path
        expected_path: expected path
        html_body: html body
    """
    pook.get(mock_url, response_body=html_body)

    filepath = download(mock_url, output_folder)
    assert filepath == expected_path

    filecontent = load_content(expected_path)
    assert filecontent == html_body
