from kirvin.analyse.temperature_per_day import analyse_temperature_per_day
from kirvin.analyse.temperature_per_station import analyse_temperature_per_station
from kirvin.clean import clean
from kirvin.load import load

data_raw = load()
data = clean(data_raw)

# create dataset
temperature_per_day = analyse_temperature_per_day(data)
temperature_per_station = analyse_temperature_per_station(data)
print(temperature_per_day)
print(temperature_per_station)

# save
temperature_per_day.write_json("./data/export/temperature_per_day.json", row_oriented=True)
temperature_per_station.write_json("./data/export/temperature_per_station.json", row_oriented=True)
