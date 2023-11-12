from enum import StrEnum, auto


class Column(StrEnum):
    """
    Column names for our dataset.
    """

    # station
    station = auto()

    # date (YYYY=year,MM=month,DD=day)
    date = auto()

    # date time (YYYY=year,MM=month,DD=day,HH=hour,MM=minute)
    date_time = auto()

    # time (HH uur/hour, UT. 12 UT=13 MET, 14 MEZT. Hourly division 05 runs from 04.00 UT to 5.00 UT
    hour = auto()

    # Mean wind direction (in degrees) during the 10-minute period preceding the time of observation (360=north, 90=east, 180=south, 270=west, 0=calm 990=variable)
    wind_direction = auto()

    # Hourly mean wind speed (in 0.1 m/s)
    wind_speed = auto()

    # Mean wind speed (in 0.1 m/s) during the 10-minute period preceding the time of observation
    mean_wind_speed_10_min = auto()

    # Maximum wind gust (in 0.1 m/s) during the hourly division
    wind_gust = auto()

    # Temperature (in 0.1 degrees Celsius) at 1.50 m at the time of observation
    temperature = auto()

    # Minimum temperature (in 0.1 degrees Celsius) at 0.1 m inthe preceding 6-hour period
    min_temperature_6_hours = auto()

    # Dew point temperature (in 0.1 degrees Celsius) at 1.50 m at the time of observation
    dew_point_temperature = auto()

    # Sunshine duration (in 0.1 hour) during the hourly division, calculated from global radiation (-1 for <0.05 hour)
    sunshine_duration = auto()

    # Global radiation (in J/cm2) during the hourly division
    global_radiation = auto()

    # Precipitation duration (in 0.1 hour) during the hourly division
    precipitation_duration = auto()

    # Hourly precipitation amount (in 0.1 mm) (-1 for <0.05 mm)
    rainfall_amount = auto()

    # Air pressure (in 0.1 hPa) reduced to mean sea level, at the time of observation
    air_pressure = auto()

    # Horizontal visibility at the time of observation (0=less than 100m, 1=100-200m, 2=200-300m,..., 49=4900-5000m, 50=5-6km, 56=6-7km, 57=7-8km, ..., 79=29-30km, 80=30-35km, 81=35-40km,..., 89=more than 70km)
    horizontal_visibility = auto()

    # Cloud cover (in octants), at the time of observation (9=sky invisible)
    cloud_coverage = auto()

    # Relative atmospheric humidity (in percents) at 1.50 m at the time of observation
    relative_atmospheric_humidity = auto()

    # Present weather code (00-99), description for the hourly division.
    weather_code = auto()

    # Indicator present weather code (1=manned and recorded (using code from visual observations), 2,3=manned and omitted (no significant weather phenomenon to report, not available), 4=automatically recorded (using code from visual observations), 5,6=automatically omitted (no significant weather phenomenon to report, not available), 7=automatically set (using code from automated observations)
    weather_indicator = auto()

    # Fog 0=no occurrence, 1=occurred during the preceding hour and/or at the time of observation
    fog = auto()

    # Rainfall 0=no occurrence, 1=occurred during the preceding hour and/or at the time of observation
    rainfall = auto()

    # Snow 0=no occurrence, 1=occurred during the preceding hour and/or at the time of observation
    snow = auto()

    # Thunder  0=no occurrence, 1=occurred during the preceding hour and/or at the time of observation
    thunder = auto()

    # Ice formation 0=no occurrence, 1=occurred during the preceding hour and/or at the time of observation
    ice = auto()
