# Specify a base image. This comes from Docker Hub.
FROM python:3.12.2-alpine

# ENV sets environment variables in the Docker container.
# PYTHONUNBUFFERED ensures that Python outputs are sent straight to terminal without being buffered.
ENV PYTHONUNBUFFERED=1

RUN apk update && \
    apk add --no-cache \
    chromium \
    chromium-chromedriver && \
    rm -rf /var/cache/apk/*

WORKDIR /app

COPY . /app

# Copies the requirements.txt from your local directory to the Docker image.
COPY ./requirements.txt /requirements.txt

# Then run pip install to install all dependencies listed in requirements.txt.
RUN pip install -r /requirements.txt

# Specifies the command to run when the Docker container starts.
CMD ["python3", "root.py","--headless"]