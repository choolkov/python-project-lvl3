"""Test for download function."""
import tempfile

import pytest
from page_loader import download
from tests.fixtures_paths import (
    EXPECTED_FILENAME,
    EXPECTED_PAGE,
    IMAGE,
    PAGE,
    STYLE,
)
from tests.fixtures_urls import (
    IMAGE2_URL,
    IMAGE_URL,
    MOCK_URL,
    STYLE1_URL,
    STYLE2_URL,
    STYLE3_URL,
)
from tests.io import get_content


@pytest.fixture
def set_mocks(requests_mock):
    requests_mock.get(MOCK_URL, text=get_content(PAGE))
    requests_mock.get(IMAGE_URL, content=get_content(IMAGE, binary=True))
    requests_mock.get(IMAGE2_URL, content=get_content(IMAGE, binary=True))
    requests_mock.get(STYLE1_URL, text=get_content(STYLE))
    requests_mock.get(STYLE2_URL, text=get_content(STYLE))
    requests_mock.get(STYLE3_URL, text=get_content(STYLE))


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
