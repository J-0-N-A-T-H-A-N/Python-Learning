from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from bs4 import BeautifulSoup
import requests

chrome_driver_path = "c:/development/chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver_path)
URL = "https://www.obrienswine.ie/collections/red-wine?hitsPerPage=1000"
driver.get(URL)
sleep(2)
accept_cookies = driver.find_element(By.CSS_SELECTOR, "button#onetrust-accept-btn-handler")
accept_cookies.click()
wine_list = driver.find_elements(By.CSS_SELECTOR, "p.product-title")
price_list = driver.find_elements(By.CSS_SELECTOR, "p.product-price, p.product-discounted")
description_list = driver.find_elements(By.CSS_SELECTOR, "p.product-additional")
count = 0
for wine, price, descr in zip(wine_list, price_list, description_list):
    search_string = f"{wine.text} {descr.text}"

    vivino_url = f"https://www.vivino.com/search/wines?q={search_string}"

    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:66.0) Gecko/20100101 Firefox/66.0",
               "Accept-Encoding": "gzip, deflate",
               "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8", "DNT": "1",
               "Connection": "close", "Upgrade-Insecure-Requests": "1"}

    vivino_response = requests.get(vivino_url, headers=headers)
    vivino_response.raise_for_status()

    soup = BeautifulSoup(vivino_response.text, "html.parser")
    try:
        vivino_rating = soup.find(name="div", class_="average__number").text.strip()
    except AttributeError:
        vivino_rating = "n/a"

    with open("ratings.csv", "a") as ratings_file:
        ratings_file.write(f"{wine.text};{descr.text};{price.text};{vivino_rating}\n")

    count += 1
    if count % 40 == 0:
        print("Waiting....")
        sleep(600)

driver.quit()
