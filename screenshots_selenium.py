#save_screenshot
#screeshot_as_file
#import base64



"""import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
driver=webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.save_screenshot("practice.jpg")
driver.close()
"""


"""import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
driver=webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://www.facebook.com/")
#driver.save_screenshot("C:\\Users\Kashi\Desktop\Screenshot_Selenium\deepmala.png")
#driver.get_screenshot_as_file("C:\\Users\Kashi\Desktop\Screenshot_Selenium\deepmala.pdf")
driver.close()
"""


"""import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import base64
driver=webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://www.facebook.com/")
screen_shot=driver.get_screenshot_as_base64()
with open("converttojpg.jpg","wb")as file:
    file.write(base64.b64decode(screen_shot))
print(screen_shot)"""

















