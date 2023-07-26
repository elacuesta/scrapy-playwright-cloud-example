# `scrapy-playwright` sample project for Scrapy Cloud

Running [`scrapy-playwright`](https://github.com/elacuesta/scrapy-playwright)
on [Zyte Scrapy Cloud](https://www.zyte.com/scrapy-cloud/).


### Dockerfile

A custom Docker image is provided: [Dockerfile](Dockerfile). To keep the
resulting image small, only the `chromium` browser is installed by default.


### Settings

```python
_browsers = {
    "chromium": "/ms-playwright/chromium/chrome-linux/chrome",
    # "firefox": "/ms-playwright/firefox/firefox/firefox",
    # "webkit": "/ms-playwright/webkit/pw_run.sh",
}
PLAYWRIGHT_BROWSER_TYPE = "chromium"
PLAYWRIGHT_LAUNCH_OPTIONS = {
    "executable_path": _browsers[PLAYWRIGHT_BROWSER_TYPE],
    "timeout": 10000,
}
```

* `PLAYWRIGHT_LAUNCH_OPTIONS`: the process within the Docker container will be
    executed by a user different from the one who built the image, the path to
    the browser executable needs to be set explicitly.


### Build and deploy

* Make sure you have [`shub`](https://shub.readthedocs.io/en/stable/index.html) installed
* Replace the project id (`project: <project-id>`) in the `scrapinghub.yml` file with your own project id
* Run `shub image upload`
* Run `shub schedule headers`

For more information, check out the [full documentation](https://shub.readthedocs.io/en/stable/deploy-custom-image.html)
on how to build and deploy Docker images to Scrapy Cloud.
