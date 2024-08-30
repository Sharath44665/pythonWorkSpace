from selenium import webdriver
from selenium.webdriver.common.by import By

myDriver = webdriver.Chrome()
myDriver.get(url="https://www.python.org/")
myDriver.implicitly_wait(10)

searchBar = myDriver.find_element(By.ID, value="id-search-field")
searchBar.send_keys("selenium")

# getLink = myDriver.find_element(By.CSS_SELECTOR, value=".small-widget.jobs-widget.last a")
# print(getLink.text) # jobs.python.org
# print(getLink.get_attribute("href")) # https://jobs.python.org/

bugLink = myDriver.find_element(By.XPATH, value='//*[@id="site-map"]/div[2]/div/ul/li[3]/a')
print(bugLink.text)
# submitbutton = myDriver.find_element(By.ID, value="submit")
# submitbutton.click()



myDriver.quit()