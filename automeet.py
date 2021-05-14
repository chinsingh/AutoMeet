from socket import timeout
from selenium import webdriver
from time import sleep
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options

from resources import *

###############################################################
###################      Functions      #######################
###############################################################

def set_options(): 
    options = Options()
    options.add_argument("--disable-infobars")
    options.add_argument("start-maximized")
    options.add_argument("--disable-extensions")
    # Pass the argument 1 to allow and 2 to block
    options.add_experimental_option("prefs", {"profile.default_content_setting_values.media_stream_mic": 1,
                                      "profile.default_content_setting_values.media_stream_camera": 1,
                                      "profile.default_content_setting_values.notifications": 1
                                      })
    return options


def login():
    chrome.find_element_by_xpath(EMAIL_FIELD).send_keys(EMAIL_ID) 
    chrome.find_element_by_xpath(NEXT_BUTTON).click()  
    sleep(30)


def is_logged_in():
    try:
        loaded_element = chrome.find_element_by_xpath(MEET_NOW_BUTTON) #Checks if login was successful by looking for an element that only shows when logged in -- 'Meet Now' button in this case
    #except:
    #   loaded_element = {}        
    #else:
    #   return bool(loaded_element)
    finally:
        return bool(loaded_element)


def keep_finding(xpath, timeout):
    for i in range(timeout):
        try:
           element = chrome.find_element_by_xpath(xpath) 
        except:    
            sleep(1)
            i+=1
        else:
            return element 


def join_meeting():
    camera_button = chrome.find_element_by_xpath(CAMERA_BUTTON)
    mic_button = chrome.find_element_by_xpath(MIC_BUTTON)
    if camera_button.get_attribute('aria-pressed') == 'true':  
        camera_button.click()
    if mic_button.get_attribute('aria-pressed') == 'true':  
        mic_button.click()
    chrome.find_element_by_xpath(PREJOIN_JOIN_BUTTON).click()


##############################################################################
####################         Script          #################################
##############################################################################


chrome = webdriver.Chrome(ChromeDriverManager().install() , options = set_options())
chrome.get(TEAMS_CALENDAR_URL)
sleep(20)
login()

while ~is_logged_in():
     chrome.refresh()
     sleep(20)


keep_finding(JOIN_BUTTON, 30).click()
sleep(5)
join_meeting()





    




