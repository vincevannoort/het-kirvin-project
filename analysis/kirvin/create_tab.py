from polars import DataFrame, col

from kirvin.columns import Column


def create_tab(data: DataFrame) -> DataFrame:
    tab = (
        data.with_columns(col(Column.temperature) / 10)
        .group_by(Column.date, maintain_order=True)
        .agg(col(Column.temperature).mean())
    )
    return tab
