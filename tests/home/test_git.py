import logging
import random
import time
from pages.home.page_clicknew import ClickNewRepo
from pages.home.page_login import LoginPage
from pages.home.page_newissue import CreateNewIssue
from pages.home.page_repo import CreateNewRepo
from pages.home.page_toolbar_nav import ToolbarNav
import unittest
import pytest
from ddt import ddt, data, unpack
import utilities.custom_logger as cl
from utilities.read_data import getCSVData

TEXT = ""


@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
@ddt
class GitPageTests(unittest.TestCase):
    log = cl.customLogger(logging.DEBUG)

    @pytest.fixture(autouse=True)
    def objectSetup(self, oneTimeSetUp):
        self.login = LoginPage(self.driver)
        self.nr = ClickNewRepo(self.driver)
        self.cr = CreateNewRepo(self.driver)
        self.cn = CreateNewIssue(self.driver)
        self.tn = ToolbarNav(self.driver)

    @pytest.mark.run(order=1)
    @data(*getCSVData("testdata.csv"))
    @unpack
    def test_challange1(self, user_id, password):
        self.login.logins(userid=user_id, password=password)
        self.nr.clickNew()
        self.cr.createRepo()

    @pytest.mark.run(order=2)
    def test_challenge2(self):
        global TEXT
        self.tn.clickIssue()
        self.tn.clickIssueButton()
        self.cn.crtIssue(title="git_title" + str(random.randrange(1, 999878)),
                         desc="git_desc" + str(random.randrange(1, 987899)))
        TEXT = self.cn.getPreIssue()
        self.cn.clkIssue()
        self.cn.crtIssue(title=TEXT[:-3], desc=TEXT[:-3])

    @pytest.mark.run(order=3)
    def test_challenge3(self):
        self.cn.comment(data="Entering Comments")
        self.cn.sendEmoji()

    @pytest.mark.run(order=4)
    def test_challenge4(self):
        time.sleep(2)
        self.tn.clickIssue()
        self.cn.issueListclk()
        self.cn.comment(data=TEXT)
        self.cn.cmntListclk()

    @pytest.mark.run(order=5)
    @data(*getCSVData("testdata.csv"))
    @unpack
    def test_challenge5(self, user_id, password):
        self.cr.deleteRepo(password=password)
