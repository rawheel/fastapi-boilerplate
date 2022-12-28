FROM python:3.10-slim-bullseye
LABEL Boiler Plate

RUN apt-get update \
    && apt-get -y install libpq-dev gcc curl procps net-tools tini \
    && apt-get -y clean \
    && rm -rf /var/lib/apt/lists/* \
    && pip install gunicorn
    
ENV POETRY_HOME=/tmp/poetry
RUN curl -sSL https://install.python-poetry.org/ | python3 -
ENV PATH=$POETRY_HOME/bin:$PATH
ENV PYTHONFAULTHANDLER=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app
COPY . /app

RUN poetry config virtualenvs.create false \
  && poetry install --only main
  
EXPOSE 8000