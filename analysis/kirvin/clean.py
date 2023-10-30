from polars import DataFrame, Utf8, all, col, concat_str, lit, when

from kirvin.columns import Column


def rename(data: DataFrame) -> DataFrame:
    # remove whitespace from column names
    data = data.rename({name: name.strip() for name in data.columns})
    # rename
    data = data.rename(
        # mapping column names of the dataset to our desired column names
        {
            "# STN": Column.station,
            "YYYYMMDD": Column.date,
            "HH": Column.hour,
            "DD": Column.wind_direction,
            "FH": Column.wind_speed,
            "FF": Column.mean_wind_speed_10_min,
            "FX": Column.wind_gust,
            "T": Column.temperature,
            "T10N": Column.min_temperature_6_hours,
            "TD": Column.dew_point_temperature,
            "SQ": Column.sunshine_duration,
            "Q": Column.global_radiation,
            "DR": Column.precipitation_duration,
            "RH": Column.hourly_precipitation,
            "P": Column.air_pressure,
            "VV": Column.horizontal_visibility,
            "N": Column.cloud_coverage,
            "U": Column.relative_atmospheric_humidity,
            "WW": Column.weather_code,
            "IX": Column.weather_indicator,
            "M": Column.fog,
            "R": Column.rainfall,
            "S": Column.snow,
            "O": Column.thunder,
            "Y": Column.ice,
        }
    )
    return data


def clean(data: DataFrame) -> DataFrame:
    data_clean = (
        rename(data)
        # strip spaces from string cols
        .with_columns(
            col(Utf8).str.strip_chars(),
        )
        # empty strings to 0
        .with_columns(
            when(
                col(Utf8) == "",
            )
            .then(None)
            .otherwise(col(Utf8))
            .keep_name(),
        )
        # cast string to int
        .with_columns(all().exclude(Column.station).cast(int))
        # dates
        .with_columns(
            # cast int to date
            col(Column.date).cast(str).str.to_date("%Y%m%d"),
            # create datetime from date_day and hour
            concat_str(
                [
                    # date
                    col(Column.date).cast(str),
                    (
                        # subtract 1 hour
                        (col(Column.hour) - (1))
                        # and pad hour format
                        .cast(str)
                        .str.rjust(2, fill_char="0")
                    ),
                    # minutes
                    lit("00"),
                ]
            )
            .str.to_datetime("%Y%m%d%H%M")
            .alias(Column.date_time),
        )
        .with_columns(
            col(Column.temperature) / 10,
        )
    )
    return data_clean
