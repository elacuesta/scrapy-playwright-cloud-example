# `scrapy-playwright` sample project for Scrapy Cloud

Trying [`scrapy-playwright`](https://github.com/elacuesta/scrapy-playwright) on [Scrapy Cloud](https://scrapinghub.com/scrapy-cloud).


### Dockerfile

A custom Docker image is provided in order to install the system dependencies needed for the headless browsers.
To save time and resources, this sample project does not download all browser binaries (see `script/update_browsers_json.py`).


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

# get path for the bundled browser binary
browsers_path = Path(inspect.getfile(playwright)).parent / "driver/browsers.json"
browsers = {x["name"]: x for x in json.loads(browsers_path.read_text())["browsers"]}
PLAYWRIGHT_BROWSER_TYPE = "chromium"
PLAYWRIGHT_LAUNCH_OPTIONS = {
    "executablePath": f"/ms-playwright/chromium-{browsers['chromium']['revision']}/chrome-linux/chrome",
    # "executablePath": f"/ms-playwright/firefox-{browsers['firefox']['revision']}/firefox/firefox",
    "args": ["--no-sandbox"],
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

Crawlera returns an _Internal server error_ if the API key is set via the `proxy.username` argument in
[`playwright.BrowserType.launch`](https://playwright.dev/python/docs/api/class-browsertype#browser_typelaunchoptions),
but it works correctly if the `Proxy-Authorization` header is explicitly included. However, there seems to be a
problem with the way the upstream implementation handles the `Proxy-Authorization` in Chromium
(https://github.com/microsoft/playwright-python/issues/443).

Proxy support works correctly with Firefox, but I'm having some issues running Firefox in Docker
within Scrapy Cloud, which runs the container as a non-root user. For instance:
```
$ shub image build -v
$ docker run --rm -ti -u 1001 <docker_image_id> bash
```

```
I have no name!@94b2f7a90d84:/app$ python script/test_playwright.py
****************************************************************************************************
chromium
<html><head></head><body><pre style="word-wrap: break-word; white-space: pre-wrap;">{
  "origin": "xxx.xxx.xxx.xxx"
}
</pre></body></html>
****************************************************************************************************
firefox
Traceback (most recent call last):
  File "/usr/local/lib/python3.8/site-packages/playwright/_browser_type.py", line 74, in launch
    return from_channel(await self._channel.send("launch", params))
  File "/usr/local/lib/python3.8/site-packages/playwright/_connection.py", line 36, in send
    return await self.inner_send(method, params, False)
  File "/usr/local/lib/python3.8/site-packages/playwright/_connection.py", line 47, in inner_send
    result = await callback.future
playwright._types.TimeoutError: Timeout 5000ms exceeded.
=========================== logs ===========================
<launching> /ms-playwright/firefox-1221/firefox/firefox -no-remote -headless -profile /tmp/playwright_firefoxdev_profile-W3qziy -juggler-pipe --no-sandbox -silent
<launched> pid=73
[err] *** You are running in headless mode.
[err]
[err] (firefox:73): GLib-GObject-WARNING **: 19:12:33.612: invalid (NULL) pointer instance
[err]
[err] (firefox:73): GLib-GObject-CRITICAL **: 19:12:33.612: g_signal_connect_data: assertion 'G_TYPE_CHECK_INSTANCE (instance)' failed
[err] JavaScript error: resource://gre/modules/XULStore.jsm, line 66: Error: Can't find profile directory.
[err] JavaScript error: resource://gre/modules/XULStore.jsm, line 66: Error: Can't find profile directory.
[err] JavaScript error: resource://gre/modules/XULStore.jsm, line 66: Error: Can't find profile directory.
[err] JavaScript error: resource://gre/modules/XULStore.jsm, line 66: Error: Can't find profile directory.
[err] JavaScript error: resource://gre/modules/XULStore.jsm, line 66: Error: Can't find profile directory.
============================================================
Note: use DEBUG=pw:api environment variable and rerun to capture Playwright logs.

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "script/test_playwright.py", line 32, in <module>
    asyncio.run(main())
  File "/usr/local/lib/python3.8/asyncio/runners.py", line 44, in run
    return loop.run_until_complete(main)
  File "/usr/local/lib/python3.8/asyncio/base_events.py", line 616, in run_until_complete
    return future.result()
  File "script/test_playwright.py", line 20, in main
    browser = await browser_type.launch(
  File "/usr/local/lib/python3.8/site-packages/playwright/async_api.py", line 6755, in launch
    await self._impl_obj.launch(
  File "/usr/local/lib/python3.8/site-packages/playwright/_browser_type.py", line 77, in launch
    raise not_installed_error(f'"{self.name}" browser was not found.')
Exception:
================================================================================
"firefox" browser was not found.
Please complete Playwright installation via running

    "python -m playwright install"

================================================================================
```
