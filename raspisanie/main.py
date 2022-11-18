import requests
import json
from bs4 import BeautifulSoup



def get_data():
    headers = {
        "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9"
    }

    url = "https://sb.bsu.by/raspisanie/map-902_sa.xml"
    response = requests.get(url=url, headers=headers)
    soup = BeautifulSoup(response.text, "lxml")
    timetable_dict = {}

    timetable = soup.find("tbody").find_all("tr", vl="14.11.2022")

    for i in range(30):

        timetable_title = timetable[i].text
        print(timetable_title)
        timetable_dict["1"] = {
            # "timetable_date": timetable_date,
            "timetable_title": timetable_title
        }
        with open("timetable_dict.json", "w") as file:
            json.dump(timetable_dict, file, indent=2, ensure_ascii=False)

        # try:
        #     timetable_date = timetable[0].text
        # except:
        #     timetable_date = "rqwe"

        # try:
        #     timetable_title = timetable[i].text
        # except:
        #     timetable_title = "qwe"

def main():
    get_data()


if __name__ == '__main__':
    main()
