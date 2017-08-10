# Email
Python Script for Sending Email (using SMTP) with Attachments.

This python script is used to send emails to any number of people with attachment. You can change the file "credentials.py" to change the sender's password and email id. Email is send using a GMAIL account using SMTP library. Sender's account should have low security.(Disable the 2 way security for the sender account). Attachment can be pdf/txt/jpeg/png/mp4 file. 

Requirements:

1. Python 3.0 or newer versions  (Tested on Python 3.6)
2. smtplib3 library. (Use pip or easy_install)

Changes Required:

emailscript.py

1. Line 19. toaddr variable - Add recipient email id  
2. Line 25  Add subject here
3. Line 27  Add your Message Here
4. Line 31  Add file name here
5. Line 32  can change filename variable (it can work with only file name if file is present in same folder - else add path on line 32 and only file name in line 31)

credentials.py

1. Line 11  Add sender email id here 
2. Line 14  Add sender email password here


You can integrate this script in your app.
