from time import sleep
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import wait
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from resources import CONNECTION_TIMEOUT, OOPS_MESSAGE, TIMEOUT, status_code, browser, CURRENTLY_IN_MEETING

def print_message(message, status):
    print(message , end=" ")
    if status == status_code.SUCCESS:
        print(u'\N{white heavy check mark}')
    elif status == status_code.LOADING:
        for i in range(2):
            print('.' , end ="")
            sleep(1)
            i+=1
        print('.')
    else:
        print(u'\N{cross mark}')


def wait_for_element_to_be_clickable(xpath, timeout = TIMEOUT):
    try:
        WebDriverWait(browser, timeout).until(EC.element_to_be_clickable((By.XPATH, xpath)))
    except TimeoutException:
        print_message(CONNECTION_TIMEOUT, status_code.FAILED)
    except:
        print_message(OOPS_MESSAGE, status_code.FAILED)

def get_current_participants():
    sleep(10)
    return int(browser.find_element_by_xpath(CURRENTLY_IN_MEETING).get_attribute('innerText')[1])
