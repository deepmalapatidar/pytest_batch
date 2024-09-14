"""import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
driver= webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.maximize_window()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.find_element(By.NAME,"enter-name").send_keys("kashi")
driver.find_element(By.ID,"alertbtn").click()
time.sleep(3)
#driver.find_element(By.ID,"confirmbtn").click()
#time.sleep(3)
text_of_alert=driver.switch_to.alert.text
driver.switch_to.alert.accept()
time.sleep(3)
assert "kashi" in text_of_alert
print(text_of_alert)
"""
import time,
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.select import Select
from webdriver_manager.chrome import ChromeDriverManager
driver=webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
time.sleep(3)
dropdown=Select(driver.find_element(By.ID,"dropdown-class-example"))
#dropdown.select_by_value("option3")
#dropdown.select_by_index(2)
#driver.find_element(By.XPATH,"//input[@id='autocomplete']").send_keys("ind")
country_list=driver.find_element(By.CLASS_NAME,"ui-menu-item-wrapper")
for country in country_list:
    print(country.text)
time.sleep(3)
#print(len(country_list))
driver.close()

































