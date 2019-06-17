#!/usr/bin/env python

# -----------------------------------------------------
# Import our required modules 
# -----------------------------------------------------
import time 
import dateutil.parser 
from dateutil.relativedelta import * 
from datetime import * 
from termcolor import colored, cprint

# Activity flag text highlights
print_flag = lambda x: cprint(x, 'red', 'on_cyan')


class filterStream(object):

    # --------------------------------------------------
    # Our stream object
    # --------------------------------------------------
    def __init__(self, user, source, created_at, followers, friends, verified, statuses_count, location):
        self.user = user
        self.source = source 
        self.created_at = created_at
        self.followers = followers
        self.friends = friends
        self.verified = verified 
        self.statuses_count = statuses_count
        self.location = location

    # --------------------------------------------------
    # Function to check how long an account has
    # been created for. 
    # --------------------------------------------------
    def account_life(self, user, created_at):
        # Cleanup twitter API date
        created = dateutil.parser.parse(created_at)
        created = created.replace(tzinfo=None)

        # Count days in existence
        days_in_existence = (datetime.now() - created).days 

        # Check if account was made within last 90 days
        if days_in_existence < 90:
            print_flag('User account: @%s was created within last 90 days' % user)  
            
        return days_in_existence


    def tweets_per_day(self, days_alive, statuses_count):
        
        if days_alive == 0:
            days_alive = 1

        # Create our ratio 
        x = days_alive / days_alive
        y = statuses_count / days_alive 
        ratio = '%d:%d' % (x,y)

        if y > 100:
            cprint('Abnormal AL/T ratio of: ' + ratio, 'yellow', attrs=['bold']) 
            return True
        else:
            return False
