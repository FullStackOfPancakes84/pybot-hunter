#!/usr/env/bin python 

# --------------------------------------------
# Import our required modules 
# --------------------------------------------
from twitter import *

import csv 
import config 
from termcolor import colored, cprint

api = Twitter(auth = OAuth(config.access_key,
                config.access_secret,
                config.consumer_key,
                config.consumer_secret))

# -------------------------------------------------
# Flag a user's screen_name for further processing
# to ./tmp/screen_name.csv
# -------------------------------------------------
def flag_activity(user):

    #statuses = api.statuses.user_timeline(screen_name=user, count=100)
    try:
        with open('./tmp/%s' % user, 'wb+') as f:
            writer = csv.writer(f)
            writer.writerow([user])
            cprint('User flagged for analysis at ./tmp/%s.csv' % user, 'green')
    except IOError:
        cprint('Error writing to ./tmp/%s.csv' % user, 'red', 'on_grey')