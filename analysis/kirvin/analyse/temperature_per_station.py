from polars import DataFrame, col, struct

from kirvin.columns import Column


def analyse_temperature_per_station(data: DataFrame) -> DataFrame:
    return (
        data.group_by(
            [
                Column.station,
                Column.date,
            ],
            maintain_order=True,
        )
        .agg(
            col(Column.temperature).mean().round(1),
        )
        # convert date to timestamp
        .with_columns(col(Column.date).dt.timestamp("ms"))
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
