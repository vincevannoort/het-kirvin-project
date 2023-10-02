from polars import DataFrame, read_csv


def load() -> DataFrame:
    data = read_csv(
        source="../data/jaar.txt",
        skip_rows=31,
    )
    return data
