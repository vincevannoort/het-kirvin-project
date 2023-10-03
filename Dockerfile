FROM python:3.11.5-slim

# install poetry
RUN apt-get -y update; apt-get -y install curl unzip
RUN curl -sSL https://install.python-poetry.org | python3 -
ENV PATH="${PATH}:/root/.local/bin:$PATH"

# copy lock and project files
ENV PYTHONPATH /code
WORKDIR /code
COPY poetry.lock pyproject.toml /code/

# install project dependencies
RUN poetry config virtualenvs.create false
RUN poetry install --no-interaction --no-ansi

# download data
RUN curl -LO  https://cdn.knmi.nl/knmi/map/page/klimatologie/gegevens/uurgegevens/jaar.zip --output jaar.zip
# create data folder
RUN mkdir -p data
# unzip to data folder
RUN unzip jaar.zip -d data

# copy the rest of the files
COPY main.py /code/main.py
COPY kirvin /code/kirvin

# run python
RUN poetry run python main.py