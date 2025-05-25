```python
import aiohttp
import asyncio

class XSSScanner:
    def __init__(self, config):
        self.payloads = config.get("xss_scanner", {}).get("options", {}).get("payloads", [])
        self.timeout = config.get("xss_scanner", {}).get("options", {}).get("timeout", 30)

    async def scan(self, url):
        async with aiohttp.ClientSession() as session:
            for payload in self.payloads:
                try:
                    async with session.get(f"{url}?q={payload}", timeout=self.timeout) as response:
                        content = await response.text()
                        if payload in content:
                            print(f"Potential XSS found at {url} with payload: {payload}")
                except Exception as e:
                    print(f"Error scanning {url}: {e}")

if __name__ == "__main__":
    config = {"xss_scanner": {"options": {"payloads": ["<script>alert(1)</script>"], "timeout": 30}}}
    scanner = XSSScanner(config)
    asyncio.run(scanner.scan("https://example.com"))
```
