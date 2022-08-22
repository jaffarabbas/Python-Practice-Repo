import time
import unittest
from selenium.webdriver.common.by import By
from lead.leadPom import LeadPom
from opportunity.opportunityPom import OpportunityPom


def opportunitySuite():
    suite = unittest.TestSuite()
    suite.addTest(TestOpportunity('test_positive_opportunity_creation'))
    return suite


class TestOpportunity(unittest.TestCase):

    estimateClose = "01/01/2020"
    slider = "100"
    value = 4000
    textField = "Test Lead"
    timeInsert = "Monthly"
    contact = "Saravanan"

    _checkMessage = "Task__description"
    _message = textField

    opportunityCreation = OpportunityPom()

    def test_positive_opportunity_creation(self):
        self.opportunityCreation.createOpportunity(self.estimateClose, self.slider, self.value,self.timeInsert, self.contact,self.textField)