import tempfile

import pytest

from criterion.scraping import Downloader


TEMP_DIR = tempfile.gettempdir()


@pytest.mark.parametrize(
    "url,path,expected",
    [
        ("https://www.criterion.com/shop/browse/list", "", "list"),
        ("https://www.criterion.com/shop/browse/list", TEMP_DIR, f"{TEMP_DIR}/list"),
        (
            "https://www.criterion.com/shop/browse/list?sort=spine_number",
            "",
            "list",
        ),
    ],
)
def test_create_path_from_url(url: str, path: str, expected: str) -> None:

    assert Downloader().create_path(url, path) == expected


@pytest.mark.parametrize(
    "url,path,expected",
    [
        ("https://www.criterion.com/shop/browse/list", TEMP_DIR, f"{TEMP_DIR}/list"),
    ],
)
def test_download_page_with_path(url: str, path: str, expected: str) -> None:

    assert Downloader().download_page(url, path) == expected


def test_download_page_as_string() -> None:

    url = "https://www.criterion.com/shop/browse/list"
    page_text = Downloader().download_page(url)

    assert "Seven Samurai" in page_text
