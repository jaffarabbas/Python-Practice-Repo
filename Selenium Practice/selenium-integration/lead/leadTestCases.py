import time
import unittest
from selenium.webdriver.common.by import By
from lead.leadPom import LeadPom


def leadSuite():
    suite = unittest.TestSuite()
    suite.addTest(TestLead('test_positive_lead_creation'))
    return suite


class TestLead(unittest.TestCase):

    textField = "Test Lead"
    date = "01/01/2020"
    time = "12:00am"
    assignUser = "Sundar Pichai"

    _checkMessage = "Task__description"
    _message = textField

    leadCreation = LeadPom()

    def test_positive_lead_creation(self):
        self.leadCreation.createLead(self.textField, self.date, self.time, self.assignUser)
        time.sleep(3)
        self.assertEqual(self.leadCreation.get_check_message(self._checkMessage, By.CLASS_NAME), self._message)