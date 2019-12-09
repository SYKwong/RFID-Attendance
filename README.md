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
- Upload > RFID.ino to the Arduino

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
- run the scheduler using
    ```
    python3 scheduler.py
    ```

**Google Sheet**
- Follow the steps to get the credentials for the Google sheet
    ```
    https://gspread.readthedocs.io/en/latest/oauth2.html
    ```

