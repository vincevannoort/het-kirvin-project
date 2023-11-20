from typing import Literal

from polars import DataFrame, Expr, col

from kirvin.columns import Column


def analyse_extreme_value(
    data: DataFrame,
    column: Column,
    extreme: Literal["min", "max"],
) -> DataFrame:
    def get_filter_value(extreme: Literal["min", "max"]) -> Expr:
        match extreme:
            case "min":
                return col(column) == col(column).min().over(Column.date)
            case "max":
                return col(column) == col(column).max().over(Column.date)

    renamed_column = column.min_column if extreme == "min" else column.max_column

    return (
        data
        # find rows with filter value
        .filter(get_filter_value(extreme))
        # rename so output is clear
        .rename(
            {column: renamed_column},
        )
    )


def analyse_extreme_values(data: DataFrame) -> tuple[DataFrame, DataFrame, DataFrame, DataFrame]:
    temperature_data = (
        data
        # select required columns
        .select(
            Column.date,
            Column.station,
            Column.temperature,
        )
        # already sort by date
        .sort(Column.date)
    )

    rainfall_data = (
        data.group_by(
            Column.date,
            Column.station,
        )
        .agg(col(Column.rainfall_amount).sum())
        .sort(Column.date)
    )

    sunshine_data = (
        data.group_by(
            Column.date,
            Column.station,
        )
        .agg(col(Column.sunshine_duration).sum())
        .sort(Column.date)
    )

    return (
        analyse_extreme_value(temperature_data, Column.temperature, "max"),
        analyse_extreme_value(temperature_data, Column.temperature, "min"),
        analyse_extreme_value(sunshine_data, Column.sunshine_duration, "max"),
        analyse_extreme_value(rainfall_data, Column.rainfall_amount, "max"),
    )
