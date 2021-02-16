from scrapy import Spider, Request


class GetSpider(Spider):
    name = "get"

    playwright = 1

    def start_requests(self):
        yield Request("http://httpbin.org/get", meta={"playwright": int(self.playwright)})

    def parse(self, response):
        print(response.url)
        print(response.text)
        yield {"url": response.url, "text": response.text}
