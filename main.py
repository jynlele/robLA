# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
from apscheduler.schedulers.blocking import BlockingScheduler

from la_rob import *

if __name__ == '__main__':
    try:
        scheduler = BlockingScheduler()
        # scheduler.add_job(sayHello, 'cron', day_of_week='0-6', hour=19, minute=50)
        #  arg time(hr) bool is weekend
        scheduler.add_job(rob, 'cron', day_of_week='thu', hour=21, minute=24, args=["10", 1])
        scheduler.add_job(rob, 'cron', day_of_week='fri', hour=19, minute=0, args=["10", 1])
        scheduler.add_job(rob, 'cron', day_of_week='mon-wed', hour=21, minute=0, args=["9", 0])
        scheduler.add_job(rob, 'cron', day_of_week='sat-sun', hour=16, minute=0, args=["9", 0])

        scheduler.start()
        # rob("9", 0)
    except:
        print("Something went wrong")

# See PyCharm help at https://www.jetbrains.com/help/pycharm/