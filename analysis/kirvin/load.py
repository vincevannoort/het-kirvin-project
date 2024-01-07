from polars import DataFrame, read_csv


def load() -> DataFrame:
    data = read_csv(
        source="data/daily.txt",
        skip_rows=59,
    )
    print(data.head())
    return data
