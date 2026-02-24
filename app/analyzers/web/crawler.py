import aiohttp
from bs4 import BeautifulSoup
from urllib.parse import urljoin
from typing import List


async def crawl_site(url: str, limit: int = 20) -> List[str]:

    links = set()

    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(url, timeout=5) as resp:

                html = await resp.text(errors="ignore")

                soup = BeautifulSoup(html, "html.parser")

                for tag in soup.find_all("a", href=True):
                    link = urljoin(url, tag["href"])
                    links.add(link)

                    if len(links) >= limit:
                        break

    except Exception:
        pass

    return list(links)
