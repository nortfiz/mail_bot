from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.keys import Keys


#o ptions
options = webdriver.ChromeOptions()

# user-agent
options.add_argument("User-Agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36")

# for ChromeDriver version
options.add_argument("--disable-blink-features=AutomationControlled")

# headless mode
# options.add_argument("--headless")
# options.headless = True

driver = webdriver.Chrome(
    executable_path="/home/user/git/parser_jung_by/ChromeDrive/chromedriver",
    options=options
)
k=0
for k in range (2):
    k+=1
    try:
        driver.get("https://jung-pro.ru/serii/jung-a-creation/")
        driver.SendKeys(driver.Selenium.Keys.Control + driver.Selenium.Keys.Shift + driver.Selenium.Keys.Return)
        items = driver.find_element(By.XPATH, f"(//a[@class='product-item__link'])[{k}]")
        items.click()
        time.sleep(1)
        pageSource = driver.page_source
        fileToWrite = open(f"page_source{k}.html", "w")
        fileToWrite.write(pageSource)
        fileToWrite.close()



    except Exception as ex:
        print(ex)
    finally:
        driver.close()
        driver.quit()

