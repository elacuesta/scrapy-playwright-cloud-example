BOT_NAME = "sc_playwright_example"

SPIDER_MODULES = ["sc_playwright_example.spiders"]
NEWSPIDER_MODULE = "sc_playwright_example.spiders"

# Crawl responsibly by identifying yourself (and your website) on the user-agent
USER_AGENT = (
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 "
    "(KHTML, like Gecko) Chrome/81.0.4044.129 Safari/537.36"
)

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

TWISTED_REACTOR = "twisted.internet.asyncioreactor.AsyncioSelectorReactor"

DOWNLOAD_HANDLERS = {
    "http": "scrapy_playwright.handler.ScrapyPlaywrightDownloadHandler",
    # "https": "scrapy_playwright.handler.ScrapyPlaywrightDownloadHandler",
}

FEED_EXPORT_ENCODING = "utf8"
FEED_EXPORT_INDENT = 4

CONCURRENT_REQUESTS = 32

LOG_LEVEL = "INFO"

PLAYWRIGHT_LAUNCH_OPTIONS = {}
