from polars import DataFrame, col, concat_str, lit


def clean(data: DataFrame) -> DataFrame:
    data_clean = (
        # convert temperature format from 245 to 24.5
        data.with_columns(
            (col("T") / 10),
        )
        # strip spaces from KenmerkenBaan
        .with_columns(
            # create date
            col("YYYYMMDD").cast(str).str.to_date("%Y%m%d"),
            # create datetime from date and hour
            concat_str(
                [
                    # date
                    col("YYYYMMDD").cast(str),
                    (
                        # subtract 1 hour
                        (col("HH") - (1))
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
        .with_columns(
            # include average temperate at hour column for each hour
            col("T").mean().over("HH").alias("mean_temp_hour"),
            col("T").mean().over("YYYYMMDD").alias("mean_temp_day"),
        )
    )
    return data_clean
