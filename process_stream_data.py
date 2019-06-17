#!/usr/bin/env python 

import os 
import csv 
from twitter import *
import config 
import time 

api = Twitter(auth = OAuth(config.access_key,
                config.access_secret,
                config.consumer_key,
                config.consumer_secret))


# ---------------------------------------------
# Loop through all the /tmp .csv's 
# ---------------------------------------------
rootdir = '/home/pi/pybot-twitter/tmp'

path, dirs, files = next(os.walk(rootdir))
file_count = len(files)
print('Processing %d records..' % file_count)
time.sleep(1)

x = 0
for subdir, dirs, files in os.walk(rootdir):
    for file in files:
        x += 1
        print('%d of %d records completed' % (x, file_count))
        user = str(file)
        statuses = api.statuses.user_timeline(screen_name=user, count=200)

        for status in statuses:

            with open('/home/pi/pybot-twitter/filtered/%s.csv' %user, 'a+') as result:
                writer = csv.writer(result)
                writer.writerow([status['text'].encode('utf-8')])

        os.remove('/home/pi/pybot-twitter/tmp/%s' %file)
            