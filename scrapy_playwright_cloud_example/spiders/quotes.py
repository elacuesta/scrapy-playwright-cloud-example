import subprocess

from scrapy import Spider, Request
from scrapy_playwright.page import PageCoroutine


class QuotesSpider(Spider):
    name = "quotes"

    def __init__(self, *args, **kwargs):
        super(). __init__(*args, **kwargs)
        user = subprocess.run("whoami", stdout=subprocess.PIPE).stdout.strip().decode("utf8")
        self.logger.info(f"Current user is '{user}'")

    def start_requests(self):
        yield Request(
            url="http://quotes.toscrape.com/scroll",
            meta=dict(
                playwright=True,
                playwright_page_coroutines=[
                    PageCoroutine("waitForSelector", "div.quote"),
                    PageCoroutine("evaluate", "window.scrollBy(0, document.body.scrollHeight)"),
                    PageCoroutine("waitForSelector", "div.quote:nth-child(11)"),
                ],
            ),
        )

    async def parse(self, response):
        for quote in response.css("div.quote"):
            yield {
                "text": quote.css("span.text::text").get(),
                "author": quote.css("small.author::text").get(),
                "tags": quote.css("a.tag::text").getall(),
            }
