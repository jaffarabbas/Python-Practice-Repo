import time

from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

from browserLoader.loadDriver import LoadDriver
from login.loginPom import LoginPom

loginPom = LoginPom()


# pre rec - open browser and login

class LeadPom:
    _driver = None
    _browserPath = "https://stage.outreach.sloovi.com/lead/lead_7e0ce02cc9854ceeb61ea58bbae3f2b6"

    # locators

    _leadMainBtn = "//*[@id='main']/div/div/div[2]/div[2]/div/div[1]/div[2]/section/header/button"
    _textField = "//*[@id=':r1:']"
    _date = "//*[@id=':r0:']"
    _time = "//*[@id='main']/div/div/div[2]/div[2]/div/div[1]/div[2]/section/section/ul/li[1]/div[2]/form/fieldset/ul/li[2]/div[1]/div/div/div[2]/div/input"
    _assignUser = "//*[@id='assigned_user']"
    _saveUserBtn = "//*[@id='main']/div/div/div[2]/div[2]/div/div[1]/div[2]/section/section/ul/li[1]/div[2]/form/div/button[2]"

    def login(self):
        email = "smithwills1989@gmail.com"
        password = "12345678"
        loginPom.login(email, password)
        self._driver = loginPom.driverHandler()
        time.sleep(5)
        self._driver.get(self._browserPath)

    def createLead(self, textField, date, timeInsert, assignUser):
        self.login()
        self._driver.find_element(By.XPATH, self._leadMainBtn).send_keys(Keys.ENTER)
        self._driver.find_element(By.XPATH, self._textField).send_keys(Keys.CONTROL + "a")
        self._driver.find_element(By.XPATH, self._textField).send_keys(Keys.DELETE)
        self._driver.find_element(By.XPATH, self._textField).send_keys(textField)
        self._driver.find_element(By.XPATH, self._date).send_keys(date)
        self._driver.find_element(By.XPATH, self._time).send_keys(timeInsert)
        self._driver.find_element(By.XPATH, self._assignUser).send_keys(assignUser)
        self._driver.find_element(By.XPATH, self._saveUserBtn).send_keys(Keys.ENTER)

    def get_check_message(self, messageId, element):
        return self._driver.find_elements(element, messageId)[0].text

    def refresh(self):
        self._driver.refresh()
