"""import time



import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
driver=webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.implicitly_wait(5)
driver.find_element(By.XPATH,"//input[@type='search']").send_keys("cu")
driver.find_element(By.XPATH,"(//button[@class=''])[1]").click()
#time.sleep(3)
driver.find_element(By.XPATH,"//input[@type='search']").clear()
#time.sleep(3)
driver.find_element(By.XPATH,"//input[@type='search']").send_keys("po")
#time.sleep(3)
driver.find_element(By.XPATH,"(//button[@class=''])[1]").click()
#time.sleep(3)
driver.find_element(By.XPATH,"//img[@alt='Cart']").click()
#time.sleep(3)
driver.find_element(By.XPATH,"//button[text()='PROCEED TO
driver.close()"""


import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from webdriver_manager.chrome import ChromeDriverManager
driver=webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://rahulshettyacademy.com/dropdownsPractise/")

#driver.implicitly_wait(10)
#driver.find_element(By.XPATH,"//input[@id='autosuggest']").send_keys("Au")
#country_names= driver.find_elements(By.XPATH,"//ul/li[@class='ui-menu-item']")
#print(len(country_names))
#for value in country_names:
    #print(value.text)
wait=WebDriverWait(driver,10)
country_names=wait.until(EC.presence_of_all_elements_located((By.XPATH,"//ul/li[@class='ui-menu-item']")))
#print(len(country_names))
for value in country_names:
    print(value.text)
















































