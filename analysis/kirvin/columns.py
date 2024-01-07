from enum import StrEnum, auto


class Column(StrEnum):
    """
    Column names for our dataset.
    """

    # station
    station = auto()

    # date (YYYY=year,MM=month,DD=day)
    date = auto()

    # TG: Daily mean temperature in (0.1 degrees Celsius)
    temperature = auto()

    # SQ: Sunshine duration (in 0.1 hour) calculated from global radiation (-1 for <0.05 hour)
    sunshine_duration = auto()

    # RH: Daily precipitation amount (in 0.1 mm) (-1 for <0.05 mm)
    rainfall_amount = auto()

    @property
    def max_column(self) -> str:
        return f"max_{self}"

    @property
    def min_column(self) -> str:
        return f"min_{self}"
