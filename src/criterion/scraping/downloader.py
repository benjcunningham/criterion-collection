import os
from typing import Optional
from urllib.parse import urlparse

import requests


CRITERION_LIST_URL = "https://www.criterion.com/shop/browse/list"


class Downloader:
    def __init__(self, data_dir: Optional[str] = None):

        self.data_dir = data_dir  # type: ignore

    @property
    def data_dir(self) -> str:
        """
        str: Directory where data will be saved on disk.

        If no path is provided, will default to the current working directory.
        Data directories will be created if they do not already exist.
        """

        return self._data_dir

    @data_dir.setter
    def data_dir(self, value: Optional[str]) -> None:

        data_dir: str = value or "."
        os.makedirs(data_dir, exist_ok=True)

        self._data_dir = data_dir

    def create_path(self, url: str, data_dir: Optional[str] = None) -> str:
        """
        Create a download path from a URL

        Args:
            url (str): Full URL of the web page.
            data_dir (:obj:`str`, optional): Directory where the page should be
                saved. Will use the object-level data_dir property if not
                provided.

        Returns:
            str: Path where the page will be saved on disk.

        Examples:
            >>> dl = Downloader()
            >>> dl.create_path("https://www.criterion.com/shop/browse/list")
            './list'

        """

        data_dir = data_dir or self.data_dir
        filename = os.path.basename(urlparse(url).path)
        path = os.path.join(data_dir, filename)

        return path

    def download_page(self, url: str, data_dir: Optional[str] = None) -> str:
        """
        Download a web page and save to disk

        Args:
            url (str): Full URL of the web page.
            data_dir (:obj:`str`, optional): Directory where the page should be
                saved. Will use the object-level data_dir property if not
                provided.

        Returns:
            str: Path where the page was saved on disk.

        Examples:
            >>> dl = Downloader()
            >>> dl.download_page("https://www.criterion.com/shop/browse/list")
            './list'

        """

        resp = requests.get(url)
        resp.raise_for_status()

        local_path = self.create_path(url, data_dir)

        with open(local_path, "w") as file:
            file.write(resp.text)

        return local_path
