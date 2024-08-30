from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()
driver.get("https://www.selenium.dev/selenium/web/web-form.html")

title = driver.title
print(title) # Web form
driver.implicitly_wait(0.5)

textBox = driver.find_element(by=By.NAME, value="my-text");
submitBtn = driver.find_element(by=By.CSS_SELECTOR, value="button")

textBox.send_keys("Selenium")
submitBtn.click()

msg = driver.find_element(by=By.ID, value="message")
text=msg.text

print(msg)
print(text) # Received!
driver.quit()