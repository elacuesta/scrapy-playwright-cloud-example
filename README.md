# `scrapy-playwright` sample project for Scrapy Cloud

Trying [`scrapy-playwright`](https://github.com/elacuesta/scrapy-playwright) on [Zyte Scrapy Cloud](https://www.zyte.com/scrapy-cloud/).


### Dockerfile

A custom Docker image is provided in order to install the system dependencies needed for the headless browsers.


### Settings

```python
TWISTED_REACTOR = "twisted.internet.asyncioreactor.AsyncioSelectorReactor"

DOWNLOAD_HANDLERS = {
    "http": "scrapy_playwright.handler.ScrapyPlaywrightDownloadHandler",
    "https": "scrapy_playwright.handler.ScrapyPlaywrightDownloadHandler",
}

browsers = {
    "chromium": "/ms-playwright/chromium/chrome-linux/chrome",
    "firefox": "/ms-playwright/firefox/firefox/firefox",
    "webkit": "/ms-playwright/webkit/pw_run.sh",
}
PLAYWRIGHT_BROWSER_TYPE = "webkit"
PLAYWRIGHT_LAUNCH_OPTIONS = {
    "executablePath": browsers[PLAYWRIGHT_BROWSER_TYPE],
    "timeout": 10000,
}
```

* `TWISTED_REACTOR`: `scrapy-playwright` will only function with the `asyncio`-based Twisted reactor
* `DOWNLOAD_HANDLERS`: tells Scrapy to use the library's download handler to process requests
* `PLAYWRIGHT_LAUNCH_OPTIONS`: the Docker image will be executed by a non-root user,
    and hence the path to the browser executable needs to be set explicitly.


### Build and deploy

* Make sure you have [`shub`](https://shub.readthedocs.io/en/stable/index.html) installed
* Replace the project id (`project: <project-id>`) in the `scrapinghub.yml` file with your own project id
* Run `shub image upload`

For more information, check out the [full documentation](https://shub.readthedocs.io/en/stable/deploy-custom-image.html)
on how to build and deploy Docker images to Scrapy Cloud.
