# Description
Analysis of the [KNMI hourly dataset](https://www.knmi.nl/nederland-nu/klimatologie/uurgegevens) of weather in the Netherlands.

## Download data file
```
poetry run python kirvin/download.py
```

## Run automatically on file changes
```
npx nodemon --ignore data --exec poetry run python main.py
```