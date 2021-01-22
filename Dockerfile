FROM python:3.8-buster
RUN apt-get update -qq \
    && apt-get install -qy \
        libappindicator1 \
        libasound2 \
        libatk1.0-0 \
        libc6 \
        libcairo2 \
        libcups2 \
        libdbus-1-3 \
        libexpat1 \
        libfontconfig1 \
        libgbm-dev \
        libgcc1 \
        libgconf-2-4 \
        libgdk-pixbuf2.0-0 \
        libglib2.0-0 \
        libgtk-3-0 \
        libnspr4 \
        libnss3 \
        libpango-1.0-0 \
        libpangocairo-1.0-0 \
        libstdc++6 \
        libx11-6 \
        libx11-xcb1 \
        libxcb1 \
        libxcomposite1 \
        libxcursor1 \
        libxdamage1 \
        libxext6 \
        libxfixes3 \
        libxi6 \
        libxrandr2 \
        libxrender1 \
        libxss1 \
        libxtst6 \
        xdg-utils \
        nano \
    && rm -rf /var/lib/apt/lists

WORKDIR /app
COPY . /app

RUN pip install playwright --no-cache-dir \
    && python /app/script/update_browsers_json.py \
    && python -m playwright install \
    && mv /root/.cache/ms-playwright /ms-playwright \
    && chmod -Rf 755 /ms-playwright \
    && pip install --no-cache-dir -r requirements.txt

ENV SCRAPY_SETTINGS_MODULE scrapy_playwright_cloud_example.settings
RUN python setup.py install
