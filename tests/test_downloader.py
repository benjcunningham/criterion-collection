import tempfile

import pytest

from criterion.scraping import Downloader


TEMP_DIR = tempfile.gettempdir()


def test_data_dir_defaults_to_cwd() -> None:

    dl = Downloader()

    assert dl.data_dir == "."


@pytest.mark.parametrize(
    "url,data_dir,expected",
    [
        ("https://www.criterion.com/shop/browse/list", None, "./list"),
        ("https://www.criterion.com/shop/browse/list", TEMP_DIR, f"{TEMP_DIR}/list"),
        (
            "https://www.criterion.com/shop/browse/list?sort=spine_number",
            None,
            "./list",
        ),
    ],
)
def test_create_path_from_url(url: str, data_dir: str, expected: str) -> None:

    assert Downloader().create_path(url, data_dir) == expected
    assert Downloader(data_dir).create_path(url) == expected
