import unittest

from lead.leadTestCases import leadSuite
from login.loginTestcases import loginSuite
from opportunity.opportunityTestCases import opportunitySuite


def main():
    runner = unittest.TextTestRunner()
    runner.run(loginSuite())
    runner.run(leadSuite())
    runner.run(opportunitySuite())


if __name__ == '__main__':
    main()
