"""Test for download function."""
import os

import pook
import pytest
from page_loader import download
from tests.fixtures_paths import (
    EXPECTED_PATH1,
    EXPECTED_PATH2,
    OUTPUT_FOLDER,
    PAGE,
    IMAGE,
)
from tests.fixtures_urls import IMAGE_URL, MOCK_URL1, MOCK_URL2
from tests.io import get_content


@pytest.fixture(autouse=True)
def clean_files():
    """Clean output files before test."""
    if os.path.isfile(EXPECTED_PATH1):
        os.remove(EXPECTED_PATH1)
    if os.path.isfile(EXPECTED_PATH2):
        os.remove(EXPECTED_PATH2)


@pytest.mark.parametrize(
    'mock_url,output_folder,expected_path,content',
    [
        (MOCK_URL1, OUTPUT_FOLDER, EXPECTED_PATH1, get_content(PAGE)),
        (MOCK_URL2, OUTPUT_FOLDER, EXPECTED_PATH2, get_content(PAGE)),
    ],
)
@pook.on
def test_download(mock_url, output_folder, expected_path, content):
    """
    Test for download function.

    Args:
        mock_url: mocked url
        output_folder: output folder path
        expected_path: expected path
        html_body: html body
    """
    pook.get(mock_url, response_body=get_content(IMAGE, bytes_=True))
    pook.get(IMAGE_URL, content=get_content(IMAGE, bytes_=True))

    filepath = download(mock_url, output_folder)
    assert filepath == expected_path

    filecontent = get_content(expected_path)
    assert filecontent == content
