import time

from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

from browserLoader.loadDriver import LoadDriver


class LoginPom(LoadDriver):
    _driver = None
    _browserPath = "https://stage.outreach.sloovi.com/login"

    # locators

    _email = "email"
    _password = "password"
    _loginBtn = "//*[@id='main']/section/div[2]/form/div[2]/button"

    def __init__(self):
        self.loadDriver()
        self._driver = self.driverHandler()
        self.open(self._browserPath)

    def login(self, email, password):
        time.sleep(2)
        # fill email
        self._driver.find_element(By.NAME,self._email).send_keys(email)
        # fill password
        self._driver.find_element(By.NAME,self._password).send_keys(password)
        # click login button
        self._driver.find_element(By.XPATH,self._loginBtn).send_keys(Keys.ENTER)


    def get_dashboard_message(self, messageId,element):
        return self._driver.find_element(element,messageId).text

    def refresh(self):
        self._driver.refresh()
