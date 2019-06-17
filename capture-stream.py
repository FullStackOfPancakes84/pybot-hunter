#!/usr/bin/env python 

# -------------------------------------------------------
# Load our API credentials 
# ------------------------------------------------------- 
import sys 
sys.path.append(".")
import config 

# -------------------------------------------------------
# Import our required modules 
# -------------------------------------------------------
from twitter import *
import csv 
from termcolor import colored, cprint

# -------------------------------------------------------
# Load our stream filters
# ------------------------------------------------------- 
import filter_stream as fs
import capture_data as capture 

# -------------------------------------------------------
# Create our streaming pybot API object 
# -------------------------------------------------------
auth = OAuth(config.access_key,
             config.access_secret,
             config.consumer_key,
             config.consumer_secret)
stream = TwitterStream(auth = auth, secure = True)


#-----------------------------------------------------------------------
# iterate over tweets matching this filter text
# IMPORTANT! this is not quite the same as a standard twitter search
#  - see https://dev.twitter.com/streaming/overview
#-----------------------------------------------------------------------
tweet_iter = stream.statuses.filter(track = config.terms)

for tweet in tweet_iter:
    #-----------------------------------------------------------------------
    # print out the contents, and any URLs found inside
    #-----------------------------------------------------------------------
    if 'text' in tweet:
        print("(%s) @%s %s" % (tweet["created_at"], tweet["user"]["screen_name"], tweet["text"]))
        for url in tweet["entities"]["urls"]:
            print(" - found URL: %s" % url["expanded_url"])

        # --------------------------------------------
        # Filter the stream for bot activity 
        # --------------------------------------------
        filtered = fs.filterStream(tweet['user']['screen_name'],
                                tweet['source'],
                                tweet['user']['created_at'],
                                tweet['user']['followers_count'],
                                tweet['user']['friends_count'],
                                tweet['user']['verified'],
                                tweet['user']['statuses_count'],
                                tweet['user']['location'])

        # --------------------------------------------------
        # Check if account was created within past 60 days
        # --------------------------------------------------
        days_alive = filtered.account_life(filtered.user,filtered.created_at)
    
        # --------------------------------------------------
        # Create our days_alive:tweets ratio 
        # --------------------------------------------------
        tweet_ratio = filtered.tweets_per_day(days_alive, filtered.statuses_count)

        if tweet_ratio is True:
            if days_alive < 90:
                # Store the screen name at ./tmp/screen_name
                capture.flag_activity(filtered.user)
            else:
                pass
        else:
            pass
    else:
        pass