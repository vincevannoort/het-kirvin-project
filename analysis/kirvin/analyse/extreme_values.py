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
        data.select(
            col(Column.station),
            col(Column.date),
            col(column),
        )
        # find rows with filter value
        .filter(get_filter_value(extreme))
        # round the column of interest
        .with_columns(col(column).round(1))
        # rename so output is clear
        .rename(
            {column: renamed_column},
        )
    )


def analyse_extreme_values(data: DataFrame) -> tuple[DataFrame, DataFrame, DataFrame, DataFrame]:
    return (
        analyse_extreme_value(data, Column.temperature, "max"),
        analyse_extreme_value(data, Column.temperature, "min"),
        analyse_extreme_value(data, Column.sunshine_duration, "max"),
        analyse_extreme_value(data, Column.rainfall_amount, "max"),
    )
