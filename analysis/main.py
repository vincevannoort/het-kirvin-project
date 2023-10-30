from kirvin.clean import clean
from kirvin.create_tab import create_tab
from kirvin.load import load

data_raw = load()
data = clean(data_raw)
print(data)

# create dataset
tab_temp_day = create_tab(data)
print(tab_temp_day)

# save
tab_temp_day.write_json("./data/export/temperature_per_day.json", row_oriented=True)
