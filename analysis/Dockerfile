FROM python:3.11.5-slim

# create data volume
VOLUME /code/data/export

# install poetry
RUN apt-get -y update; apt-get -y install curl
RUN curl -sSL https://install.python-poetry.org | python3 -
ENV PATH="${PATH}:/root/.local/bin:$PATH"

# copy lock and project files
ENV PYTHONPATH /code
WORKDIR /code
COPY poetry.lock pyproject.toml /code/

# install project dependencies
RUN poetry config virtualenvs.create false
RUN poetry install --no-interaction --no-ansi

# copy the rest of the files
COPY main.py /code/main.py
COPY kirvin /code/kirvin