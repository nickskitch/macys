__author__ = 'Nick'
import os
import subprocess
import time
from datetime import datetime, timedelta



timeStart = "05:00"
timeEnd =   "08:00"

times = ("0500", "0600", "0700", "0800")
depart = []


    #cmd1 = "curl -s 'http://www.bart.gov/schedules/bystationresults?station=MONT&date=today&time=7%3A30%20PM' | grep Millbrae | awk '{gsub(/<[^>]+>/,\"\");print $1}'"

#7%3A30%20PM

for t in times:
    cmd2 = "curl -s 'http://www.bart.gov/schedules/bystationresults?station=MONT&date=today&time=" + t + "' | grep Millbrae | awk '{gsub(/<[^>]+>/,\"\");print $1}'"
    depart.append(subprocess.Popen(cmd2, shell=True, stdout=subprocess.PIPE).stdout.read().rstrip())

for d in depart:
    print(d)

while True:
    #time.sleep(60)  # Delay for 1 minute (60 seconds)
    tm = datetime.now() + timedelta(minutes=7)
    for d in depart:
        if d < (datetime.now() + timedelta(minutes=7)):
            print "test"

#terminal-notifier -message "Train leaves in 6 minutes at 5pm" -title "BART Alert"
