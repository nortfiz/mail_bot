# import requests
# import json
# from bs4 import BeautifulSoup
#
# def get_data():
#     headers = {
#         "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36",
#         "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9"
#     }
#
#     url = "https://sb.bsu.by/raspisanie/map-902_sa.xml"
#     response = requests.get(url=url, headers=headers)
#     soup = BeautifulSoup(response.text, "lxml")
#     timetable_date = {}
#
#     timetable = soup.find('div', class_="sw-result")
#     r = "Дата обновления 16.11.2022 16:28"
#     text_find = timetable.find(text=r)
#     if text_find == r:
#         timetable_date = {
#             "timetable_date": r
#             # "timetable_id": k
#         }
#         # with open("timetable_date.json", "w") as file:
#         #     json.dump(timetable_date, file, indent=1, sort_keys=True, ensure_ascii=False)
#         print(text_find)
#     else:
#         print("Please, update timetable!!!")
#
# def main():
#     get_data()
#     # select_data()
#
#
# if __name__ == '__main__':
#     main()
import json

with open("timetable_date.json", "r") as file:
    dict = json.load(file)
    r = "Дата обновления 16.11.2022 16:28"
    text_find = dict.items(text=r)
    if text_find == r:
        timetable_date = {
            "timetable_date": r
                # "timetable_id": k
        }
            # with open("timetable_date.json", "w") as file:
            #     json.dump(timetable_date, file, indent=1, sort_keys=True, ensure_ascii=False)
        print(text_find)
    else:
        print("Please, update timetable!!!")
