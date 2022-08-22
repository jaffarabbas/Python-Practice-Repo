from selenium import webdriver


class LoadDriver:
    _browserDriver = "J:\Github\Python-Practice-Repo\Selenium Practice\selenium-integration\drivers\chromedriver.exe"
    _driver = None

    def loadDriver(self):
        print("Loading driver")
        self._driver = webdriver.Chrome(self._browserDriver)
        self._driver.maximize_window()

    def driverHandler(self):
        return self._driver

    def open(self, url):
        self._driver.get(url)

    def close(self):
        self._driver.close()
