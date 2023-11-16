from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import Keys
import time
myDriver = webdriver.Chrome()
myDriver.implicitly_wait(20)
myDriver.get(url="https://en.wikipedia.org/wiki/Main_Page")

articleCountText = myDriver.find_element(By.XPATH, value='//*[@id="articlecount"]/a[1]').text
# print(articleCountText)

# myDriver.find_element(By.LINK_TEXT, value="Community portal").click()
myDriver.find_element(By.NAME,value="search").send_keys("Python")
myDriver.find_element(By.NAME,value="search").send_keys(Keys.ENTER)
time.sleep(2)
myDriver.quit()


