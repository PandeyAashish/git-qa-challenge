from base.selenium_driver import SeleniumDriver
from traceback import print_stack


class BasePage(SeleniumDriver):

    def __init__(self, driver):
        """
        Inits BasePage class

        Returns:
            None
        """
        super(BasePage, self).__init__(driver)
        self.driver = driver

    def verifyPageTitle(self, titleToVerify):
        pass
