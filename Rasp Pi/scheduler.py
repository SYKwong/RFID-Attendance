import gspread
import datetime
import oauth2client
from oauth2client.service_account import ServiceAccountCredentials
from pprint import pprint
from crontab import CronTab
import sys
import subprocess

# log into google sheet
scope = ["https://spreadsheets.google.com/feeds",'https://www.googleapis.com/auth/spreadsheets',"https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]
creds = ServiceAccountCredentials.from_json_keyfile_name("creds.json", scope)
client = gspread.authorize(creds)

enrollment_sheet = client.open("ATTENDANCE").get_worksheet(0)
classTime = enrollment_sheet.col_values(2)
meetingDay = enrollment_sheet.col_values(3)
section = enrollment_sheet.col_values(4)

# Remove the reference cell
classTime.pop(0)
meetingDay.pop(0)
section.pop(0)

#M1 T2 W3 R4 F5 S6 N0
dic = {"M":1, "T":2, "W":3, "R":4, "F":5, "S":6, "N":0}
m = 0

cron = CronTab(user='pi')
cron.remove_all()

#grab one an element of meetingDay and classTime and translate into a format that crontab likes

while m < len(meetingDay):
    x = meetingDay[m]
    y = classTime[m]
    z = section[m]

    #takes apart one of the dow into separate parts and replcaes it with 1-7
    #separates entry w/ multiple dow into a list of multiple dow
    dow = [str(d) for d in str(x)]
    #replace dow w/ numbers
    dayOfWeek = [dic.get(n,n) for n in dow]
    dayOfWeekStr = ','.join(map(str,dayOfWeek))

    #takes apart time into minute and hour
    meetingTimes = [str(d) for d in str(y)]
    meetingTimes.remove(":")
    hrs = meetingTimes[0:-1-1]
    mins = [meetingTimes[-2],meetingTimes[-1]]
    #we start reading 10min before class
    minute = int(''.join(mins))-10
    hour = int(''.join(hrs))

    if minute < 0:
        minute += 60
        hour -= 1

    comm = sys.executable + ' /home/pi/Desktop/ATTENDANCE/handler.py '+ z + ' >> /home/pi/Desktop/ATTENDANCE/cron.log 2>&1'

    job1 = cron.new(comm)

    job1.setall(minute, hour, '*', '*', dayOfWeekStr)
    cron.write()
    m += 1

subprocess.run(["crontab", "-l"])