import random

import utilities.custom_logger as cl
import logging
from base.basepage import BasePage


class CreateNewRepo(BasePage):
    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    _reponame = "//input[@id='repository_name']"
    _repodisc = "//input[@id='repository_description']"
    _create = "//button[@class='btn btn-primary first-in-line']"
    _setting = "//span[contains(text(),'Settings')]"
    _del_repo = "//summary[contains(text(),'Delete this repository')]"
    _pop_text = "//details-dialog[contains(@class,'Box Box--overlay d-flex flex-column anim-fade-in fast')]//p[2]//strong[1]"
    _pop_textbox = "//div[contains(@class,'Box-body overflow-auto')]//input[contains(@name,'verify')]"
    _cnfrm = "//button[contains(text(),'I understand the consequences, delete this reposit')]"
    _passwrd = "//input[@id='sudo_password']"
    _btn = "//button[@class='btn btn-block btn-primary']"

    def createRepo(self):
        self.sendKeys(locator=self._reponame, locatorType="xpath", data="git_demo" + str(random.randrange(1, 999878)))
        self.sendKeys(locator=self._repodisc, locatorType="xpath", data="git_demo_Desc")
        self.webScroll(direction="down")
        self.waitForElement(locator=self._create, locatorType="xpath")
        self.elementClick(locator=self._create, locatorType="xpath")

    def deleteRepo(self, password):
        self.elementClick(locator=self._setting, locatorType="xpath")
        self.webScroll(direction="down")
        self.elementClick(locator=self._del_repo, locatorType="xpath")
        txt = self.getText(locator=self._pop_text, locatorType="xpath")
        self.sendKeys(locator=self._pop_textbox, locatorType="xpath", data=txt)
        self.elementClick(locator=self._cnfrm, locatorType="xpath")
        ele = self.elementPresenceCheck(locator=self._passwrd, byType="xpath")
        if ele:
            self.sendKeys(locator=self._passwrd, locatorType="xpath", data=password)
            self.elementClick(locator=self._btn, locatorType="xpath")


