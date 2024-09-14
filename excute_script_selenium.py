#window.open
#window.scrollBy(0,document.body.scrollHeight)

import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
driver= webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
time.sleep(3)
#driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")
#driver.execute_script("window.scrollBy(0,1500)")
#for adding new multiple windows
driver.execute_script("window.open('https://www.flipkart.com/')")
time.sleep(3)
driver.execute_script("window.open('https://www.facebook.com/')")
time.sleep(3)
driver.quit()