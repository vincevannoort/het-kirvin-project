from polars import DataFrame, col

from kirvin.columns import Column


def analyse_sunshine_per_day(data: DataFrame) -> DataFrame:
    tab = (
        data
        # take average over all stations
        .group_by(
            Column.date,
            maintain_order=True,
        )
        .agg(
            col(Column.sunshine_duration).mean(),
        )
        # convert date to timestamp
        .with_columns(
            col(Column.date).dt.timestamp("ms"),
            col(Column.sunshine_duration).rolling_mean(window_size=7, center=True).round(1),
        )
    )
    return tab
