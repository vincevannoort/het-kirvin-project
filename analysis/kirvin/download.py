from datetime import datetime, timedelta

import requests


def download_daily_data(
    url: str = "https://daggegevens.knmi.nl/klimatologie/daggegevens",
    start: str = (datetime.today() - timedelta(days=365)).strftime("%Y%m%d"),
    end: str = datetime.today().strftime("%Y%m%d"),
) -> None:
    # helpful page for understanding how to download data from knmi
    # https://www.knmi.nl/kennis-en-datacentrum/achtergrond/data-ophalen-vanuit-een-script
    print(f"Downloading: {url}, start: {start}, end: {end}")
    response = requests.post(
        url=url,
        data=(
            "&".join(
                [
                    # start and end date
                    f"start={start}",
                    f"end={end}",
                    # we want all statinos
                    "stns=ALL",
                    # varibles we want to know
                    "vars=TG:SQ:RH",
                ]
            )
        ),
    )
    with open("data/daily.txt", "wb") as f:
        f.write(response.content)


if __name__ == "__main__":
    download_daily_data()
