import json

#XPaths
JOIN_BUTTON = '//button[@title="Join"]'
EMAIL_FIELD = '//*[@id="i0116"]'
NEXT_BUTTON = '//*[@id="idSIButton9"]'
MEET_NOW_BUTTON = '//*[@id="id__19"]'
CAMERA_BUTTON = '//*[@title="Turn camera off"]'
MIC_BUTTON = '//*[@title="Mute microphone"]'
PREJOIN_JOIN_BUTTON = '//button[@data-tid="prejoin-join-button"]'

#Other Constants
TEAMS_CALENDAR_URL = 'https://teams.microsoft.com/_?lm=deeplink&lmsrc=homePageWeb&cmpid=WebSignIn#/calendarv2' 
EMAIL_ID = 'chinmay.singh@sap.com' #Settings JSON

#Data from Settings
data = json.load(open('settings.json'))

EMAIL_ID = data['email_id']