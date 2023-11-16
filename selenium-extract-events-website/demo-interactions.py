from selenium import webdriver
from selenium.webdriver.common.by import By
import time

myDriver = webdriver.Chrome()
myDriver.get(url="http://secure-retreat-92358.herokuapp.com/")
myDriver.implicitly_wait(20)

myDriver.find_element(By.NAME, value="fName").send_keys("Sharath")
myDriver.find_element(By.NAME, value="lName").send_keys("C")
myDriver.find_element(By.NAME,value="email").send_keys("someone@example.com")
myDriver.find_element(By.XPATH, value="/html/body/form/button").click()

time.sleep(5)
myDriver.quit()

