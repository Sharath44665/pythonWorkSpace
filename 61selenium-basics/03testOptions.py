from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.proxy import Proxy
from selenium.webdriver.common.proxy import ProxyType


# see more in docs
def testPageLoadStrategyNormal():
    options = webdriver.FirefoxOptions()
    print(options)

    options.page_load_strategy="normal"
    driver = webdriver.Firefox(options=options)

    driver.get("https://www.selenium.dev/")
    driver.quit()

testPageLoadStrategyNormal()