from polars import DataFrame, col

from kirvin.columns import Column


def analyse_rain_per_day(data: DataFrame) -> DataFrame:
    tab = (
        data
        # take average per day over all stations
        .group_by(
            Column.date,
            maintain_order=True,
        )
        .agg(
            col(Column.rainfall_amount).mean().round(2),
        )
        # date to timestamp (highcharts) and calculate rolling mean
        .with_columns(
            col(Column.date).dt.timestamp("ms"),
            rollmean=col(Column.rainfall_amount).rolling_mean(window_size=7, center=True).round(2),
        )
    )
    return tab
