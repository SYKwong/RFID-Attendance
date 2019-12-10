# RFID Attendance

# Set up

**Arduino**
- Follow Sparkfun's guide to apply thermal pad, and attach the external antenna
    ```
    https://learn.sparkfun.com/tutorials/simultaneous-rfid-tag-reader-hookup-guide/introduction
    ```
- Follow Sparkfun's instusction to install the Arduino library
    ```
    https://learn.sparkfun.com/tutorials/simultaneous-rfid-tag-reader-hookup-guide/using-the-arduino-library
    ```

**Raspberry Pi**
- We used Raspbian, but any Linux distro that is fully compatible with Raspberry Pi should work
- Download and follow the instruction for NOOBS/Raspbian, or other Linux distros of your choice
    ```
    https://www.raspberrypi.org/downloads/
    ```
- Install the required modules
    ```
    pip3 install --upgrade gspread
    pip3 install --upgrade oauth2client
    pip3 install --upgrade crontab
    ```
    
**Google Sheet**
- Follow the steps to get the credentials for the Google sheet
    ```
    https://gspread.readthedocs.io/en/latest/oauth2.html
    ```
- Change the credential file name to `creds.json`


**Running**
- Upload `RFID.ino` to the Arduino
- Make sure the following files are in `/home/pi/Desktop/ATTENDANCE/`
    ```
    creds.json
    handler.py
    scheduler.py
    ```
- Make sure the schedule is in the first sheet of the spreadsheet and in the format of
    ```
    Column 1    Column 2    Column 3    Column 4
    Class-Name  Class-Time  Meeting-Day Section
    ```
    - First row is unchecked
    - Class-Time needs to be in 24-hour format HH:MM
    - Meeting-Day uses NMTWRFS for
    ```
    suNday
    Monday
    Tuesday
    Wednesday
    thuRsday
    Friday
    Saturday
    ```
    - Section refers to the nth+1 sheet of the spreadsheet
- Open the terminal and run the schudler using 
    ```
    python3 /home/pi/Desktop/ATTENDANCE/scheduler.py
    ```

