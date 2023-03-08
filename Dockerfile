FROM python:3.10-slim

RUN apt-get update && \
    apt-get upgrade -y && \
    apt-get install -y --no-install-recommends vim

COPY requirements_deploy.txt requirements.txt

RUN pip install --trusted-host pypi.org --no-cache-dir --upgrade pip && \
    pip install --trusted-host pypi.org --no-cache-dir -r requirements.txt

WORKDIR /app
CMD python run_app.py