import requests
import json
from bs4 import BeautifulSoup

def update_date():
        headers = {
                "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9"
        }

        url = "https://sb.bsu.by/raspisanie/map-902_sa.xml"
        response = requests.get(url=url, headers=headers)
        soup = BeautifulSoup(response.text, "lxml")
        date_now = {}
        timetable = soup.find('div', class_="sw-result")

        k = 1
        for q in range(14):
                date_update = timetable
                date_now[k] = {
                    'date_now': date_update
                }
                k +=1
        with open("test_date.json", "w") as file:
                json.dump(date_now, file, indent=1, sort_keys=True, ensure_ascii=False)
def main():

    update_date()

if __name__ == '__main__':
    main()

