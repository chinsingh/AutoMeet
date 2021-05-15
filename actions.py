from datetime import datetime
from validations import login_failed
from resources import *
from time import sleep
from utility import print_message, wait_for_element_to_be_clickable, get_current_participants


def try_again():
    print_message('Trying again', status_code.LOADING)
    browser.find_element_by_xpath(TRY_AGAIN_BUTTON).click()
    wait_for_element_to_be_clickable(NEW_MEETING_BUTTON)
    

def login():
    print_message('Logging in', status_code.LOADING)
    wait_for_element_to_be_clickable(EMAIL_FIELD, 10)
    browser.find_element_by_xpath(EMAIL_FIELD).send_keys(EMAIL_ID) 
    wait_for_element_to_be_clickable(NEXT_BUTTON, 10)
    browser.find_element_by_xpath(NEXT_BUTTON).click()  
    wait_for_element_to_be_clickable(NEW_MEETING_BUTTON)
    print_message(LOGIN_SUCCESSFUL, status_code.SUCCESS)
    if login_failed():
        print_message(LOGIN_FAILED, status_code.FAILED)
        try_again()
    


def keep_finding(xpath, interval):
    element_not_found = True
    while element_not_found:
        try:
            element = browser.find_element_by_xpath(xpath) 
            element_not_found = False
        except:    
            sleep(interval)
        else:
            return element 


def join_meeting():
    print_message('Time to meet. Joining', status_code.LOADING)
    
    try:
        camera_button = browser.find_element_by_xpath(CAMERA_BUTTON)
        camera_button.click()
    finally:
        print_message('Camera off', status_code.SUCCESS)  
  
    try:
        mic_button = browser.find_element_by_xpath(MIC_BUTTON)  
        mic_button.click()
    finally:
        print_message('Microphone off', status_code.SUCCESS)
    
    browser.find_element_by_xpath(PREJOIN_JOIN_BUTTON).click()
    print_message('Connecting', status_code.LOADING)
    wait_for_element_to_be_clickable(HANGUP_BUTTON)
    print_message('Joined meeting', status_code.SUCCESS)
    

def leave_meeting():
    browser.execute_script("document.getElementById('roster-button').click()")
    while get_current_participants() > MINIMUM_PARTICIPANTS:
        sleep(60)
    print_message('Leaving', status_code.LOADING)
    browser.execute_script("document.getElementById('hangup-button').click()")
    print_message('Left Meeting at %d' , datetime.now())


          
