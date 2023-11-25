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
        .with_columns(
            col(Column.temperature).rolling_mean(window_size=7, center=True).round(2),
        )
        # convert date to timestamp
        .with_columns(col(Column.date).dt.timestamp("ms"))
    )
    return tab
