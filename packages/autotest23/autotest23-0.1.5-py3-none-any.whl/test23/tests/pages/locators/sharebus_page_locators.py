
from abc import ABC

class SharebusPageLocators(ABC):

    en_id: str = "navbarScrollingDropdown"
    signin_xpath: str = "//body/div[1]/nav/div/ul/li[2]/a"
    search_for_destinations__festivals_or_events__id: str = ""
    _id: str = "0"
    termsandconditions_xpath: str = "//body/div[1]/div[3]/footer/div[1]/ul/li[1]/a"
    aboutsharebus_xpath: str = "//body/div[1]/div[3]/footer/div[1]/ul/li[2]/a"
    aboutferdia_xpath: str = "//body/div[1]/div[3]/footer/div[1]/ul/li[3]/a"
    help_xpath: str = "//body/div[1]/div[3]/footer/div[1]/ul/li[4]/a"
    acceptcookies_type: str = "button"
    reject_type: str = "button"

    PAGE_LOCATOR_TESTER = "Page locator found."
    '''This constsant is for connectivity test only  [BS23]'''