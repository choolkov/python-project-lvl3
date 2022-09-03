"""Loader module."""
import os
from pathlib import Path

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

DEFAULT_PATH = os.getcwd()


def download(url: str, path=DEFAULT_PATH) -> str:
    """
    Download the html page and save it to the output path.

    Args:
        url: URL
        path: path to directory

    Returns:
        str: the path to the saved file
    """
    resonce = requests.get(url)

    html_name = get_html_name(url)
    files_path = Path(path, get_directory_name(url))
    make_dir(files_path)

    soup = BeautifulSoup(resonce.text, 'html.parser')
    image_tags = soup.find_all('img')
    for tag in image_tags:
        # TODO is same domain
        url = tag['src']
        filename = get_name(url, get_extension(url))
        img_content = download_content(url, text=False)
        file_path = Path(files_path, filename)
        write_content(file_path, img_content, bytes_=True)
        tag['src'] = file_path
    html_path = Path(path, html_name)
    write_content(html_path, soup.prettify())

    return html_path
