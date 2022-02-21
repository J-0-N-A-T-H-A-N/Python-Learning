import requests
from bs4 import BeautifulSoup

CARDANO_URL = "https://www.coinbase.com/price/cardano"

html_response = requests.get(CARDANO_URL).text

soup = BeautifulSoup(html_response, "html.parser")
percent_buying = soup.find_all(name="div", class_="PercentBarBuying__Text-pn1f5a-2")
for item in percent_buying:
    print(item.getText())

print(soup.prettify())




