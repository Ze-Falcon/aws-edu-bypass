import os 
import schedule

def bypass_ses():
    os.system("python ./bypass.py")
    print("Starting 2-Hourly Bypass ..")
schedule.every(2.5).hours.do(bypass_ses)

while 1:
    schedule.run_pending()
