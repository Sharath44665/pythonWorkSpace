from selenium import  webdriver
from selenium.webdriver.common.by import By

def test_eight_components():
    driver = setup()

    title = driver.title
    assert title == "Web form"

    driver.implicitly_wait(0.5)

    textBox = driver.find_element(by=By.NAME, value="my-text")
    submitBtn = driver.find_element(by=By.CSS_SELECTOR, value="button")

    textBox.send_keys("Selenium")
    submitBtn.click()

    msg = driver.find_element(by=By.ID, value="message")
    value = msg.text

    assert value == "Received!"
    teardown(driver)

def setup():
    driver = webdriver.Firefox()
    driver.get("https://www.selenium.dev/selenium/web/web-form.html")
    return driver
def teardown(driver):
    driver.quit()

test_eight_components()