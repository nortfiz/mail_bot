import json
import pandas as pd

with open("timetable_date.json", "r") as file:
    timetable_date = json.load(file)
    # df = pd.read_json (r'timetable_date.json')
    # df.to_csv(r'date.txt')
    for k,v in (timetable_date.items()):
        # print(k,v)
        q = 0
        q = f"{v['date_now']}"
        print(q)

