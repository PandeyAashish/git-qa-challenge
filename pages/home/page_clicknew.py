import utilities.custom_logger as cl
import logging
from base.basepage import BasePage


class ClickNewRepo(BasePage):
    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    _new = "//aside//h2[contains(text(),'Repositories')]//a[1]//*[local-name()='svg']"

    def clickNew(self):
        self.elementClick(locator=self._new, locatorType="xpath")
