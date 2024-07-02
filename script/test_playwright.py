import asyncio

from playwright.async_api import async_playwright


# only chromium installed by default to reduce image size
BROWSERS = [
    "chromium",
    # "firefox",
    # "webkit",
]


async def main():
    async with async_playwright() as pw:
        for browser_name in BROWSERS:
            print("*" * 100)
            print(browser_name)
            browser_type = getattr(pw, browser_name)
            browser = await browser_type.launch(
                timeout=5000,
                # args=["--no-sandbox"],  # --no-sandbox is not recognized in webkit
            )
            page = await browser.new_page()
            await page.goto("http://httpbin.org/get")
            print(await page.content())
            await browser.close()


if __name__ == "__main__":
    asyncio.run(main())
