import requests
from bs4 import BeautifulSoup
import math
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep


MAX_PRICE = 250000
FORM_URL = "https://docs.google.com/forms/d/e/1FAIpQLSd9GjlD7yshA-bSMCym-TAqjLOO2L-kQX1xneiCX7T9oh3zBA/viewform"
CHROME_DRIVER_PATH = "c:/development/chromedriver.exe"

address_list = []
link_list = []
price_list = []
num_pages = 1
current_page = 1
while current_page <= num_pages:
    if current_page != 1:
        page_num = f"page={current_page}&"
    else:
        page_num = ""
    URL = f"https://www.myhome.ie/residential/cork/detached-house-for-sale?{page_num}maxprice={MAX_PRICE}&minbeds=3"
    print(URL)
    html_content = requests.get(URL).text
    soup = BeautifulSoup(html_content, "html.parser")

    addresses = soup.select(".PropertyListingCard__Address")
    prices = soup.select(".PropertyListingCard__Price")
    num_results = int(soup.select_one(".SearchResults__Heading").getText().split(" - ")[1].split()[0])
    num_pages = math.ceil(num_results / 20)         # Round UP

    for addr, price in zip(addresses,prices):
        address_list.append(addr.getText().strip())
        link_list.append(f"https://www.myhome.ie/{addr.get('href')}")
        price_list.append(price.getText().strip())
    current_page += 1

print(len(address_list), len(link_list), len(price_list))
print(address_list, link_list, price_list)



for entry in range(len(address_list)):
    driver = webdriver.Chrome(executable_path=CHROME_DRIVER_PATH)
    driver.get(FORM_URL)

    address_field = driver.find_element(By.XPATH,
                                        '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div[2]/textarea')
    link_field = driver.find_element(By.XPATH,
                                     '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
    price_field = driver.find_element(By.XPATH,
                                      '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
    submit_button = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span/span')

    sleep(2)
    address_field.send_keys(address_list[entry])
    link_field.send_keys(link_list[entry])
    price_field.send_keys(price_list[entry])
    submit_button.click()


