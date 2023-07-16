FROM python:3.11.2-slim

# setup environment variable
ENV SERVICE_HOME=/usr/src/application \
    PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PIP_NO_CACHE_DIR=off \
    PIP_DISABLE_PIP_VERSION_CHECK=on \
    PIP_DEFAULT_TIMEOUT=100 \
    MODE=PROD

RUN apt-get update -y &&  \
    apt-get upgrade -y &&  \
    apt-get -y install telnet && \
    rm -rf /var/lib/apt/lists/* && \
    mkdir $SERVICE_HOME

# where your code lives
WORKDIR $SERVICE_HOME

# copy whole project to your docker home directory.
COPY . .

# Install poetry:
RUN pip3 install poetry && \
    poetry config virtualenvs.create false

# run this command to install all dependencies
RUN poetry lock --no-update && \
    poetry install --without dev

EXPOSE 8000

# Run gunicorn
ENTRYPOINT ["gunicorn", "-c", "app/shared/config/gunicorn.py", "app.main:app", "--preload"]
