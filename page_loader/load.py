"""Loader module."""
import os
from pathlib import Path
from urllib.parse import urljoin

import requests
from bs4 import BeautifulSoup
from page_loader.io.fs import make_dir, write_content
from page_loader.io.web import download_content
from page_loader.naming import (
    get_directory_name,
    get_extension,
    get_html_name,
    get_name,
)
from page_loader.web import Asset, get_assets, in_same_domain

DEFAULT_PATH = os.getcwd()


def download(url: str, path=DEFAULT_PATH) -> str:  # NOQA WPS210
    """
    Download the html page and save it to the output path.

    Args:
        url: URL
        path: path to directory

    Returns:
        str: the path to the saved file
    """
    html_name = get_html_name(url)
    files_path = Path(path, get_directory_name(url))
    make_dir(files_path)

    resonce = requests.get(url)
    soup = BeautifulSoup(resonce.text, 'html.parser')
    assets: list[Asset] = get_assets(soup)

    for asset in assets:
        tag = asset.tag
        if in_same_domain(url, asset.url):
            asset_url = urljoin(url, asset.url)
            file_name = get_name(asset_url, get_extension(asset_url))
            file_content = download_content(asset_url, binary=asset.is_binary)
            file_path = Path(files_path, file_name)
            write_content(file_path, file_content, binary=asset.is_binary)
            relative_path = file_path.relative_to(path)
            tag[asset.attr] = relative_path

    html_path = Path(path, html_name)
    write_content(html_path, soup.prettify())
    return html_path
