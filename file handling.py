"""import time
from selenium import webdriver
from selenium.webdriver.common.by import By
driver=webdriver.Chrome()
driver.maximize_window()

driver.get("https://www.facebook.com/")
driver.find_element(By.XPATH,'//input[@type="text"]').send_keys(8827703396)
driver.find_element(By.XPATH,'//button[@name="login"]').send_keys("degtrhyhtf")
value=driver.find_element((By.CLASS_NAME,"_6lux"))
print(value.text)
time.sleep(3)
#driver.find_element(By.ID,"pass").send_keys("deepmalato")
#driver.find_element(By.NAME,"login").click()
#time.sleep(3)
driver.close()"""