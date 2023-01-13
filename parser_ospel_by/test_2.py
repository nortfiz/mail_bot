from selenium import webdriver
from selenium.webdriver.common.by import By
import json
from bs4 import BeautifulSoup
import pandas
import time
import requests


def get_janga_prod_test():
    # options
    options = webdriver.ChromeOptions()

    # user-agent
    options.add_argument(
        "User-Agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36")

    # for ChromeDriver version
    options.add_argument("--disable-blink-features=AutomationControlled")

    driver = webdriver.Chrome(
        executable_path="/home/user/git/parser_jung_by/ChromeDrive/chromedriver",
        options=options
    )

    # url
    url = "https://xn--e1amhej.xn--90ais/katalog"

    name_product = "jung-ls-plus"
    # list item
    headers = {
        "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36"
    }

    r = requests.get(url=url, headers=headers)

    soup = BeautifulSoup(r.text, "lxml")


def main():
    get_janga_prod_test()

if __name__ == '__main__':
    main()
