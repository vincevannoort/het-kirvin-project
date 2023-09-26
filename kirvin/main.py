import polars as pl

from kirvin.load import load

data_raw = load()

data = pl.DataFrame(data_raw)

print(
    data.select(
        # text columns
        pl.col("ID"),
        pl.col("KenmerkenBaan"),
        pl.col("Perioden"),
        pl.col("BedrijfstakkenBranchesSBI2008"),
        # convert all other columns to floats
        pl.all()
        .exclude(["ID", "KenmerkenBaan", "Perioden", "BedrijfstakkenBranchesSBI2008"])
        .str.strip_chars()
        .cast(pl.Int32),
    )
)
