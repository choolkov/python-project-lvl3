"""Test for download function."""
import os
from pathlib import Path
import stat
import tempfile

import pytest
from page_loader import download
from requests.exceptions import HTTPError
from tests.fixtures_paths import (
    EXPECTED_FILENAME,
    EXPECTED_PAGE,
    IMAGE,
    PAGE,
    SCRIPT,
    STYLE,
)
from tests.fixtures_urls import (
    IMAGE1_URL,
    IMAGE2_URL,
    IMAGE3_URL,
    MOCK_URL,
    SCRIPT1_URL,
    SCRIPT2_URL,
    SCRIPT3_URL,
    STYLE1_URL,
    STYLE2_URL,
    STYLE3_URL,
)
from tests.io import get_content


@pytest.fixture
def set_mocks(requests_mock):
    requests_mock.get(MOCK_URL, text=get_content(PAGE))
    requests_mock.get(IMAGE1_URL, content=get_content(IMAGE, binary=True))
    requests_mock.get(IMAGE2_URL, content=get_content(IMAGE, binary=True))
    requests_mock.get(IMAGE3_URL, content=get_content(IMAGE, binary=True))
    requests_mock.get(STYLE1_URL, text=get_content(STYLE))
    requests_mock.get(STYLE2_URL, text=get_content(STYLE))
    requests_mock.get(STYLE3_URL, text=get_content(STYLE))
    requests_mock.get(SCRIPT1_URL, text=get_content(SCRIPT))
    requests_mock.get(SCRIPT2_URL, text=get_content(SCRIPT))
    requests_mock.get(SCRIPT3_URL, text=get_content(SCRIPT))


@pytest.fixture
def set_fail_mocks(requests_mock):
    requests_mock.get(MOCK_URL, status_code=404, reason='Page not found')


@pytest.fixture
def temp_dir():
    return tempfile.TemporaryDirectory()


@pytest.mark.usefixtures('set_mocks')
def test_success_download(temp_dir):
    with temp_dir as directory:
        filepath = download(MOCK_URL, directory)
        assert Path(filepath).name == EXPECTED_FILENAME

        filecontent = get_content(filepath)
        assert filecontent == get_content(EXPECTED_PAGE)


@pytest.mark.usefixtures('set_fail_mocks')
def test_fail_download(temp_dir):
    try:
        download(MOCK_URL)
    except HTTPError as error:
        assert error.response.status_code == 404
        assert error.response.reason == 'Page not found'


@pytest.mark.usefixtures('set_mocks')
def test_permission_download(temp_dir):
    with temp_dir as directory:
        os.chmod(directory, stat.S_IRUSR)
        try:
            download(MOCK_URL, directory)
        except PermissionError as error:
            assert error.strerror == 'Permission denied'
