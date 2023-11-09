from polars import DataFrame, col

from kirvin.columns import Column


def analyse_sunshine_per_day(data: DataFrame) -> DataFrame:
    tab = (
        data
        # sum up amount of sunhine per day per station
        .group_by(
            Column.date,
            Column.station,
            maintain_order=True,
        )
        .agg(
            col(Column.sunshine_duration).sum(),
        )
        # take average over sunshine duration per station
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
            col(Column.sunshine_duration).rolling_mean(window_size=7, center=True),
        )
    )
    return tab
