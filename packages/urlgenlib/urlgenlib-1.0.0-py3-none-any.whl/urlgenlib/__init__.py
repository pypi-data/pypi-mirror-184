from bs4 import BeautifulSoup
import requests
from urllib.parse import urljoin


def urlgen(url: str) -> list:
    r = requests.get(url)
    s = BeautifulSoup(r.content, "html.parser")
    urls = []

    for i in s.prettify().splitlines():
        for j in i.split('"'):
            if j.startswith("http"):
                urls.append(j)
            if j.startswith("/"):
                urls.append(urljoin(url, j))

    return urls
