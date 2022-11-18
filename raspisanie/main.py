import requests
import json
from bs4 import BeautifulSoup
from datetime import datetime
import time

def get_data():
    headers = {
        "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9"
    }

    url = "https://sb.bsu.by/raspisanie/map-902_sa.xml"
    response = requests.get(url=url, headers=headers)
    soup = BeautifulSoup(response.text, "lxml")


    # raspisanie_days = soup.find("div", class_="schedule-days").find_all("span", vl="17.10.2022")
    # raspisanie = soup.find("tbody").find_all("tr", vl="17.10.2022")
    # rasp_days_select = soup.find("td", class_="head-date>18.10.2022")

    select_days = soup.find_all("td", class_="head-date")
    days = soup.find_all(select_days)

    print(days)

    # page_count = soup.find("div", class_="schedule-days").find_all("span")[-1].text

    # for page in range (1, page_count +1):
    #     class_=f"select={page}"

        # response = requests.get(url=url,headers=headers)
        # soup =BeautifulSoup(response.text, "lxml")
        # books_items = soup.find("table", class_="table-schedule").find_all("tr")
        #
        # for bi in books_items:
        #     book_data = bi.find_all("td")
        #
        #     try:
        #         book_title = book_data[0].find("td").text.strip()
        #     except:
        #         print("NO")
        #
        #     print(book_data)


def main():
    get_data()

if __name__ == '__main__':
    main()