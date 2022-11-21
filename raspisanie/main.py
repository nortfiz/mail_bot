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

    timetable = soup.find("tbody").find_all("tr", vl="21.11.2022")
    k = 1
    for i in range(20):
        id = timetable[i].text

        timetable_dict[k] = {
            "timetable_title": id,
            "timetable_id": k
        }
        k += 1

    with open("timetable_dict.json", "w") as file:
        json.dump(timetable_dict, file, indent=1, sort_keys=True, ensure_ascii=False)

# def select_data():
#     with open("timetable_dict.json") as file:
#         timetable_dict = json.load(file)
#
#     for i in timetable_dict.itmes():
#             if i['timetable_id'] == '1':
#                 print("Its OKEY")
#             else:
#                 print("Dont okey")
def main():
    get_data()
    # select_data()

if __name__ == '__main__':
    main()