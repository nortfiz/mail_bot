from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import requests
import json
from bs4 import BeautifulSoup


def save_page_product():
    # options
    options = webdriver.ChromeOptions()

    # user-agent
    options.add_argument(
        "User-Agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36")

    # for ChromeDriver version
    options.add_argument("--disable-blink-features=AutomationControlled")

    # headless mode
    # options.add_argument("--headless")
    # options.headless = True

    driver = webdriver.Chrome(
        executable_path="/home/user/git/parser_jung_by/ChromeDrive/chromedriver",
        options=options
    )

    # url
    url = "https://jung-pro.ru/serii/jung-ls-plus/"

    name_product = "jung-ls-plus"
# list item
    headers = {
        "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36"
    }

    r = requests.get(url=url, headers=headers)

    soup = BeautifulSoup(r.text, "lxml")
    product_cards = soup.find_all("a", "product-item__link")
    y = len(product_cards)
    print(y)
    for k in range(y):
        k += 1
        driver.get(url)
        driver.maximize_window()
        # time.sleep(2)
        # button_discription = driver.find_element(By.XPATH, "(//span[contains(text(),'состоит из')])[1]")
        # time.sleep(2)
        # button_discription.click()
        items = driver.find_element(By.XPATH, f"(//a[@class='product-item__link'])[{k}]")
        items.click()
        time.sleep(1)
        pageSource = driver.page_source
        fileToWrite = open(f"html/page_source_{k}_{name_product}.html", "w")
        fileToWrite.write(pageSource)
        fileToWrite.close()
        # print(driver.find_element(By.XPATH, "(//td[contains(text(),'Бренд:')])[2]"))
        driver.stop_client()
    driver.close()
    driver.quit()
def get_janga_prod():
    for i in range (38):
        name_product = "jung-ls-plus"
        i+=1
        with open(f"html/page_source_{i}_{name_product}.html") as file:
            src = file.read()

        soup = BeautifulSoup(src, "lxml")
        product_cards = soup.find_all("div", class_="product-wrap")
        product_dict = {}
        for product in product_cards:
            product_other = product.find_all("td", class_="table-col introtext-col")
            y = len(product_other)
            for product in product_cards:
                product_title = product.find("div", "product-title").text.strip()
                product_article_id = product.find_all("td", "product-properties__value")[2].text.strip()
                product_img = "https://jung-pro.ru/" + product.find("img").get("src")
                if y == 0:
                    with open(f"html/page_source_{i}_{name_product}.html") as file:
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
                        "product_number_of_posts": product_number_of_posts,
                        "product_img": product_img
                    }
                    with open(f"json/page_source_{i}_{name_product}.json", "w") as file:
                        json.dump(product_dict, file, indent=4, ensure_ascii=False)
                    break
                if y == 1:
                    for q in range(y):
                        with open(f"html/page_source_{i}_{name_product}.html") as file:
                            src = file.read()
                        soup = BeautifulSoup(src, "lxml")

                        product_other[q] = product.find_all("td", class_="table-col introtext-col")[q]

                        product_other_1 = product_other[0].text.strip()

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
                        product_without_baffle = soup.find_all("td", class_="product-properties__value")[
                            13].text.strip()
                        product_hinged_lid = soup.find_all("td", class_="product-properties__value")[14].text.strip()
                        product_degree_of_protection = soup.find_all("td", class_="product-properties__value")[
                            15].text.strip()
                        product_number_of_posts = soup.find_all("td", class_="product-properties__value")[
                            16].text.strip()

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
                            "product_number_of_posts": product_number_of_posts,
                            "product_other_1": product_other_1,
                            "product_img": product_img
                        }
                        with open(f"json/page_source_{i}_{name_product}.json", "w") as file:
                            json.dump(product_dict, file, indent=4, ensure_ascii=False)
                        break
                elif y == 2:
                    for q in range(y):
                        with open(f"html/page_source_{i}_{name_product}.html") as file:
                            src = file.read()
                        soup = BeautifulSoup(src, "lxml")

                        product_other[q] = product.find_all("td", class_="table-col introtext-col")[q]
                        product_other_1 = product_other[0].text.strip()
                        product_other_2 = product_other[1].text.strip()


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
                        product_without_baffle = soup.find_all("td", class_="product-properties__value")[
                            13].text.strip()
                        product_hinged_lid = soup.find_all("td", class_="product-properties__value")[14].text.strip()
                        product_degree_of_protection = soup.find_all("td", class_="product-properties__value")[
                            15].text.strip()
                        product_number_of_posts = soup.find_all("td", class_="product-properties__value")[
                            16].text.strip()

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
                            "product_number_of_posts": product_number_of_posts,
                            "product_other_1": product_other_1,
                            "product_other_2": product_other_2,
                            "product_img": product_img
                        }
                        with open(f"json/page_source_{i}_{name_product}.json", "w") as file:
                            json.dump(product_dict, file, indent=4, ensure_ascii=False)
                        break
                else:
                    for q in range(y):
                        with open(f"html/page_source_{i}_{name_product}.html") as file:
                            src = file.read()
                        soup = BeautifulSoup(src, "lxml")

                        product_other[q] = product.find_all("td", class_="table-col introtext-col")[q]
                        # print(product_other[0].text.strip())
                        product_other_1 = product_other[0].text.strip()
                        product_other_2 = product_other[1].text.strip()
                        product_other_3 = product_other[2].text.strip()

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
                        product_without_baffle = soup.find_all("td", class_="product-properties__value")[
                            13].text.strip()
                        product_hinged_lid = soup.find_all("td", class_="product-properties__value")[14].text.strip()
                        product_degree_of_protection = soup.find_all("td", class_="product-properties__value")[
                            15].text.strip()
                        product_number_of_posts = soup.find_all("td", class_="product-properties__value")[
                            16].text.strip()

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
                            "product_number_of_posts": product_number_of_posts,
                            "product_other_1": product_other_1,
                            "product_other_2": product_other_2,
                            "product_other_3": product_other_3,
                            "product_img": product_img
                        }
                        with open(f"json/page_source_{i}_{name_product}.json", "w") as file:
                            json.dump(product_dict, file, indent=4, ensure_ascii=False)
                        break


def main():
    save_page_product()
    get_janga_prod()

if __name__ == '__main__':
    main()