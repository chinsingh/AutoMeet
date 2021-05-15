from resources import *
from actions import *


#Login
browser.get(TEAMS_CALENDAR_URL)
print_message('Login page loaded', status_code.SUCCESS)
login()

#Join Meeting
print_message('Looking for a meeting to join', status_code.LOADING)
keep_finding(JOIN_BUTTON, 60).click()
sleep(5)
join_meeting()

#Keep track of participants and leave
leave_meeting()




    




