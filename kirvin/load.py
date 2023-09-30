from polars import DataFrame, read_csv


def load() -> DataFrame:
    data = read_csv(
        source="../data/jaar-cleaned.txt",
    )
    # remove whitespace from column names
    data = data.rename({name: name.strip() for name in data.columns})
    return data
