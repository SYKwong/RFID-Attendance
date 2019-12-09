# Set up

Arduino/RFID
- Follow Sparkfun's guide to apply thermal pad, and attach the external antenna
https://learn.sparkfun.com/tutorials/simultaneous-rfid-tag-reader-hookup-guide/introduction
- Follow Sparkfun's instusction to install the Arduino library
https://learn.sparkfun.com/tutorials/simultaneous-rfid-tag-reader-hookup-guide/using-the-arduino-library

Raspberry Pi
- We used Raspbian, but any Linux distro that is fully compatible with Raspberry Pi should work
- Download and follow the instruction for NOOBS/Raspbian
https://www.raspberrypi.org/downloads/
- Install the required modules
    ` pip3 install gspread \n` 
    ` pip3 install oauth2client`
    ` pip3 install crontab`

- run the schedule using > python3 scheduler.py

