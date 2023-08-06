
from src.test23.tests.resources.custom_keywords import CustomKeywords
from src.test23.tests.constants.common_constants import CommonConstants
from src.test23.tests.pages.locators.nav_bar_locators import NavBarLocators

from src.test23.tests.pages.locators.sharebus_page_locators import SharebusPageLocators

class SharebusPage(CommonConstants, CustomKeywords, NavBarLocators, SharebusPageLocators): 

    def __init__(self):
        self.log(file_directory= self.LOG_FILE_PATH_LOCATION)

    def example_method(self):
        self.logger.warning("nav_locator: "+self.NAV_LOCATOR_TESTER)
        self.logger.warning("page_locator: "+self.PAGE_LOCATOR_TESTER)
        self.logger.warning("Page Found.")
