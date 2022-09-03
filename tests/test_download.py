"""Test for download function."""
import os

import pytest
from page_loader import download
from tests.fixtures_paths import (
    EXPECTED_PAGE,
    EXPECTED_PATH,
    IMAGE,
    IMAGE2,
    OUTPUT_FOLDER,
    PAGE,
)
from tests.fixtures_urls import IMAGE2_URL, IMAGE_URL, MOCK_URL
from tests.io import get_content


@pytest.fixture(autouse=True)
def clean_files():
    """Clean output files before test."""
    if os.path.isfile(EXPECTED_PATH):
        os.remove(EXPECTED_PATH)


@pytest.fixture
def set_mocks(requests_mock):
    requests_mock.get(MOCK_URL, text=get_content(PAGE))
    requests_mock.get(IMAGE_URL, content=get_content(IMAGE, binary=True))
    requests_mock.get(IMAGE2_URL, content=get_content(IMAGE2, binary=True))


@pytest.mark.usefixtures('set_mocks')
def test_download():
    filepath = download(MOCK_URL, OUTPUT_FOLDER)
    assert filepath == EXPECTED_PATH

    filecontent = get_content(EXPECTED_PATH)
    assert filecontent == get_content(EXPECTED_PAGE)
