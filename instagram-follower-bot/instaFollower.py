import selenium.common
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time,pandas

class InstaFollower:
    def __init__(self):
        self.myDriver = webdriver.Chrome()
        self.myDriver.implicitly_wait(20)
        csvData =pandas.read_csv("myPassword.csv")
        self.username = csvData.iloc[0,0]
        self.password = csvData.iloc[0,1]
        pass

    def login(self):
        self.myDriver.get(url="https://www.instagram.com/")
        self.myDriver.find_element(By.NAME, value="username").send_keys(self.username)
        self.myDriver.find_element(By.NAME,value="password").send_keys(self.password)
        self.myDriver.find_element(By.XPATH,value="//button[@type='submit']").click()
        self.myDriver.maximize_window()

        pass

    def findFollowers(self):
        # search for item
        try:
            self.myDriver.find_element(By.XPATH, value="//span[text()='Search']").click()
        except selenium.common.ElementNotInteractableException:
            self.myDriver.refresh()
            print("webservice refreshed")
            self.myDriver.find_element(By.XPATH, value="//span[text()='Search']").click()

        self.myDriver.find_element(By.XPATH, value="//input[@aria-label='Search input']").send_keys("instagram")
        time.sleep(10)
        self.myDriver.find_element(By.XPATH,value="//div[@class='x9f619 x1n2onr6 x1ja2u2z x78zum5 x1iyjqo2 xs83m0k xeuugli x1qughib x6s0dn4 x1a02dak x1q0g3np xdl72j9']//span[contains(text(),'instagram')]").click()
        time.sleep(10)

        pass

    def follow(self):
        # click on followers
        self.myDriver.find_element(By.XPATH,value="//a[@href='/instagram/followers/']").click()
        time.sleep(10)
        # unable to find this div
        targetDiv = self.myDriver.find_element(By.CLASS_NAME,value="")
        # scrolling
        actions = ActionChains(self.myDriver)
        actions.move_to_element(targetDiv).perform()
        # actions.move_to_element(targetDiv).scroll_to(targetDiv, 0, targetDiv.size['height']).perform()


        pass
