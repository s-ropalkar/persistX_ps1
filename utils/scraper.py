
# from urllib.request import urlopen
# from bs4 import BeautifulSoup


# def extract_text_from_url(url):
#     try:
#         response = urlopen(url, timeout=5)
#         html = response.read()

#         soup = BeautifulSoup(html, "html.parser")

#         for tag in soup(["script", "style"]):
#             tag.decompose()

#         text = soup.get_text(separator=" ")

#         return text.strip()

#     except Exception as e:
#         print("Scraping error:", e)
#         return ""
# utils/scraper.py

from urllib.request import Request, urlopen
from bs4 import BeautifulSoup


def extract_text_from_url(url):
    try:
        # 🔥 add headers (VERY IMPORTANT)
        req = Request(
            url,
            headers={
                'User-Agent': 'Mozilla/5.0'
            }
        )

        response = urlopen(req, timeout=5)
        html = response.read()

        soup = BeautifulSoup(html, "html.parser")

        for tag in soup(["script", "style"]):
            tag.decompose()

        text = soup.get_text(separator=" ")

        return text.strip()

    except Exception as e:
        print("Scraping error:", e)
        return ""