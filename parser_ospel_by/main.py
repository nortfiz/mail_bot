import requests
import json
from bs4 import BeautifulSoup
from selenium import webdriver
import time
import webbrowser

def get_product():
    with open(f"html/ospel_all.html") as file:
        src = file.read()

    soup = BeautifulSoup(src, "lxml")
    product_cards = soup.find_all("div", class_="t951__container_mobile-grid")
    product_dict = {}
    for product in product_cards:
        product_title = product.find_all("div", class_="js-store-prod-name js-product-name t-store__card__title t-name t-name_xs")
        product_url = product.find_all("a")
        x = len(product_url)
        y = len(product_title)
        for k in range(x):
            url = product_url[k].get("href")
            webbrowser.open_new_tab(url)
        # print(product_other[9].text.strip())
        print(k)


def main():
    get_product()


if __name__ == '__main__':
    main()