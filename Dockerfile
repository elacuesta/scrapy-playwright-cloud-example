FROM mcr.microsoft.com/playwright:focal

WORKDIR /app

# Install Python
RUN apt-get update \
    && apt-get install -y python3.9-dev python3-pip nano \
    && python3.9 -m pip install --no-cache-dir --upgrade pip \
    && python3.9 -m pip install --no-cache-dir playwright

COPY requirements.txt /app/requirements.txt
RUN rm -rf /ms-playwright/* \
    && python3.9 -m playwright install chromium \
    && chmod -Rf 777 /ms-playwright \
    && mv /ms-playwright/chromium-* /ms-playwright/chromium \
    # && mv /ms-playwright/firefox-* /ms-playwright/firefox \
    # && mv /ms-playwright/webkit-* /ms-playwright/webkit \
    && pip install --no-cache-dir -r requirements.txt

COPY . /app
ENV SCRAPY_SETTINGS_MODULE scrapy_playwright_cloud_example.settings
RUN python3.9 setup.py install
