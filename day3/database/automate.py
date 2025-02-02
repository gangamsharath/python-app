import schedule
import time

def upload():
    print("upload started...........")

schedule.every(1).minute.do(upload)
schedule.every().monday.do(upload)

while True:
    schedule.run_pending()
    time.sleep(10)
    print("****")