from polars import DataFrame, Utf8, all, col, concat_str, lit, when

from kirvin.columns import Column
from kirvin.stations import Station


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
            "RH": Column.rainfall_amount,
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
        # for sun and rain, small measurements (<0.05hour/<0.01mm) are coded as -1, set to 0
        .with_columns(
            when(
                col(Column.rainfall_amount) == -1,
            )
            .then(None)
            .otherwise(col(Column.rainfall_amount))
            .keep_name(),
            when(
                col(Column.sunshine_duration) == -1,
            )
            .then(None)
            .otherwise(col(Column.sunshine_duration))
            .keep_name(),
        )
        # wheather indicators to logical units, for example rainfall to mm (now in 0.1 mm)
        .with_columns(
            col(Column.temperature) / 10,
            col(Column.sunshine_duration) / 10,
            col(Column.rainfall_amount) / 10,
        )
        # replace station integers with station names
        .with_columns(
            col(Column.station).cast(str).map_dict(Station.create_int_string_mapping()),
        )
    )
    return data_clean
