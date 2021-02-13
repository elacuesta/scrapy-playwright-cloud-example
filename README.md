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


### Crawlera support

With Chromium, Crawlera returns an _Internal server error_ if the API key is set via the `proxy.username` argument in
[`playwright.BrowserType.launch`](https://playwright.dev/python/docs/api/class-browsertype#browser_typelaunchoptions),
but it works correctly if the `Proxy-Authorization` header is explicitly included. However, there seems to be a
problem with the way the upstream implementation handles the `Proxy-Authorization` in Chromium
(https://github.com/microsoft/playwright-python/issues/443).

Proxy support works correctly with Firefox, but I wasn't able to run Firefox in Docker
as a non-root user, which is how Scrapy Cloud uses the image.

Because of the above, `webkit` is the recommended browser to be used in Scrapy Cloud if Crawlera support is needed.
```
