import random

import utilities.custom_logger as cl
import logging
from base.basepage import BasePage
from pages.home.page_toolbar_nav import ToolbarNav


class CreateNewIssue(BasePage):
    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    _title = "//input[@id='issue_title']"
    _i_body = "//textarea[@id='issue_body']"
    _sbmt = "//button[@class='btn btn-primary']"
    _i_text = "/html//a[@id='issue_1_link']"
    _issue_list = "//a[@id]"
    _iss = "/html[1]/body[1]/div[4]/div[1]/main[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/a[1]"
    _comntdesc = "//textarea[@id='new_comment_field']"
    _comntbtn = "//button[contains(text(),'Comment')]"
    _cnf = "// a[contains(text(), 'creating a new file')]"
    _repof = "//input[@placeholder='Name your file…']"
    _sbmtbtn = "//button[@id='submit-file']"
    _cde = "//span[contains(text(),'Code')]"
    _id = "//span[@class='gh-header-number']"
    _iss_title = "//span[@class='js-issue-title']"
    _cmntclk = "//a[@class='issue-link js-issue-link']"

    def crtIssue(self, title, desc):
        self.sendKeys(locator=self._title, locatorType="xpath", data=title)
        self.sendKeys(locator=self._i_body, locatorType="xpath", data=desc)
        self.elementClick(locator=self._sbmt, locatorType="xpath")

    def getPreIssue(self):
        text = self.getText(locatorType="xpath", locator=self._iss_title)
        ids = self.getText(locatorType="xpath", locator=self._id)
        return text + " " + ids

    def clkIssue(self):
        self.elementClick(locator=self._iss, locatorType="xpath")

    def comment(self, data=""):
        self.sendKeys(locator=self._comntdesc, locatorType="xpath", data=data)
        self.elementClick(locator=self._comntbtn, locatorType="xpath")

    def sendEmoji(self):
        self.elementClick(locator=self._cde, locatorType="xpath")
        self.elementClick(locator=self._cnf, locatorType="xpath")
        self.sendKeys(locator=self._repof, locatorType="xpath", data=":100:")
        self.webScroll(direction="down")
        self.elementClick(locator=self._sbmtbtn, locatorType="xpath")

    def issueListclk(self):
        self.elementClick(locator=self._i_text, locatorType="xpath")

    def cmntListclk(self):
        self.elementClick(locator=self._cmntclk, locatorType="xpath")
