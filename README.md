# `scrapy-playwright` sample project for Scrapy Cloud

Trying [`scrapy-playwright`](https://github.com/elacuesta/scrapy-playwright) on [Scrapy Cloud](https://scrapinghub.com/scrapy-cloud).


### Dockerfile

A custom Docker image is provided in order to install the system dependencies needed for the headless browsers. This sample project uses Chromium, binaries for the other playwright-supported browsers (Firefox and Webkit) are not downloaded to save time and resources.


### Settings

```python
import inspect
import json
from pathlib import Path

import playwright


TWISTED_REACTOR = "twisted.internet.asyncioreactor.AsyncioSelectorReactor"

DOWNLOAD_HANDLERS = {
    "http": "scrapy_playwright.handler.ScrapyPlaywrightDownloadHandler",
    "https": "scrapy_playwright.handler.ScrapyPlaywrightDownloadHandler",
}

# get path for the bundled chromium binary
browsers_path = Path(inspect.getfile(playwright)).parent / "driver/browsers.json"
chromium = json.loads(browsers_path.read_text())["browsers"][0]
PLAYWRIGHT_BROWSER_TYPE = "chromium"
PLAYWRIGHT_LAUNCH_OPTIONS = {
    "executablePath": f"/ms-playwright/chromium-{chromium['revision']}/chrome-linux/chrome",
    "args": ["--no-sandbox"],
}
```

* `TWISTED_REACTOR`: `scrapy-playwright` will only function with the `asyncio`-based Twisted reactor
* `DOWNLOAD_HANDLERS`: tells Scrapy to use the library's download handler to process requests
* `PLAYWRIGHT_LAUNCH_OPTIONS`: the Docker image will be executed by a non-root user, and hence the path to the browser executable needs to be set explicitly.


### Build and deploy

* Make sure you have [`shub`](https://shub.readthedocs.io/en/stable/index.html) installed
* Replace the project id (`project: <project-id>`) in the `scrapinghub.yml` file with your own project id
* Run `shub image upload`

For more information, check out the [full documentation](https://shub.readthedocs.io/en/stable/deploy-custom-image.html) on how to build and deploy Docker images to Scrapy Cloud.
