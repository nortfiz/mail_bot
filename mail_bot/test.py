import requests
from bs4 import BeautifulSoup

headers = {
    "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9"
}

url = "https://sb.bsu.by/raspisanie/map-902_sa.xml"
response = requests.get(url=url, headers=headers)
soup = BeautifulSoup(response.text, "lxml")

timetable = soup.find('div', class_="sw-result")
# date = timetable.split()
print(timetable)
for i in timetable:
    if i == "Дата обновления":
        print("Its work")
    else:
        print("broke")