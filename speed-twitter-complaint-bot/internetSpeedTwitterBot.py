import selenium.common
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time,pandas


class InternetSpeedTwitterBot:
    def __init__(self):
        self.myDriver = webdriver.Chrome()
        self.myDriver.implicitly_wait(20)
        csvData = pandas.read_csv("myToken.csv")

        self.email = csvData.iloc[0,0]
        self.password = csvData.iloc[0,1]


    def getInternetSpeed(self):
        self.myDriver.get(url="https://www.speedtest.net/")
        try:
            self.myDriver.find_element(By.ID, value="onetrust-accept-btn-handler").click()
        except selenium.common.NoSuchElementException:
            print("elementNotFound")
        self.myDriver.find_element(By.CSS_SELECTOR, value=".js-start-test.test-mode-multi").click()
        time.sleep(150)
        try:
            self.myDriver.find_element(By.PARTIAL_LINK_TEXT, value="Close").click()
        except selenium.common.NoSuchElementException:
            print("elementNotFound")

        downloadSpeed = self.myDriver.find_element(By.XPATH,
                                                   value="//span[starts-with(@data-download-status-value,'0')]").text
        uploadSpeed = self.myDriver.find_element(By.XPATH,
                                                 value="//span[starts-with(@data-upload-status-value,'0')]").text
        self.myDriver.quit()
        return [downloadSpeed, uploadSpeed]

    def tweetAtProvider(self):
        self.myDriver = webdriver.Chrome()
        self.myDriver.implicitly_wait(20)

        self.myDriver.get(url="https://twitter.com/")

        # login
        self.myDriver.find_element(By.LINK_TEXT, value="Sign in").click()
        self.myDriver.find_element(By.NAME, value="text").send_keys(self.email)
        self.myDriver.find_element(By.XPATH, value="//span[text()='Next']").click()
        self.myDriver.find_element(By.NAME, value="password").send_keys(self.password)
        self.myDriver.find_element(By.XPATH, value="//div[@data-testid='LoginForm_Login_Button']").click()

        # tweet at airtel:
        time.sleep(10)
        self.myDriver.find_element(By.XPATH, value="//input[@data-testid='SearchBox_Search_Input']").send_keys("Airtel")
        self.myDriver.find_element(By.XPATH, value="//input[@data-testid='SearchBox_Search_Input']").send_keys(
            Keys.ENTER)
        # click on people
        self.myDriver.find_element(By.LINK_TEXT, value="People").click()
        pass
