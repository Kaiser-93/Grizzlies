from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time

service_obj = Service('./chromedriver')
driver = webdriver.Chrome(service=service_obj)
url = "https://www.google.com"
driver.get(url)
time.sleep(3)
driver.close()