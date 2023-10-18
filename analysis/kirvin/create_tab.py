from polars import DataFrame, col


def create_tab(data: DataFrame) -> DataFrame:
    tab = (
        data.with_columns(col("temperature") / 10)
        .group_by("date", maintain_order=True)
        .agg(col("temperature").mean())
    )
    return tab
