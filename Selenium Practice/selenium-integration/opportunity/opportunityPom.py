import time
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from login.loginPom import LoginPom

loginPom = LoginPom()


# pre rec - open browser and login
class OpportunityPom:
    _driver = None
    _browserPath = "https://stage.outreach.sloovi.com/lead/lead_7e0ce02cc9854ceeb61ea58bbae3f2b6"

    # locators
    _opportunityMainBtn = "//*[@id='main']/div/div/div[2]/div[2]/div/div[1]/div[3]/section/header/button"
    _estimatedClose = "//*[@id='main']/div/div/div[2]/div[2]/div/div[1]/div[3]/section/section/ul/li[1]/div[2]/form/div[2]/div/div/label/div/div/div/input"
    _slider = "//*[@id='main']/div/div/div[2]/div[2]/div/div[1]/div[3]/section/section/ul/li[1]/div[2]/form/div[3]/label/input"
    _value = "//*[@id='main']/div/div/div[2]/div[2]/div/div[1]/div[3]/section/section/ul/li[1]/div[2]/form/div[4]/label/div/input"
    _time = "//*[@id='main']/div/div/div[2]/div[2]/div/div[1]/div[3]/section/section/ul/li[1]/div[2]/form/div[5]/div/div/div/input"
    _contact = "//*[@id='main']/div/div/div[2]/div[2]/div/div[1]/div[3]/section/section/ul/li[1]/div[2]/form/div[6]/div/div/label/div/div/div/input"
    _user = "InputField__fieldContainer"
    _selectUser = "//*[@id='tippy-128']/div/div[1]/ul/li[2]"
    _textArea = "//*[@id='msg']"
    _save_btn = "//*[@id='main']/div/div/div[2]/div[2]/div/div[1]/div[3]/section/section/ul/li[1]/div[2]/form/div[9]/div/button[2]"

    def login(self):
        email = "smithwills1989@gmail.com"
        password = "12345678"
        loginPom.login(email, password)
        self._driver = loginPom.driverHandler()
        time.sleep(5)
        self._driver.get(self._browserPath)

    def createOpportunity(self, estimatedClose, slider, value, timeInsert, contact, textArea):
        self.login()
        self._driver.find_element(By.XPATH, self._opportunityMainBtn).send_keys(Keys.ENTER)
        self._driver.find_element(By.XPATH, self._estimatedClose).send_keys(estimatedClose)
        # self._driver.find_element(By.XPATH, self._slider).send_keys(slider)
        self._driver.find_element(By.XPATH, self._value).send_keys(value)
        self._driver.find_element(By.XPATH, self._time).send_keys(timeInsert)
        self._driver.find_element(By.XPATH, self._contact).send_keys(contact)
        # self._driver.find_element(By.CLASS_NAME, self._user).send_keys(Keys.ENTER)
        # time.sleep(2)
        # self._driver.find_element(By.XPATH, self._selectUser).send_keys(Keys.ENTER)
        self._driver.find_element(By.XPATH, self._textArea).send_keys(textArea)
        self._driver.find_element(By.XPATH, self._save_btn).send_keys(Keys.ENTER)

    def get_check_message(self, messageId, element):
        return self._driver.find_elements(element, messageId)[0].text

    def refresh(self):
        self._driver.refresh()
