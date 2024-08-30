from selenium import webdriver
from selenium.webdriver.common.by import By
from pyvirtualdisplay import Display

# display = Display(visible=0, size=(800,800))
# display.start()

# keep driver open
chromeOptions = webdriver.ChromeOptions()
chromeOptions.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chromeOptions)

# driver.get(url="https://www.amazon.in")
driver.get(url="https://www.amazon.in/Reebok-Cypress-Running-Shoes-8-FW0366/dp/B082QJDRZV/?th=1&psc=1")
price = driver.find_element(By.CLASS_NAME, value="a-price-whole").text
print(price) # 2,034
print("do something")

driver.quit()
# display.stop()



