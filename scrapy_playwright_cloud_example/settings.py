BOT_NAME = "scrapy_playwright_cloud_example"

SPIDER_MODULES = ["scrapy_playwright_cloud_example.spiders"]
NEWSPIDER_MODULE = "scrapy_playwright_cloud_example.spiders"

USER_AGENT = "Mozilla/5.0 (X11; Linux x86_64; rv:127.0) Gecko/20100101 Firefox/127.0"

ROBOTSTXT_OBEY = False

FEED_EXPORT_ENCODING = "utf8"
FEED_EXPORT_INDENT = 4

LOG_LEVEL = "INFO"

TELNETCONSOLE_ENABLED = False


# scrapy-playwright
###################

TWISTED_REACTOR = "twisted.internet.asyncioreactor.AsyncioSelectorReactor"

DOWNLOAD_HANDLERS = {
    "http": "scrapy_playwright.handler.ScrapyPlaywrightDownloadHandler",
    "https": "scrapy_playwright.handler.ScrapyPlaywrightDownloadHandler",
}

PLAYWRIGHT_DEFAULT_NAVIGATION_TIMEOUT = 10_000
PLAYWRIGHT_BROWSER_TYPE = "chromium"
PLAYWRIGHT_LAUNCH_OPTIONS = {
    "timeout": 10_000,
    "args": ["--no-sandbox"],  # --no-sandbox is not recognized in webkit
}
