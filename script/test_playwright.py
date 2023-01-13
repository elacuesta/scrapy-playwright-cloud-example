import asyncio

from playwright import async_playwright


browsers = {
    "chromium": "/ms-playwright/chromium/chrome-linux/chrome",
    "firefox": "/ms-playwright/firefox/firefox/firefox",
    "webkit": "/ms-playwright/webkit/pw_run.sh",
}


async def main():
    async with async_playwright() as pw:
        # for browser_type in [pw.chromium, pw.firefox, pw.webkit]:
        for browser_type in [pw.webkit]:
            print("*" * 100)
            print(browser_type.name)
            browser = await browser_type.launch(
                executable_path=browsers[browser_type.name],
                timeout=5000,
                # args=["--no-sandbox"],  # --no-sandbox is not recognized in webkit
            )
            page = await browser.newPage()
            await page.goto("http://httpbin.org/get")
            print(await page.content())
            await browser.close()


if __name__ == "__main__":
    asyncio.run(main())
