import os
from typing import Optional
from urllib.parse import urlparse

import requests


class Downloader:
    def create_path(self, url: str, path: str = "") -> str:
        """
        Create a local path where a page can be downloaded.

        Args:
            url (str): Full URL of a web page to download.
            path (str): Directory where the page will be saved on disk.

        Returns:
            str: Path where the page can be saved on disk.

        Examples:
            >>> dl = Downloader()
            >>> dl.create_path("https://www.criterion.com/shop/browse/list")
            'list'

        """

        filename = os.path.basename(urlparse(url).path)
        path = os.path.join(path, filename)

        return path

    def download_page(self, url: str, path: Optional[str] = None) -> str:
        """
        Download a web page and save to disk

        Args:
            url (str): Full URL of the web page to download.
            path (:obj:`str`, optional): Directory where the page will be saved on disk.

        Returns:
            If `path` is None, the resulting file as a string. Otherwise the path to the
            downloaded file on disk.

        Examples:
            >>> dl = Downloader()
            >>> dl.download_page("https://www.criterion.com/shop/browse/list", "/tmp")
            '/tmp/list'

        """

        resp = requests.get(url)
        resp.raise_for_status()

        if path is None:

            path_or_text = resp.text

        else:

            path_or_text = self.create_path(url, path)

            with open(path_or_text, "w") as file:
                file.write(resp.text)

        return path_or_text
