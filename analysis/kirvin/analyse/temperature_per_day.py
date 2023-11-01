from polars import DataFrame, col

from kirvin.columns import Column


def analyse_temperature_per_day(data: DataFrame) -> DataFrame:
    tab = (
        data.group_by(
            Column.date,
            maintain_order=True,
        )
        .agg(
            col(Column.temperature).mean().round(1),
        )
        # convert date to timestamp
        .with_columns(col(Column.date).dt.timestamp("ms"))
    )
    return tab
