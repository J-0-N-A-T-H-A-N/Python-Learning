from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_driver_path = "c:\development\chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

URL = "https://python.org"

driver.get(URL)

event_dates = driver.find_elements(By.CSS_SELECTOR, ".event-widget time")
events = driver.find_elements(By.CSS_SELECTOR, ".event-widget li a")

event_dict = {event_dates.index(date): {"time": date.text, "event": event.text} for date, event in zip(event_dates, events)}
print(event_dict)

driver.quit()       # quit closes the browser, close() will close the tab.
