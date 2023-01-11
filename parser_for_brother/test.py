import requests
import json
from bs4 import BeautifulSoup
from datetime import datetime
import time
import json

import openpyxl

def get_first_news():
    with open('product_dict.json') as file:
        data = json.load(file)

        # for product in data['1']:
        k = 1
        for k in range(50):
            product = data[k]
            print(k)
        product_title = product['product_title']
        manufacturer_name_title = product['manufacturer_name_title']
        jshop_price_span_title = product['jshop_price_span_title']
        jshop_price_usd_title = product['jshop_price_usd_title']
        old_price_title = product['old_price_title']
        extra_fields_title = product['extra_fields_title']
        product_url = product['product_url']
        img_title = product['img_title']

    book = openpyxl.Workbook()
    sheet = book.active
    sheet['A1'] = 'product_title'
    sheet['B1'] = 'manufacturer_name_title'
    sheet['C1'] = 'jshop_price_span_title'
    sheet['D1'] = 'jshop_price_usd_title'
    sheet['E1'] = 'old_price_title'
    sheet['F1'] = 'extra_fields_title'
    sheet['G1'] = 'product_url'
    sheet['H1'] = 'img_title'
    sheet['A2'] = product_title
    sheet['B2'] = manufacturer_name_title
    sheet['C2'] = jshop_price_span_title
    sheet['D2'] = jshop_price_usd_title
    sheet['E2'] = old_price_title
    sheet['F2'] = extra_fields_title
    sheet['G2'] = product_url
    sheet['H2'] = img_title
    book.save("product_book.xlsx")
    book.close()






def main():
    get_first_news()


if __name__ == '__main__':
    main()



