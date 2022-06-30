import scrapy


class HeadersSpider(scrapy.Spider):
    name = "headers"
    playwright = 1

    def start_requests(self):
        yield scrapy.Request(
            url="https://httpbin.org/headers",
            meta={"playwright": int(self.playwright)},
        )

    def parse(self, response):
        print(response.url)
        print(response.text)
        yield {"url": response.url}
