import asyncio
import inspect
import json
from pathlib import Path

import playwright
from playwright import async_playwright


browsers_path = Path(inspect.getfile(playwright)).parent / "driver/browsers.json"
browsers = {x["name"]: x for x in json.loads(browsers_path.read_text())["browsers"]}
browsers["chromium"]["path"] = f"/ms-playwright/chromium-{browsers['chromium']['revision']}/chrome-linux/chrome"
browsers["firefox"]["path"] = f"/ms-playwright/firefox-{browsers['firefox']['revision']}/firefox/firefox"

async def main():
    async with async_playwright() as pw:
        for browser_type in [pw.chromium, pw.firefox]:
            print("*" * 100)
            print(browser_type.name)
            browser = await browser_type.launch(
                executablePath=browsers[browser_type.name]["path"],
                args=["--no-sandbox"],
                timeout=5000,
            )
            page = await browser.newPage()
            await page.goto("https://httpbin.org/ip")
            print(await page.content())
            await browser.close()


if __name__ == "__main__":
    asyncio.run(main())
