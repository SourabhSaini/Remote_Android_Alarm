# Remote_Android_Alarm

This is Python 3.5 based Desktop Application with which user can set alarms/reminders remotely to any Smartphone (Tested on Android). The only requirement is that the mobile device should have 'Automate' : Android Application, installed and runnig in background.

How it works:
To set alarm remotely, this application uses free SMS service i.e Way2SMS. Entered Title, Note, Time and Repeat Days will be sent to the mobile phone in encrypted text via SMS. Automate application running on the mobile phone will decrypt the text and set alarm.

How to Set It Up:
1. Downloadd all the files and keep it in same folder.
2. You must have all required modules installed on your machne: tkinter.
3. Create Account on Way2SMS, if you don't have one.
4. Open 'remote_alarm.py' in edit mode and modify Line 139, 141, 142 accordingly.
5. Save and close it.
6. Install 'Automate' on your android device from Google PlayStore: https://play.google.com/store/apps/details?id=com.llamalab.automate&hl=en
7. Add '#SMS' to Automate Application : Download from https://www.dropbox.com/s/je8s4d9jqyszrk2/%23SMS.flo?dl=0
8. Start the Flow in Automate Application and you are good to go.

Run the application, by typing:
$ python3 [PATH_TO_FILE]/remote_alarm.py

Enter Data and click on Set Alarm. You will recieve a SMS on your mobile numbers which you have added in Line 139 of remote_alarm.py file. To check open alarm/clock application in your phone.

In case, you are facing and issue or getting anuy error message, please write to me : sourabh.saini08@gmail.com
