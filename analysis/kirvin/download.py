import zipfile
from io import BytesIO

import requests


def download_and_unzip(url: str, extract: dict[str, str]):
    print(f"Downloading: {url}")
    response = requests.get(url)
    zip_file = zipfile.ZipFile(BytesIO(response.content))
    for src, dest in extract.items():
        zip_file.getinfo(src).filename = dest
        zip_file.extract(src)
        print(f"Extracted {src} to {dest}")


if __name__ == "__main__":
    download_and_unzip(
        url="https://cdn.knmi.nl/knmi/map/page/klimatologie/gegevens/uurgegevens/jaar.zip",
        extract={"jaar.txt": "data/uurgegevens.txt"},
    )
    download_and_unzip(
        url="https://cdn.knmi.nl/knmi/map/page/klimatologie/gegevens/daggegevens/jaar.zip",
        extract={"jaar.txt": "data/jaargegevens.txt"},
    )
