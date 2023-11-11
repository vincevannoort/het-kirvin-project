from polars import DataFrame, col

from kirvin.columns import Column


def analyse_sunshine_per_day(data: DataFrame) -> DataFrame:
    tab = (
        data
        # each row contains the duration of sunshine per hour
        # when we sum up per day, we have the amount of sunhine per day instead of hour
        # 0   ->  0 hours of sunshine in the last hour
        # 0.5 ->  0.5 hours of sunshine in the last hour
        # 1   ->  1 hour of sunshine in the last hour
        .group_by(
            Column.date,
            Column.station,
            maintain_order=True,
        )
        .agg(
            col(Column.sunshine_duration).sum(),
        )
        # take average over sunshine duration per day
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
