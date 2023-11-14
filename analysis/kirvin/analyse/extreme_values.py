from polars import DataFrame, col

from kirvin.columns import Column


def analyse_min_temperature(data: DataFrame) -> DataFrame:
    return (
        data
        # find rows with min temperature
        .filter(
            col(Column.temperature) == col(Column.temperature).min().over(Column.date),
        )
        # rename so output is clear
        .rename(
            {Column.temperature: Column.temperature.min_column},
        )
    )


def analyse_max_temperature(data: DataFrame) -> DataFrame:
    return (
        data
        # find rows with max temperature
        .filter(
            col(Column.temperature) == col(Column.temperature).max().over(Column.date),
        )
        # rename so output is clear
        .rename(
            {Column.temperature: Column.temperature.max_column},
        )
    )


def analyse_most_sunshine(data: DataFrame) -> DataFrame:
    return (
        data.group_by(
            Column.date,
            Column.station,
        )
        .agg(col(Column.sunshine_duration).sum())
        .sort(Column.date)
        # find rows with most sunshine duration
        .filter(
            col(Column.sunshine_duration) == col(Column.sunshine_duration).max().over(Column.date)
        )
        # rename so output is clear
        .rename(
            {Column.sunshine_duration: Column.sunshine_duration.max_column},
        )
    )


def analyse_most_rain(data: DataFrame) -> DataFrame:
    return (
        data.group_by(
            Column.date,
            Column.station,
        )
        .agg(col(Column.rainfall_amount).sum())
        .sort(Column.date)
        # find rows with most rain
        .filter(col(Column.rainfall_amount) == col(Column.rainfall_amount).max().over(Column.date))
        # rename so output is clear
        .rename(
            {Column.rainfall_amount: Column.sunshine_duration.rainfall_amount.max_column},
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

    return (
        analyse_max_temperature(temperature_data),
        analyse_min_temperature(temperature_data),
        analyse_most_sunshine(data),
        analyse_most_rain(data),
    )
