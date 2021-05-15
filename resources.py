import toml
import enum
from driver_factory import get_driver


#Important determinations and constants
browser = get_driver()  
TEAMS_CALENDAR_URL = 'https://teams.microsoft.com/_?lm=deeplink&lmsrc=homePageWeb&cmpid=WebSignIn#/calendarv2' 

#XPaths
JOIN_BUTTON = '//button[@title="Join"]'
EMAIL_FIELD = '//*[@id="i0116"]'
NEXT_BUTTON = '//*[@id="idSIButton9"]'
NEW_MEETING_BUTTON = '//button[@id="header_new_meeting_button"]'
CAMERA_BUTTON = '//*[@title="Turn camera off"]'
MIC_BUTTON = '//*[@title="Mute microphone"]'
PREJOIN_JOIN_BUTTON = '//button[@data-tid="prejoin-join-button"]'
OOPS = '//*[@class=oops]'
TRY_AGAIN_BUTTON = '//button[@translate-once="tryAgain"]'
PARTICIPANTS_BUTTON = '//button[@id="roster-button"]'
CURRENTLY_IN_MEETING = '//*[@id="page-content-wrapper"]/div[1]/div/calling-screen/div/div[2]/meeting-panel-components/calling-roster/div/div[4]/div/div[1]/accordion/div/accordion-section[2]/div/calling-roster-section/div/div[1]/button/span[3]'
# '//*[@ng-if="::ctrl.enableRosterParticipantsLimit"]'
HANGUP_BUTTON = '//button[@id="hangup-button"]'


#Messages
OOPS_MESSAGE = 'Something went wrong. Please run the script again'
LOGIN_SUCCESSFUL = 'Login Successful!'
LOGIN_FAILED = 'Oops! Login Failed.'
CONNECTION_TIMEOUT = """Connection took too much time. Script may still work, its just wasn't able too verify the connection because it took long to respond.
                        Here's what you can do, if it doesn't work:
                            1. Try running the script again. If your internet works slightly faster this time, this should work.
                            2. If the above solution doesn't work. Try increasing timeout in advanced settings and run the script again."""

#Status for messages
class status_code(enum.Enum):
    SUCCESS = 1
    LOADING = 2
    FAILED = 3 


#Data from Settings
data = toml.load(open('settings.toml'))

EMAIL_ID = data['email_id']
MINIMUM_PARTICIPANTS = data['minimum_participants']
TIMEOUT = data['timeout']
