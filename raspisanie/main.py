import requests
import json
from bs4 import BeautifulSoup
from datetime import datetime
import time

def get_first_news():
    headers = {
        "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36"
    }

    url = "https://sb.bsu.by/raspisanie/map-902_sa.xml"
    r = requests.get(url=url, headers=headers)

    soup = BeautifulSoup(r.text, "lxml")

    articles_cards = soup.find_all("table", class_="table-schedule")
####
    for article in articles_cards:
        article_title = article.find("tr", vl="14.11.2022").text.strip()
        article_desc = article.find("tr", vl="14.11.2022").find("td").text.strip()
        print({article_title} | {article_desc})

get_first_news()
