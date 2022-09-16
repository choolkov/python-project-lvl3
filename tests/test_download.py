"""Test for download function."""
import os
import stat
import tempfile
from pathlib import Path

import pytest
from page_loader import download
from requests.exceptions import HTTPError
from tests.fixtures_paths import (
    EXPECTED_FILENAME,
    EXPECTED_PAGE,
    EXPECTED_RESOURCES_DIR_NAME,
    IMAGE,
    PAGE,
    SCRIPT,
    STYLE,
)
from tests.fixtures_urls import (
    IMAGE1_URL,
    IMAGE2_URL,
    IMAGE3_URL,
    MOCK_400,
    MOCK_500,
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
    requests_mock.get(MOCK_400, status_code=400, reason='Bad Request')
    requests_mock.get(MOCK_500, status_code=500, reason='Server Error')


@pytest.fixture
def temp_dir():
    with tempfile.TemporaryDirectory() as directory:
        yield directory


@pytest.fixture
def expected_resources():
    return {
        'test-com-assets-menu.css': STYLE,
        'test-com-assets-application.css': STYLE,
        'test-com-python.png': IMAGE,
        'test-com-ruby.png': IMAGE,
        'test-com-assets-script.js': SCRIPT,
        'test-com-assets-run.js': SCRIPT,
    }


@pytest.mark.usefixtures('set_mocks')
def test_success_download(temp_dir, expected_resources):
    filepath = Path(download(MOCK_URL, temp_dir))
    assert filepath.name == EXPECTED_FILENAME

    filecontent = get_content(filepath)
    assert filecontent == get_content(EXPECTED_PAGE)

    resources_dir = filepath.parent / EXPECTED_RESOURCES_DIR_NAME
    assert resources_dir.exists()

    resources_list = os.listdir(resources_dir)
    assert len(resources_list) == len(expected_resources)

    for resource_filename, (expected_filename, path) in zip(
        sorted(resources_list), sorted(expected_resources.items()),
    ):
        assert resource_filename == expected_filename
        assert get_content(
            resources_dir / resource_filename, binary=True,
        ) == get_content(path, binary=True)


@pytest.mark.parametrize(
    ('url', 'code', 'reason'),
    [
        (MOCK_400, 400, 'Bad Request'),
        (MOCK_500, 500, 'Server Error'),
    ],
)
@pytest.mark.usefixtures('set_fail_mocks')
def test_fail_download(url, code, reason):
    try:
        download(url)
    except HTTPError as error:
        assert error.response.status_code == code
        assert error.response.reason == reason


@pytest.mark.usefixtures('set_mocks')
def test_download_directory_permission(temp_dir):
    os.chmod(temp_dir, stat.S_IRUSR)
    try:
        download(MOCK_URL, temp_dir)
    except PermissionError as error:
        assert error.strerror == 'Permission denied'


@pytest.mark.usefixtures('set_mocks')
def test_download_directory_not_exist(temp_dir):
    os.rmdir(temp_dir)
    try:
        download(MOCK_URL, temp_dir)
    except FileNotFoundError as error:
        assert error.strerror == 'No such file or directory'
