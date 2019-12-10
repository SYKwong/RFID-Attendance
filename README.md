# RFID Attendance

# Set up

**Arduino**
- Follow [Sparkfun's guide](https://learn.sparkfun.com/tutorials/simultaneous-rfid-tag-reader-hookup-guide/introduction) to apply thermal pad, and attach the external antenna
    
- Follow [Sparkfun's instruction](https://learn.sparkfun.com/tutorials/simultaneous-rfid-tag-reader-hookup-guide/using-the-arduino-library) to install the Arduino library

- The code is a modified version of the example code from the [SparkFun Simultaneous RFID Tag Reader Library](https://github.com/sparkfun/SparkFun_Simultaneous_RFID_Tag_Reader_Library)


**Raspberry Pi**
- We used Raspbian, but any Linux distro that is fully compatible with Raspberry Pi should work
- Download and follow the instruction for [NOOBS/Raspbian](https://www.raspberrypi.org/downloads/), or other fully compatible Linux distros of your choice
- Install the required modules
    ```
    pip3 install --upgrade gspread
    pip3 install --upgrade oauth2client
    pip3 install --upgrade crontab
    ```
    
**Google Sheet**
- Follow the steps to get the [credentials for the Google sheet](https://gspread.readthedocs.io/en/latest/oauth2.html)
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
    - *First row* is unchecked
    - *Class-Time* needs to be in 24-hour format HH:MM
    - *Meeting-Day* uses NMTWRFS for
    ```
    suNday
    Monday
    Tuesday
    Wednesday
    thuRsday
    Friday
    Saturday
    ```
    - *Section* refers to the nth+1 sheet of the spreadsheet
- Open the terminal and run the schudler using 
    ```
    python3 /home/pi/Desktop/ATTENDANCE/scheduler.py
    ```

**Case**
![Box](https://github.com/SYKwong/RFID-Attendance/blob/master/Case/box%20screenshot.png)
Arduino and Reader sits at the bottom and the Pi sits above. The larger hole is where the fan is mounted inside the structure and blows in. The dimensions are 65.75mm wide, 71.25mm tall, and 127mm long. 

- An example of how all the pieces would fit together inside. The Solidworks models and files for the devices were borrowed from online sources. This does not include the RFID Tag Reader shield attached to the Arduino, however we took many measurements to ensure that there would be enough room for the reader the jumper cables coming out of the shield. 
Files containing the CAD designs of the Raspberry Pi 4, the Arduino UNO R3, and the 60mm fan: 
    - [Raspberry Pi 4](https://grabcad.com/library/raspberry-pi-4-model-b-1) 
    - [Arduino](https://my.solidworks.com/asset/3f1ffe37-e6ff-4405-ba55-ce50e84128bf)
    - [60mm fan](https://grabcad.com/library/cooling-fan-60x60x25-1)