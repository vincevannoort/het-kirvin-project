from kirvin.clean import clean
from kirvin.load import load

data_raw = load()
data = clean(data_raw)


print(data)
# print(data.group_by("BedrijfstakkenBranchesSBI2008").agg(pl.count()))
# print(data.group_by("KenmerkenBaan").agg(pl.count()))

# df = pl.DataFrame(data_raw)
