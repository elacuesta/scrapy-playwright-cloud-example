FROM mcr.microsoft.com/playwright:focal

WORKDIR /app
COPY . /app

# Install Python 3.8
RUN apt-get update \
    && apt-get install -y python3.8-dev python3-pip nano \
    && python3.8 -m pip install --no-cache-dir --upgrade pip \
    && python3.8 -m pip install --no-cache-dir playwright

RUN chmod -Rf 777 /ms-playwright \
    && mv /ms-playwright/chromium-* /ms-playwright/chromium \
    && mv /ms-playwright/firefox-* /ms-playwright/firefox \
    && mv /ms-playwright/webkit-* /ms-playwright/webkit \
    && pip install --no-cache-dir -r requirements.txt

ENV SCRAPY_SETTINGS_MODULE scrapy_playwright_cloud_example.settings
RUN python3.8 setup.py install
