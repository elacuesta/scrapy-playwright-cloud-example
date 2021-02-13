BOT_NAME = "scrapy_playwright_cloud_example"

SPIDER_MODULES = ["scrapy_playwright_cloud_example.spiders"]
NEWSPIDER_MODULE = "scrapy_playwright_cloud_example.spiders"

# Crawl responsibly by identifying yourself (and your website) on the user-agent
USER_AGENT = (
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 "
    "(KHTML, like Gecko) Chrome/81.0.4044.129 Safari/537.36"
)

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

FEED_EXPORT_ENCODING = "utf8"
FEED_EXPORT_INDENT = 4

CONCURRENT_REQUESTS = 32

LOG_LEVEL = "INFO"

# scrapy-playwright settings

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
    # "args": ["--no-sandbox"],
}
