FROM python:3.10.10-bullseye

WORKDIR /app

# Install Python
RUN apt-get update \
    && apt-get install nano \
    && pip install --no-cache-dir --upgrade pip \
    && pip install --no-cache-dir playwright scrapy-playwright scrapinghub-entrypoint-scrapy \
    && playwright install --with-deps chromium \
    && mv /root/.cache/ms-playwright /ms-playwright \
    && mv /ms-playwright/chromium-* /ms-playwright/chromium \
    # && mv /ms-playwright/firefox-* /ms-playwright/firefox \
    # && mv /ms-playwright/webkit-* /ms-playwright/webkit \
    && chmod -Rf 777 /ms-playwright

COPY . /app
ENV SCRAPY_SETTINGS_MODULE scrapy_playwright_cloud_example.settings
RUN python setup.py install
