import csv
import json

with open('date.csv', "w") as file:
    writer = csv.writer(file)
    writer.writerow(
        ("product_title", "product_brand")
    )

with open('json/a-550/page_source_1_jung-a-550.json') as file_2:
    product_json = json.load(file_2)
for product in product_json:
    with open("date.csv", "a") as file:
        writer=csv.writer(file)
        writer.writerow(
            product
        )

