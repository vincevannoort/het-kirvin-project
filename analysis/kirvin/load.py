from polars import DataFrame, read_csv


def load() -> DataFrame:
    data = read_csv(
        source="data/uurgegevens.txt",
        skip_rows=31,
    )
    return data
