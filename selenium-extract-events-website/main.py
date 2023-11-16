from selenium import webdriver
from selenium.webdriver.common.by import By

myDriver = webdriver.Chrome()
myDriver.implicitly_wait(20)
myDriver.get(url="https://www.python.org/")

# click on User Group Events
myDriver.find_element(By.XPATH, value='//*[@id="container"]/li[7]/ul/li[2]/a').click()

eventNames = myDriver.find_elements(By.CSS_SELECTOR, value=".list-recent-events.menu li h3 a")
times = myDriver.find_elements(By.CSS_SELECTOR,value=".list-recent-events.menu li p time")
# for val in eventNames:
#     print(val.text)
result = {}
for idx in range(len(eventNames)):
    result[idx] = {"time": times[idx].text,
                   "name": eventNames[idx].text}

print(result)


myDriver.quit()


