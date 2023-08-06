
from abc import ABC

class SoftwareitesPageLocators(ABC):
    skiptocontent_title: str = "Skip to content"
    mainmenu_type: str = "button"
    accept_id: str = "cookie_action_close_header"
    close_id: str = "cliModalClose"
    saveaccept_id: str = "wt-cli-privacy-save-btn"

    PAGE_LOCATOR_TESTER = "Page locator found."
    '''This constsant is for connectivity test only  [BS23]'''