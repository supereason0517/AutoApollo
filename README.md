CloudRiches-Apollo Attendance Checker
This Python script automates the attendance checking process for CloudRiches-Apollo using Playwright. It logs in to the system, checks if it's a working day, and then performs the necessary actions to record your attendance. If successful, it sends a notification to your LINE account. If there's an issue, it will notify you of the failure.

Prerequisites
Python 3.6 or above
Playwright library
pandas library
requests library
A valid LINE Notify token
Configuration file (config.py) with LINE token and user credentials
Installation
Install the required libraries:
bash
Copy code
pip install playwright pandas requests
Create a configuration file config.py with the following structure:
python
Copy code
# config.py

# LINE Notify token
Line = "your_line_notify_token"

# CloudRiches-Apollo credentials
User = "your_apollo_username"
Password = "your_apollo_password"
Replace "your_line_notify_token", "your_apollo_username", and "your_apollo_password" with your actual LINE Notify token and CloudRiches-Apollo credentials.

Prepare a CSV file date.csv containing information about working days. Ensure it has columns 西元日期 and 是否放假.
Usage
Run the script:

bash
Copy code
python attendance_checker.py
Features
Automatic login to CloudRiches-Apollo
Check if it's a working day using the provided CSV file
Record attendance by clicking the appropriate button based on the current time
Capture a screenshot of the attendance record for verification
Notifications
The script utilizes LINE Notify to send notifications. Make sure your LINE Notify token is valid and has the necessary permissions.

Notes
Ensure the script is executed in an environment with a graphical interface as Playwright uses a headless browser.
Regularly update the CSV file with working day information.
Feel free to customize the script to fit your specific needs!
