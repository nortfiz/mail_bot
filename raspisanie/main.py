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
    for i in range(10):
        id = timetable[i].text
        timetable_dict = {
            "qwe": id
        }
    with open("otus.txt", "w", encoding='utf8') as file:
        file.write(id)
        print(id)


    # for a_id in range(20):
    #
    #     for i in range(10):
    #
    #         timetable_title = timetable[i].text
    #
    #         # try:
    #         #     timetable_title = timetable[i].text
    #         # except:
    #         #     timetable_title = "qwe"
    #
    #         timetable_dict[a_id] = {
    #             "timetable_title": timetable_title
    #         }
    #         with open("timetable_dict.json", "w") as file:
    #             json.dump(timetable_dict, file, indent=5, ensure_ascii=False)
    #         print(timetable_title)
    # if timetable_title !="qwe":
    #     with open("timetable_dict.json", "w") as file:
    #         json.dump(timetable_dict, file, indent=5, ensure_ascii=False)
    # else:
    #     print("error")

        # try:
        #     timetable_date = timetable[0].text
        # except:
        #     timetable_date = "rqwe"



def main():
    get_data()


if __name__ == '__main__':
    main()

# timetable_title0 = timetable[0].text
# timetable_title1 = timetable[1].text
# timetable_title2 = timetable[2].text
# timetable_title3 = timetable[3].text
# timetable_title4 = timetable[4].text
# timetable_title5 = timetable[5].text
# timetable_title6 = timetable[6].text
# timetable_title7 = timetable[7].text
# timetable_title8 = timetable[8].text
# timetable_title9 = timetable[9].text
# timetable_title10 = timetable[10].text
# timetable_title11 = timetable[11].text
# timetable_title12 = timetable[12].text
# timetable_title13 = timetable[13].text
# timetable_title14 = timetable[14].text
# timetable_title15 = timetable[15].text
# timetable_title16 = timetable[16].text
# timetable_title17 = timetable[17].text
# timetable_title18 = timetable[18].text
# timetable_title19 = timetable[19].text
# timetable_title20 = timetable[20].text
# timetable_title21 = timetable[21].text
# timetable_title22 = timetable[22].text
# timetable_title23 = timetable[23].text
# timetable_title24 = timetable[24].text
# timetable_title25 = timetable[25].text


# "timetable_title0": timetable_title0,
# "timetable_title1": timetable_title1,
# "timetable_title2": timetable_title2,
# "timetable_title3": timetable_title3,
# "timetable_title4": timetable_title4,
# "timetable_title5": timetable_title5,
# "timetable_title6": timetable_title6,
# "timetable_title7": timetable_title7,
# "timetable_title8": timetable_title8,
# "timetable_title9": timetable_title9,
# "timetable_title10": timetable_title10,
# "timetable_title11": timetable_title11,
# "timetable_title12": timetable_title12,
# "timetable_title13": timetable_title13,
# "timetable_title14": timetable_title14,
# "timetable_title15": timetable_title15,
# "timetable_title16": timetable_title16,
# "timetable_title17": timetable_title17,
# "timetable_title18": timetable_title18,
# "timetable_title19": timetable_title19,
# "timetable_title20": timetable_title20,
# "timetable_title21": timetable_title21,
# "timetable_title22": timetable_title22,
# "timetable_title23": timetable_title23
# "timetable_title24": timetable_title24,
# "timetable_title25": timetable_title25