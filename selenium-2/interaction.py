# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
# import time
#
# chrome_driver_path = "c:\development\chromedriver.exe"
# driver = webdriver.Chrome(executable_path=chrome_driver_path)

# URL = "https://en.wikipedia.org/wiki/Main_Page"
# driver.get(URL)
#
# article_count = driver.find_element(By.CSS_SELECTOR, "#articlecount a")
# print(article_count.text)
#
# all_portals = driver.find_element(By.LINK_TEXT, "All portals")
# # all_portals.click()
#
# search_bar = driver.find_element(By.NAME, "search")
# search_bar.send_keys("python")
# search_bar.send_keys(Keys.RETURN)                   # Keys import required
#


# URL = "http://secure-retreat-92358.herokuapp.com/"
# driver.get(URL)
#
# first_name_field = driver.find_element(By.NAME, "fName")
# last_name_field = driver.find_element(By.NAME, "lName")
# email_field = driver.find_element(By.NAME, "email")
# sign_up_button = driver.find_element(By.CSS_SELECTOR, "button")
#
# first_name_field.send_keys("Jonathan")
# last_name_field.send_keys("Garvin")
# email_field.send_keys("jonathan@hotmail.com")
# sign_up_button.click()


#### Automatically play the Cookie Clicker ####

from selenium import webdriver
from selenium.webdriver.common.by import By
import time

chrome_driver_path = "c:\development\chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

COOKIE_URL = "https://orteil.dashnet.org/cookieclicker/"
driver.get(COOKIE_URL)

cookie = driver.find_element(By.ID, "bigCookie")
upgrade_count = 0
product_count = 0
golden_cookie_count = 0
game_on = True
start_time = time.time()
while time.time() < start_time + 300:       # Total run time in seconds
    end_time = time.time() + 5              # number of seconds to run clicks for
    while time.time() < end_time:
        cookie.click()

    # golden_cookie = driver.find_element(By.CLASS_NAME, "goldenCookie")
    # golden_cookie_count += 1

    upgrades = driver.find_elements(By.CLASS_NAME, "crate.upgrade.enabled")
    if len(upgrades) > 0:
        upgrade = upgrades[len(upgrades) - 1]
        upgrade.click()
        upgrade_count += 1

    unlocked = driver.find_elements(By.CLASS_NAME, "product.unlocked.enabled")
    if len(unlocked) > 0:
        buy = unlocked[len(unlocked) - 1]
        buy.click()
        product_count += 1


cookies_per_second = driver.find_element(By.CSS_SELECTOR, "#cookies div")
print(f"Cookies {cookies_per_second.text}")

print(f"Upgrades: {upgrade_count}\t\tProducts: {product_count}")

driver.quit()
