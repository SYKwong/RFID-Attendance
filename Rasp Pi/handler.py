#!/bin/python3

import sys
import gspread
import datetime
from oauth2client.service_account import ServiceAccountCredentials
from pprint import pprint
import serial
import time
import RPi.GPIO as GPIO

#for logging purpose
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
    fail = 0
    ser.close()
    ser.open()
    end = time.time() + 60*20
    while time.time() < end:
        line = ser.readline()
        linestr = str(line)
        linestr = linestr.strip(" 'b\\n\\r")
        if linestr == "Module failed to respond. Please check wiring.":
            # Reset the RFID reader if it outputs an error
             ser.close()
             ser.open()
             fail = 1
             if fail > 0:
                 GPIO.output(18, 0)
                 time.sleep(5)
                 GPIO.output(18, 1)
                 time.sleep(5)
        else:
            attendance.add(linestr)
            # Else just add the output to the attendance set

def update(classIndex):
    #Get the current date in MM/DD/YY
    date = datetime.datetime.today().strftime("%m/%d/%y")

    #Get the sheet
    classSheet = googleSheet.get_worksheet(classIndex)

    #Get the index for starting column
    offset = len(classSheet.row_values(1))+1

    #Add an extra column if the sheet is out of columns
    if offset>=26:
        classSheet.resize(None, offset)

    #Get the column with the students' EPC numbers
    enrollment = classSheet.col_values(2)
    #The first value from the column is "EPC number"
    enrollment.pop(0)

    #Update the value of the first cell from the starting column with the current date
    classSheet.update_cell(1,offset, date)

    #Check if student is present
    for student in attendance:
        if student in enrollment:
            studentIndex = enrollment.index(student)+2
            classSheet.update_cell(studentIndex, offset, "1")

if __name__ == '__main__':
    classIndex = int(sys.argv[1])

    rfid()
    GPIO.output(18, 0)

    update(classIndex)

    #for logging purpose
    print("end ", datetime.datetime.now())