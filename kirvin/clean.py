import polars as pl


def clean(data):
    data_clean = (
        pl.DataFrame(data)
        # strip spaces from KenmerkenBaan
        .with_columns(pl.col("KenmerkenBaan").str.strip_chars())
    )
    return data_clean
