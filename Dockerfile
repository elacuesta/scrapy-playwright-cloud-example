FROM python:3.11.4-slim-bullseye

WORKDIR /app
COPY . /app

RUN apt-get update \
    && pip install --no-cache-dir --upgrade pip \
    && pip install --no-cache-dir -r requirements.txt \
    && playwright install --with-deps chromium \
    && mv /root/.cache/ms-playwright /ms-playwright \
    && mv /ms-playwright/chromium-* /ms-playwright/chromium \
    # && mv /ms-playwright/firefox-* /ms-playwright/firefox \
    # && mv /ms-playwright/webkit-* /ms-playwright/webkit \
    && chmod -Rf 777 /ms-playwright

ENV SCRAPY_SETTINGS_MODULE scrapy_playwright_cloud_example.settings
RUN python setup.py install
