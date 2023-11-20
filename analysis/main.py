from pathlib import Path

from kirvin.analyse.extreme_values import analyse_extreme_values
from kirvin.analyse.rain_per_day import analyse_rain_per_day
from kirvin.analyse.sunshine_per_day import analyse_sunshine_per_day
from kirvin.analyse.temperature_per_day import analyse_temperature_per_day
from kirvin.analyse.temperature_per_station import analyse_temperature_per_station
from kirvin.clean import clean
from kirvin.load import load


def running_in_docker() -> bool:
    cgroup = Path("/proc/self/cgroup")
    return Path("/.dockerenv").is_file() or cgroup.is_file() and "docker" in cgroup.read_text()


# load and clean data
data_raw = load()
data = clean(data_raw)

# analyse and create datasets
temperature_per_day = analyse_temperature_per_day(data)
temperature_per_station = analyse_temperature_per_station(data)
sunshine_per_day = analyse_sunshine_per_day(data)
rain_per_day = analyse_rain_per_day(data)
max_temperature, min_temperature, most_sunshine, most_rainfall = analyse_extreme_values(data)

# save datasets
for _file_name, dataset in [
    ("temperature_per_day", temperature_per_day),
    ("temperature_per_station", temperature_per_station),
    ("sunshine_per_day", sunshine_per_day),
    ("rain_per_day", rain_per_day),
    ("max_temperature", max_temperature),
    ("min_temperature", min_temperature),
    ("most_sunshine", most_sunshine),
    ("most_rainfall", most_rainfall),
]:
    print(dataset)
    # copy to export folder
    dataset.write_json(
        f"./data/export/{_file_name}.json",
        row_oriented=True,
    )
    if not running_in_docker():
        # also copy to dashboard folder
        dataset.write_json(
            f"../dashboard/data/{_file_name}.json",
            row_oriented=True,
        )
