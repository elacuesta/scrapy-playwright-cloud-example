from scrapy import Spider, Request


class IPSpider(Spider):
    name = "ip"

    playwright = False

    def start_requests(self):
        yield Request("http://httpbin.org/ip", meta={"playwright": self.playwright})

    def parse(self, response):
        yield {"url": response.url, "text": response.text}
