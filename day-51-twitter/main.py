from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
import datetime as dt
import pandas

CHROME_DRIVER_PATH = "c:\development\chromedriver.exe"
PROMISED_UPLOAD = 1.8       # Mbps
PROMISED_DOWNLOAD = 0.5     # Mbps

class InternetSpeedTwitterBot:
    def __init__(self):
        self.down = 0;
        self.up = 0
        self.driver = webdriver.Chrome(executable_path=CHROME_DRIVER_PATH)
        self.URL = "https://www.speedtest.net/"

    def get_internet_speed(self):
        self.driver.get(self.URL)
        cookie_consent = self.driver.find_element(By.CSS_SELECTOR, "button.evidon-barrier-acceptbutton")
        cookie_consent.click()
        go = self.driver.find_element(By.CSS_SELECTOR, "span.start-text")
        go.click()
        sleep(45)       # Give time from Download & Upload tests to run
        download_speed = self.driver.find_element(By.CSS_SELECTOR, "span.download-speed").text
        upload_speed = self.driver.find_element(By.CSS_SELECTOR, "span.upload-speed").text
        self.driver.quit()
        return download_speed, upload_speed

    def tweet_isp(self):
        pass


isp_bot = InternetSpeedTwitterBot()
down_up_speed = isp_bot.get_internet_speed()
timestamp = dt.datetime.now().strftime("%d-%b-%Y %H:%M")

speed_dict = {
    "Time": timestamp,
    "Download": float(down_up_speed[0]),
    "Upload": float(down_up_speed[1])
}
print(speed_dict)
df = pandas.DataFrame(speed_dict, index=[0])
df.to_csv("speed_history.csv", mode="a", index=False, header=False)

history = pandas.read_csv("speed_history.csv")
print(history)

