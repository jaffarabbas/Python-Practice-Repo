import time
import unittest

from selenium.webdriver.common.by import By

from login.loginPom import LoginPom


def loginSuite():
    suite = unittest.TestSuite()
    suite.addTest(TestLogin('test_negative_login'))
    suite.addTest(TestLogin('test_positive_login'))
    return suite

class TestLogin(unittest.TestCase):

    loginPom = LoginPom()

    def test_positive_login(self):
        email = "smithwills1989@gmail.com"
        password = "12345678"
        _dashboardMessagePath = "OrganizationDropdown_organizationName"
        dashboardMessage = "Saravanan Testing"

        self.loginPom.login(email, password)
        time.sleep(10)
        self.assertEqual(self.loginPom.get_dashboard_message(_dashboardMessagePath, By.CLASS_NAME), dashboardMessage)

    def test_negative_login(self):
        # test data
        email = ["asdas@adas.com", "smithwills1989@gmail.com"]
        password = ["12345678", "132123"]

        _dashboardMessagePath = "//*[@id='main']/section/div[2]/form/div[2]"
        dashboardMessage = ["The email address and password does not match.", "Validation error"]

        for i in range(len(email)):
            with self.subTest(i=i):
                self.loginPom.login(email[i], password[i])
                time.sleep(10)
                self.assertEqual(self.loginPom.get_dashboard_message(_dashboardMessagePath, By.XPATH),
                                 dashboardMessage[i])
                self.loginPom.refresh()
