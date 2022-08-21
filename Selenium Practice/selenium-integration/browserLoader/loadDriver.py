from selenium import webdriver


class LoadDriver:
    _browserDriver = "C:\Program Files (x86)\chromedriver.exe"
    _driver = None

    def __init__(self):
        self._driver = webdriver.Chrome(self._browserDriver)
        self._driver.maximize_window()

    def driverHandler(self):
        return self._driver

    def open(self, url):
        self._driver.get(url)
        return self._driver

    def quit(self):
        self._driver.quit()
        return self._driver
