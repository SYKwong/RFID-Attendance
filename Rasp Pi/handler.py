#!/bin/python3

import sys
import gspread
import datetime
from oauth2client.service_account import ServiceAccountCredentials
from pprint import pprint
import serial
import time
import RPi.GPIO as GPIO

print("start ", datetime.datetime.now())

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(18, GPIO.OUT)

ser = serial.Serial('/dev/ttyACM0', 115200)
ser.close()
ser.open()

scope = ["https://spreadsheets.google.com/feeds",'https://www.googleapis.com/auth/spreadsheets',"https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]
creds = ServiceAccountCredentials.from_json_keyfile_name("/home/pi/Desktop/ATTENDANCE/creds.json", scope)
client = gspread.authorize(creds)

googleSheet = client.open("ATTENDANCE")

attendance = set()

time.sleep(5)
GPIO.output(18, 1)
time.sleep(5)

def rfid():
    ser.close()
    ser.open()
    #print("start")
    end = time.time() + 60*20
    while time.time() < end:
        line = ser.readline()
        linestr = str(line)
        linestr = linestr.strip(" 'b\\n\\r")
        print(linestr)
        if linestr == "Module failed to respond. Please check wiring.":
             ser.close()
             ser.open()
             if linestr in attendance:
                 GPIO.output(18, 0)
                 time.sleep(5)
                 GPIO.output(18, 1)
                 time.sleep(5)
        else:
            attendance.add(linestr)
    #print("end")

def update(classIndex):
    date = datetime.datetime.today().strftime("%m/%d/%y")

    classSheet = googleSheet.get_worksheet(classIndex)
    offset = len(classSheet.row_values(1))+1
    if offset>=26:
        classSheet.resize(None, offset)
    enrollment = classSheet.col_values(2)
    enrollment.pop(0)

    classSheet.update_cell(1,offset, date)
    for student in attendance:
        if student in enrollment:
            studentIndex = enrollment.index(student)+2
            classSheet.update_cell(studentIndex, offset, "1")


def cleanup():
    #get rid of the extra stuff
    attendance.add("Module continuously reading. Asking it to stop...")
    attendance.add("Initializing...")
    attendance.add("")
    attendance.add("Searching for tag")

    attendance.remove("Initializing...")
    attendance.remove("Module continuously reading. Asking it to stop...")
    attendance.remove("")
    attendance.remove("Searching for tag")

if __name__ == '__main__':
    classIndex = int(sys.argv[1])

    rfid()
    cleanup()
    GPIO.output(18, 0)

    update(classIndex)
    print("end ", datetime.datetime.now())