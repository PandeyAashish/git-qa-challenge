import utilities.custom_logger as cl
import logging
from base.basepage import BasePage


class ToolbarNav(BasePage):
    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    _issuelnk = "//span[contains(text(),'Issues')]"
    _i_create = "//a[@class='btn btn-primary']"

    def clickIssue(self):
        self.elementClick(locator=self._issuelnk, locatorType="xpath")

    def clickIssueButton(self):
        self.elementClick(locator=self._i_create, locatorType="xpath")
