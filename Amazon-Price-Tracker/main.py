from bs4 import BeautifulSoup
import requests
import lxml
import smtplib

SMTP_SERVER = "smtp.live.com"
FROM_EMAIL = "xxxxxxxxxxxxxxxxx"
PASSWORD = "xxxxxxxxxxxxxxxxxxxxx"

WATCH_PRICE = 45.00

PRODUCT_URL = "https://www.amazon.co.uk/all-new-blink-outdoor-wireless-weather-resistant-hd-security-camera-with-2-year-" \
      "battery-life-motion-detection-add-on-camera/dp/B088CWLN3C/ref=sr_1_1?crid=XB3QBH1ORO3T&keywords=blink+add+" \
      "on+camera&qid=1642605516&s=amazon-devices&sprefix=blink+add%2Camazon-devices%2C57&sr=1-1"

# Amazon expects some headers
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9"
}

response = requests.get(PRODUCT_URL, headers=headers)
response.raise_for_status()

html_content = response.text
soup = BeautifulSoup(html_content, "lxml")
product_title = soup.find(name="span", id="productTitle").getText().strip()
soup_price = soup.find(name="span", class_="a-offscreen").getText()
price = float(soup_price[1:])
currency = soup_price[0]

if price < WATCH_PRICE:
    with smtplib.SMTP(SMTP_SERVER) as connection:
        connection.starttls()
        connection.login(user=FROM_EMAIL, password=PASSWORD)
        connection.sendmail(from_addr=FROM_EMAIL,
                            to_addrs="jonathan_garvin@hotmail.com",
                            msg=f"Subject:Price Update\n\n\n{product_title}\n\n "
                                f"Currently on sale for {price}. You set a watch price of {WATCH_PRICE}")
        print(f"Current price {currency}{price} is under your watch price of {currency}{WATCH_PRICE}")
else:
    print(f"Current price {currency}{price} exceeds your watch price of {currency}{WATCH_PRICE}")
