#!/usr/bin/env python
import subprocess
import os 
import sys 

print('Processing suspicious account activity. This could take a few minutes..')
subprocess.call("sshpass -p raspberry ssh pi@192.168.0.228 'cd ~ && python pybot-twitter/process_stream_data.py'", shell=True)

