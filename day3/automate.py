import schedule,time

def job():
    print("Schduled function")

schedule.every(1).seconds.do(job)


if __name__=='__main__':
    while True:
        schedule.run_pending()
        time.sleep(1)