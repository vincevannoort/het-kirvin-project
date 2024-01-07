from polars import DataFrame, col, struct

from kirvin.columns import Column


def analyse_temperature_per_station(data: DataFrame) -> DataFrame:
    return (
        data
        # remove all rows without a temperature
        .drop_nulls(Column.temperature)
        .with_columns(
            col(Column.station),
            # round temperature
            col(Column.temperature).round(1),
            # convert date to timestamp
            col(Column.date).dt.timestamp("ms"),
        )
        # create row per station
        .groupby(
            Column.station,
            maintain_order=True,
        )
        .agg(
            data=(
                struct(
                    [
                        # x value
                        col(Column.date),
                        # y value
                        Column.temperature,
                    ]
                )
            )
        )
    )
