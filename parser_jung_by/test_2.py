
import json
from bs4 import BeautifulSoup

def get_janga_prod_test():
    g = 8
    with open(f"html/page_source_{g}_jung-a-creation.html") as file:
        src = file.read()

    soup = BeautifulSoup(src, "lxml")
    product_cards = soup.find_all("div", class_="product-wrap")
    product_dict={}
    for product in product_cards:
        product_other = product.find_all("td", class_="table-col introtext-col")
        y = len(product_other)
        for q in range (y):
            product_other[q] = product.find_all("td", class_="table-col introtext-col")[q]
            print(product_other[0].text.strip())


def get_janga_prod():
    for g in range (8):
        with open(f"html/page_source_{g}_jung-a-creation.html") as file:
            src = file.read()

        soup = BeautifulSoup(src, "lxml")
        product_cards = soup.find_all("div", class_="product-wrap")
        product_dict = {}
        for product in product_cards:
            product_title = product.find("div", "product-title").text.strip()
            product_article_id = product.find_all("td", "product-properties__value")[2].text.strip()
            product_img = "https://jung-pro.ru/" + product.find("img").get("src")
            product_other = product.find_all("td", class_="table-col introtext-col")
            y = len(product_other)
            if y == 1:
                for q in range(y):
                    product_other[q] = product.find_all("td", class_="table-col introtext-col")[q]
                    print(product_other[0].text.strip())
                    product_other_1 = product_other[0].text.strip()
                    with open(f"html/page_source_{g}_jung-a-creation.html") as file:
                        src = file.read()
                    soup = BeautifulSoup(src, "lxml")
                    product_brand = soup.find_all("td", class_="product-properties__value")[0].text.strip()
                    product_series = soup.find_all("td", class_="product-properties__value")[1].text.strip()
                    product_article = soup.find_all("td", class_="product-properties__value")[2].text.strip()
                    product_material = soup.find_all("td", class_="product-properties__value")[3].text.strip()
                    product_color = soup.find_all("td", class_="product-properties__value")[4].text.strip()
                    product_type = soup.find_all("td", class_="product-properties__value")[5].text.strip()
                    product_kind_material = soup.find_all("td", class_="product-properties__value")[6].text.strip()
                    product_type_surface = soup.find_all("td", class_="product-properties__value")[7].text.strip()
                    product_halogen_free = soup.find_all("td", class_="product-properties__value")[8].text.strip()
                    product_mounting_orientation = soup.find_all("td", class_="product-properties__value")[
                        9].text.strip()
                    product_field_of_inscription = soup.find_all("td", class_="product-properties__value")[
                        10].text.strip()
                    product_height = soup.find_all("td", class_="product-properties__value")[11].text.strip()
                    product_width = soup.find_all("td", class_="product-properties__value")[12].text.strip()
                    product_without_baffle = soup.find_all("td", class_="product-properties__value")[13].text.strip()
                    product_hinged_lid = soup.find_all("td", class_="product-properties__value")[14].text.strip()
                    product_degree_of_protection = soup.find_all("td", class_="product-properties__value")[
                        15].text.strip()
                    product_number_of_posts = soup.find_all("td", class_="product-properties__value")[16].text.strip()

                    product_dict[product_article_id] = {
                        "product_title": product_title,
                        "product_brand": product_brand,
                        "product_series": product_series,
                        "product_article": product_article,
                        "product_material": product_material,
                        "product_color": product_color,
                        "product_type": product_type,
                        "product_kind_material": product_kind_material,
                        "product_type_surface": product_type_surface,
                        "product_halogen_free": product_halogen_free,
                        "product_mounting_orientation": product_mounting_orientation,
                        "product_field_of_inscription": product_field_of_inscription,
                        "product_height": product_height,
                        "product_width": product_width,
                        "product_without_baffle": product_without_baffle,
                        "product_hinged_lid": product_hinged_lid,
                        "product_degree_of_protection": product_degree_of_protection,
                        "product_other_1": product_other_1,
                        "product_number_of_posts": product_number_of_posts,
                        "product_img": product_img
                    }

                    with open(f"json/page_source_{g}_jung-a-creation.json", "w") as file:
                        json.dump(product_dict, file, indent=4, ensure_ascii=False)
                    break
            elif y == 2:
                for q in range(y):
                    product_other[q] = product.find_all("td", class_="table-col introtext-col")[q]
                    print(product_other[0].text.strip())
                    product_other_1 = product_other[0].text.strip()
                    product_other_2 = product_other[1].text.strip()
                    with open(f"html/page_source_{g}_jung-a-creation.html") as file:
                        src = file.read()
                    soup = BeautifulSoup(src, "lxml")
                    product_brand = soup.find_all("td", class_="product-properties__value")[0].text.strip()
                    product_series = soup.find_all("td", class_="product-properties__value")[1].text.strip()
                    product_article = soup.find_all("td", class_="product-properties__value")[2].text.strip()
                    product_material = soup.find_all("td", class_="product-properties__value")[3].text.strip()
                    product_color = soup.find_all("td", class_="product-properties__value")[4].text.strip()
                    product_type = soup.find_all("td", class_="product-properties__value")[5].text.strip()
                    product_kind_material = soup.find_all("td", class_="product-properties__value")[6].text.strip()
                    product_type_surface = soup.find_all("td", class_="product-properties__value")[7].text.strip()
                    product_halogen_free = soup.find_all("td", class_="product-properties__value")[8].text.strip()
                    product_mounting_orientation = soup.find_all("td", class_="product-properties__value")[
                        9].text.strip()
                    product_field_of_inscription = soup.find_all("td", class_="product-properties__value")[
                        10].text.strip()
                    product_height = soup.find_all("td", class_="product-properties__value")[11].text.strip()
                    product_width = soup.find_all("td", class_="product-properties__value")[12].text.strip()
                    product_without_baffle = soup.find_all("td", class_="product-properties__value")[13].text.strip()
                    product_hinged_lid = soup.find_all("td", class_="product-properties__value")[14].text.strip()
                    product_degree_of_protection = soup.find_all("td", class_="product-properties__value")[
                        15].text.strip()
                    product_number_of_posts = soup.find_all("td", class_="product-properties__value")[16].text.strip()

                    product_dict[product_article_id] = {
                        "product_title": product_title,
                        "product_brand": product_brand,
                        "product_series": product_series,
                        "product_article": product_article,
                        "product_material": product_material,
                        "product_color": product_color,
                        "product_type": product_type,
                        "product_kind_material": product_kind_material,
                        "product_type_surface": product_type_surface,
                        "product_halogen_free": product_halogen_free,
                        "product_mounting_orientation": product_mounting_orientation,
                        "product_field_of_inscription": product_field_of_inscription,
                        "product_height": product_height,
                        "product_width": product_width,
                        "product_without_baffle": product_without_baffle,
                        "product_hinged_lid": product_hinged_lid,
                        "product_degree_of_protection": product_degree_of_protection,
                        "product_other_1": product_other_1,
                        "product_other_2": product_other_2,
                        "product_number_of_posts": product_number_of_posts,
                        "product_img": product_img
                    }

                    with open(f"html/page_source_{g}_jung-a-creation.html", "w") as file:
                        json.dump(product_dict, file, indent=4, ensure_ascii=False)
                    break
            elif y == 3:
                for q in range(y):
                    product_other[q] = product.find_all("td", class_="table-col introtext-col")[q]
                    print(product_other[0].text.strip())
                    product_other_1 = product_other[0].text.strip()
                    product_other_2 = product_other[1].text.strip()
                    product_other_3 = product_other[2].text.strip()
                    with open(f"html/page_source_{g}_jung-a-creation.html") as file:
                        src = file.read()
                    soup = BeautifulSoup(src, "lxml")
                    product_brand = soup.find_all("td", class_="product-properties__value")[0].text.strip()
                    product_series = soup.find_all("td", class_="product-properties__value")[1].text.strip()
                    product_article = soup.find_all("td", class_="product-properties__value")[2].text.strip()
                    product_material = soup.find_all("td", class_="product-properties__value")[3].text.strip()
                    product_color = soup.find_all("td", class_="product-properties__value")[4].text.strip()
                    product_type = soup.find_all("td", class_="product-properties__value")[5].text.strip()
                    product_kind_material = soup.find_all("td", class_="product-properties__value")[6].text.strip()
                    product_type_surface = soup.find_all("td", class_="product-properties__value")[7].text.strip()
                    product_halogen_free = soup.find_all("td", class_="product-properties__value")[8].text.strip()
                    product_mounting_orientation = soup.find_all("td", class_="product-properties__value")[
                        9].text.strip()
                    product_field_of_inscription = soup.find_all("td", class_="product-properties__value")[
                        10].text.strip()
                    product_height = soup.find_all("td", class_="product-properties__value")[11].text.strip()
                    product_width = soup.find_all("td", class_="product-properties__value")[12].text.strip()
                    product_without_baffle = soup.find_all("td", class_="product-properties__value")[13].text.strip()
                    product_hinged_lid = soup.find_all("td", class_="product-properties__value")[14].text.strip()
                    product_degree_of_protection = soup.find_all("td", class_="product-properties__value")[
                        15].text.strip()
                    product_number_of_posts = soup.find_all("td", class_="product-properties__value")[16].text.strip()

                    product_dict[product_article_id] = {
                        "product_title": product_title,
                        "product_brand": product_brand,
                        "product_series": product_series,
                        "product_article": product_article,
                        "product_material": product_material,
                        "product_color": product_color,
                        "product_type": product_type,
                        "product_kind_material": product_kind_material,
                        "product_type_surface": product_type_surface,
                        "product_halogen_free": product_halogen_free,
                        "product_mounting_orientation": product_mounting_orientation,
                        "product_field_of_inscription": product_field_of_inscription,
                        "product_height": product_height,
                        "product_width": product_width,
                        "product_without_baffle": product_without_baffle,
                        "product_hinged_lid": product_hinged_lid,
                        "product_degree_of_protection": product_degree_of_protection,
                        "product_other_1": product_other_1,
                        "product_other_2": product_other_2,
                        "product_other_3": product_other_3,
                        "product_number_of_posts": product_number_of_posts,
                        "product_img": product_img
                    }

                    with open(f"html/page_source_{g}_jung-a-creation.html", "w") as file:
                        json.dump(product_dict, file, indent=4, ensure_ascii=False)
                    break
            else:
                for q in range(y):
                    product_other[q] = product.find_all("td", class_="table-col introtext-col")[q]
                    print(product_other[0].text.strip())
                    product_other_1 = product_other[0].text.strip()
                    product_other_2 = product_other[1].text.strip()
                    product_other_3 = product_other[2].text.strip()
                    product_other_4 = product_other[3].text.strip()
                    with open(f"html/page_source_{g}_jung-a-creation.html") as file:
                        src = file.read()
                    soup = BeautifulSoup(src, "lxml")
                    product_brand = soup.find_all("td", class_="product-properties__value")[0].text.strip()
                    product_series = soup.find_all("td", class_="product-properties__value")[1].text.strip()
                    product_article = soup.find_all("td", class_="product-properties__value")[2].text.strip()
                    product_material = soup.find_all("td", class_="product-properties__value")[3].text.strip()
                    product_color = soup.find_all("td", class_="product-properties__value")[4].text.strip()
                    product_type = soup.find_all("td", class_="product-properties__value")[5].text.strip()
                    product_kind_material = soup.find_all("td", class_="product-properties__value")[6].text.strip()
                    product_type_surface = soup.find_all("td", class_="product-properties__value")[7].text.strip()
                    product_halogen_free = soup.find_all("td", class_="product-properties__value")[8].text.strip()
                    product_mounting_orientation = soup.find_all("td", class_="product-properties__value")[
                        9].text.strip()
                    product_field_of_inscription = soup.find_all("td", class_="product-properties__value")[
                        10].text.strip()
                    product_height = soup.find_all("td", class_="product-properties__value")[11].text.strip()
                    product_width = soup.find_all("td", class_="product-properties__value")[12].text.strip()
                    product_without_baffle = soup.find_all("td", class_="product-properties__value")[13].text.strip()
                    product_hinged_lid = soup.find_all("td", class_="product-properties__value")[14].text.strip()
                    product_degree_of_protection = soup.find_all("td", class_="product-properties__value")[
                        15].text.strip()
                    product_number_of_posts = soup.find_all("td", class_="product-properties__value")[16].text.strip()

                    product_dict[product_article_id] = {
                        "product_title": product_title,
                        "product_brand": product_brand,
                        "product_series": product_series,
                        "product_article": product_article,
                        "product_material": product_material,
                        "product_color": product_color,
                        "product_type": product_type,
                        "product_kind_material": product_kind_material,
                        "product_type_surface": product_type_surface,
                        "product_halogen_free": product_halogen_free,
                        "product_mounting_orientation": product_mounting_orientation,
                        "product_field_of_inscription": product_field_of_inscription,
                        "product_height": product_height,
                        "product_width": product_width,
                        "product_without_baffle": product_without_baffle,
                        "product_hinged_lid": product_hinged_lid,
                        "product_degree_of_protection": product_degree_of_protection,
                        "product_other_1": product_other_1,
                        "product_other_2": product_other_2,
                        "product_other_3": product_other_3,
                        "product_other_4": product_other_4,
                        "product_number_of_posts": product_number_of_posts,
                        "product_img": product_img
                    }

                    with open(f"html/page_source_{g}_jung-a-creation.html", "w") as file:
                        json.dump(product_dict, file, indent=4, ensure_ascii=False)
                    break



        # except:
        #
        #     with open("html/page_source_1_jung-a-creation.html") as file:
        #         src = file.read()
        #     soup = BeautifulSoup(src, "lxml")
        #     product_brand = soup.find_all("td", class_="product-properties__value")[0].text.strip()
        #     product_series = soup.find_all("td", class_="product-properties__value")[1].text.strip()
        #     product_article = soup.find_all("td", class_="product-properties__value")[2].text.strip()
        #     product_material = soup.find_all("td", class_="product-properties__value")[3].text.strip()
        #     product_color = soup.find_all("td", class_="product-properties__value")[4].text.strip()
        #     product_type = soup.find_all("td", class_="product-properties__value")[5].text.strip()
        #     product_kind_material = soup.find_all("td", class_="product-properties__value")[6].text.strip()
        #     product_type_surface = soup.find_all("td", class_="product-properties__value")[7].text.strip()
        #     product_halogen_free = soup.find_all("td", class_="product-properties__value")[8].text.strip()
        #     product_mounting_orientation = soup.find_all("td", class_="product-properties__value")[9].text.strip()
        #     product_field_of_inscription = soup.find_all("td", class_="product-properties__value")[10].text.strip()
        #     product_height = soup.find_all("td", class_="product-properties__value")[11].text.strip()
        #     product_width = soup.find_all("td", class_="product-properties__value")[12].text.strip()
        #     product_without_baffle = soup.find_all("td", class_="product-properties__value")[13].text.strip()
        #     product_hinged_lid = soup.find_all("td", class_="product-properties__value")[14].text.strip()
        #     product_degree_of_protection = soup.find_all("td", class_="product-properties__value")[15].text.strip()
        #     product_number_of_posts = soup.find_all("td", class_="product-properties__value")[16].text.strip()
        #
        #     product_dict[product_article_id] = {
        #         "product_title": product_title,
        #         "product_brand": product_brand,
        #         "product_series": product_series,
        #         "product_article": product_article,
        #         "product_material": product_material,
        #         "product_color": product_color,
        #         "product_type": product_type,
        #         "product_kind_material": product_kind_material,
        #         "product_type_surface": product_type_surface,
        #         "product_halogen_free": product_halogen_free,
        #         "product_mounting_orientation": product_mounting_orientation,
        #         "product_field_of_inscription": product_field_of_inscription,
        #         "product_height": product_height,
        #         "product_width": product_width,
        #         "product_without_baffle": product_without_baffle,
        #         "product_hinged_lid": product_hinged_lid,
        #         "product_degree_of_protection": product_degree_of_protection,
        #         "product_number_of_posts": product_number_of_posts,
        #         "product_img": product_img
        #     }
        #
        #     with open(f"html/page_source_{g}_jung-a-creation.html", "w") as file:
        #         json.dump(product_dict, file, indent=4, ensure_ascii=False)
        #     break

def main():
    # get_janga_prod_test()
    get_janga_prod()

if __name__ == '__main__':
    main()
