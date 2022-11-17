#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'matteomadeddu'
__author__ = 'valentinarho'

##### GOOGLE CALENDAR CONFIGURATION

# Setup your Google email and password
EMAIL = 'gs.eng.ch@gmail.com'
PASS = 'dd464972006r2'

# Define the name for the calendar dedicated to Trello events and trello2google app.
# if the calendar not exists the app will create it for you!
CALENDAR_NAME = 'Trello Events'

##### TRELLO CONFIGURATION

# Application key and secret:
# Get it from this url: https://trello.com/1/appKey/generate
KEY = "4523bc8df66311fc00dc59e7b2a25713"
SECRET = "79abd55090ad424041e904980f34d9fb628fd98ff00bf27ca275c108711810b9"

# Get forever token from visiting this url (first complete the url with your API-KEY)
# https://trello.com/1/authorize?key=__YOUR-APP-KEY__&name=Trello2Google&expiration=never&response_type=token
FOREVER_TOKEN = "5a183388705c54223099018fef42aedb"

# Boards to convert
# On the left the board name, on the right the board id!
# Get your board id from Trello URL: https://trello.com/b/____BOARD-ID____/title-of-board
# Visit your board from a browser, and copy the ___BOARD-ID___ string.
BOARDS = {
    'Board One': '63544402a429e601aaf991b1',
}

BOARDS1 = {
    'Board One': '63544402a429e601aaf991b1',
    'Board Two': 'TODOffa426a6793f36001zzz',
}