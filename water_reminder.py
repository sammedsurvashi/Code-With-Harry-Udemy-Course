import time
from plyer import notification

while True:
    print("Please sip some water!")  
    notification.notify(
        title="Please drink some water",
        message="You need to drink some water"
    )
    time.sleep(60*60) 

#How It Works 

The script imports time for delay and notification to show desktop alerts.
It runs an infinite loop using while True.
Each loop prints a water reminder and shows a desktop notification.
Then the script pauses for 1 hour using time.sleep(60*60).
After the delay, it repeats again automatically.
