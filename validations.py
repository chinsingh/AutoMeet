from resources import *


def login_failed():
    try:
        oops_page = browser.find_element_by_xpath(OOPS)
    except:
        oops_page = None
    finally:
        return bool(oops_page)
    
