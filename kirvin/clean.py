from polars import DataFrame, Utf8, all, col, concat_str, lit, when


def rename(data: DataFrame) -> DataFrame:
    # remove whitespace from column names
    data = data.rename({name: name.strip() for name in data.columns})
    # rename
    data = data.rename(
        {
            "# STN": "station",
            "YYYYMMDD": "date_day",
            "HH": "hour",
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
        .with_columns(all().exclude("station").cast(int))
        # dates
        .with_columns(
            # cast int to date
            col("date_day").cast(str).str.to_date("%Y%m%d"),
            # create datetime from date_day and hour
            concat_str(
                [
                    # date
                    col("date_day").cast(str),
                    (
                        # subtract 1 hour
                        (col("hour") - (1))
                        # and pad hour format
                        .cast(str)
                        .str.rjust(2, fill_char="0")
                    ),
                    # minutes
                    lit("00"),
                ]
            )
            .str.to_datetime("%Y%m%d%H%M")
            .alias("datetime"),
        )
    )
    return data_clean

    # # convert temperature format from 245 to 24.5
    # .with_columns(
    #     (col("T") / 10),
    # )
    # .with_columns(
    #     # include average temperate at hour column for each hour
    #     col("T").mean().over("hour").alias("mean_temp_hour"),
    #     col("T").mean().over("date_day").alias("mean_temp_day"),
    # )


# specific cleaning

# enrich
