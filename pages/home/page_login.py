import utilities.custom_logger as cl
import logging
from base.basepage import BasePage


class LoginPage(BasePage):
    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    _clksignin = "/html//header[@role='banner']/div/div[2]//a[@href='/login']"
    _user = "//input[@id='login_field']"
    _pass = "//input[@id='password']"
    _signin = "//input[@name='commit']"

    def logins(self, userid, password):
        self.elementClick(locator=self._clksignin, locatorType="xpath")
        self.sendKeys(locator=self._user, locatorType="xpath", data=userid)
        self.sendKeys(locator=self._pass, locatorType="xpath", data=password)
        self.elementClick(locator=self._signin, locatorType="xpath")
