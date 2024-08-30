from selenium import webdriver
from selenium.webdriver.common.by import By
import os

# https://www.selenium.dev/documentation/webdriver/elements/file_upload/

def testUploads():
    driver= setup()
    driver.get("https://the-internet.herokuapp.com/upload")

    # single dot. meaning currentWorking directory
    uploadFile = os.path.abspath(os.path.join(os.path.dirname(__file__), ".", "selenium_4_logo.png"))

    fileInput = driver.find_element(By.CSS_SELECTOR, value="input[type='file']")
    fileInput.send_keys(uploadFile)

    driver.find_element(By.ID, value="file-submit").click()

    fileName = driver.find_element(By.ID, value="uploaded-files").text

    assert fileName == "selenium_4_logo.png"

    tearDown(driver)
    pass

def setup():
    driver= webdriver.Firefox()
    return driver

def tearDown(driver):
    driver.quit()

testUploads()