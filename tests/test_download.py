"""Test for download function."""
import os
import tempfile

import pytest
from page_loader import download
from tests.fixtures_paths import (
    EXPECTED_FILENAME,
    EXPECTED_PAGE,
    EXPECTED_PATH,
    IMAGE,
    IMAGE2,
    OUTPUT_FOLDER,
    PAGE,
)
from tests.fixtures_urls import IMAGE2_URL, IMAGE_URL, MOCK_URL
from tests.io import get_content


@pytest.fixture
def set_mocks(requests_mock):
    requests_mock.get(MOCK_URL, text=get_content(PAGE))
    requests_mock.get(IMAGE_URL, content=get_content(IMAGE, binary=True))
    requests_mock.get(IMAGE2_URL, content=get_content(IMAGE2, binary=True))

@pytest.fixture
def temp_dir():
    return tempfile.TemporaryDirectory()

@pytest.mark.usefixtures('set_mocks')
def test_download(temp_dir):
    with temp_dir as directory:
        filepath = download(MOCK_URL, directory)
        assert filepath.name == EXPECTED_FILENAME

        filecontent = get_content(filepath)
        assert filecontent == get_content(EXPECTED_PAGE)
