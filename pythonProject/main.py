import requests
import json
from bs4 import BeautifulSoup
from datetime import datetime
import time


def get_first_news():
    headers = {
        "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36"
    }

    url = "https://1prime.ru/state_regulation/"
    r = requests.get(url=url, headers=headers)

    soup = BeautifulSoup(r.text, "lxml")

    articles_cards = soup.find_all("article", class_="rubric-list__article rubric-list__article_default")

    news_dict = {}
    for article in articles_cards:
        article_title = article.find("h2", class_="rubric-list__article-title").text.strip()
        article_img = soup
        article_url = "https://1prime.ru/" + article.find("h2", class_="rubric-list__article-title").find("a").get(
            "href")
        url_2 = article_url
        r = requests.get(url=url_2, headers=headers)
        soup = BeautifulSoup(r.text, "lxml")
        articles_cards = soup.find_all("div", class_="article-body__content")
        for article_2 in articles_cards:
            article_desc = article_2.find("p").text.strip()


        article_date_time = article.find("time").get("datetime")
        date_from_iso = datetime.fromisoformat(article_date_time)
        date_time = datetime.strftime(date_from_iso, "%Y-%m-%d %H:%M:%S")
        article_date_timestamp = time.mktime(datetime.strptime(date_time, "%Y-%m-%d %H:%M:%S").timetuple())

        article_id = article_url.split("/")[-1]
        article_id = article_id[:-5]

        news_dict[article_id] = {
            "article_date_timestamp": article_date_timestamp,
            "article_title": article_title,
            "article_url": article_url,
            "article_desc": article_desc
        }

        with open("news_dict.json", "w") as file:
            json.dump(news_dict, file, indent=4, ensure_ascii=False)


def chek_new_update():
    with open("news_dict.json") as file:
        news_dict = json.load(file)

    headers = {
        "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36"
    }

    url = "https://1prime.ru/state_regulation/"
    r = requests.get(url=url, headers=headers)

    soup = BeautifulSoup(r.text, "lxml")

    articles_cards = soup.find_all("article", class_="rubric-list__article rubric-list__article_default")

    fresh_news = {}
    for article in articles_cards:

        article_url = "https://1prime.ru/" + article.find("h2", class_="rubric-list__article-title").find("a").get(
            "href")
        article_id = article_url.split("/")[-1]
        article_id = article_id[:-5]
        if article_id in news_dict:
            continue
        else:
            article_title = article.find("h2", class_="rubric-list__article-title").text.strip()
            url_2 = article_url
            r = requests.get(url=url_2, headers=headers)
            soup = BeautifulSoup(r.text, "lxml")
            articles_cards = soup.find_all("div", class_="article-body__content")
            for article_2 in articles_cards:
                article_desc = article_2.find("p").text.strip()

            article_date_time = article.find("time").get("datetime")
            date_from_iso = datetime.fromisoformat(article_date_time)
            date_time = datetime.strftime(date_from_iso, "%Y-%m-%d %H:%M:%S")
            article_date_timestamp = time.mktime(datetime.strptime(date_time, "%Y-%m-%d %H:%M:%S").timetuple())

            news_dict[article_id] = {
                "article_date_timestamp": article_date_timestamp,
                "article_title": article_title,
                "article_url": article_url,
                "article_desc": article_desc
            }

            fresh_news[article_id] = {
                "article_date_timestamp": article_date_timestamp,
                "article_title": article_title,
                "article_url": article_url,
                "article_desc": article_desc
            }

    with open("news_dict.json", "w") as file:
        json.dump(news_dict, file, indent=4, ensure_ascii=False)

    return fresh_news

def main():
    # get_first_news()
    print(chek_new_update())


if __name__ == '__main__':
    main()
