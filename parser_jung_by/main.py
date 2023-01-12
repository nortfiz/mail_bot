import requests
import json
from bs4 import BeautifulSoup
from selenium import webdriver
import time

def get_first_news():

    headers = {
        "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36"
    }

    url = "https://jung-pro.ru/products/ramki-jung-ac581ch.html"
    r = requests.get(url=url, headers=headers)

    soup = BeautifulSoup(r.text, "lxml")

    product_cards = soup.find_all("div", class_="product-item__wrap")
    product_dict={}
    for product in product_cards:
        product_title = product.find("a", "product-item__title").text.strip()
        product_article_id = product.find("div", "product-item__info-text").text.strip()
        product_url = "https://jung-pro.ru/" + product.find("a").get("href")
        product_img = "https://jung-pro.ru/" + product.find("img").get("src")
        product_brand = product.find("div", class_="product-item__info hidden-mobile").text
        product_article = product.find("div", "product-item__info-text").text.strip()
        product_description = product.find("div", "elctr-prod-parts-row Выключатели for-filter-element")
        # product_article = product_title[25:].split(' ')[-1]
        print(product_description)

        product_dict[product_article_id] = {
            "product_title": product_title,
            "product_brand": product_brand,
            # # "product_series": product_series,
            # # "product_country": product_country,
            "product_article": product_article,
            "product_url": product_url ,
            "product_img": product_img
        }



        with open("json/product_dict_2.json", "w") as file:
            json.dump(product_dict, file, indent=4, ensure_ascii=False)
    # driver.close()



def main():
    get_first_news()


if __name__ == '__main__':
    main()