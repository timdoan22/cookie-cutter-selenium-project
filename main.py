from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

COOKIE_URL = "https://orteil.dashnet.org/cookieclicker/"

DRIVER_PATH = "/Users/td/Development/chromedriver"
ser = Service(DRIVER_PATH)
driver = webdriver.Chrome(service=ser)
driver.maximize_window()

driver.get(COOKIE_URL)

five_minutes = time.time() + 60 * 5
four_seconds = time.time() + 4

big_cookie = driver.find_element(By.ID, "bigCookie")

while time.time() < five_minutes:
    big_cookie.click()

    golden_cookie = driver.find_element(By.ID, "shimmers").get_attribute("value")
    print(golden_cookie)
    if golden_cookie != None:
        golden_cookie.click()

    upgrades = driver.find_elements(By.CSS_SELECTOR, ".crate.upgrade.enabled")
    if upgrades:
        for upgrade in upgrades:
            upgrade.click()

    if time.time() > four_seconds:
        products_unlocked = driver.find_elements(By.CSS_SELECTOR, ".product.unlocked.enabled .price")

        num = 0
        highest_product = 0
        product_num = 0
        for product in products_unlocked:
            product_cost = int(product.text.replace(",", ""))
            if product_cost > highest_product:
                highest_product = product_cost
                product_num = num
            num += 1

        product_owned = driver.find_element(By.XPATH, f'//*[@id="productOwned{product_num}"]').text
        click_product = driver.find_element(By.ID, f"product{product_num}")

        if product_num == 1:
            grandmas_owned = driver.find_element(By.ID, "productOwned1").text
            if grandmas_owned != "":
                int_grandmas_owned = int(grandmas_owned)
                if int_grandmas_owned < 13:
                    driver.find_element(By.ID, "product1").click()

        if product_owned != "":
            int_product_owned = int(product_owned)

        if product_owned == "" or int_product_owned < 12:
            click_product.click()

        four_seconds = time.time() + 4

total_cookies = driver.find_element(By.ID, "cookies").text
print(total_cookies)
