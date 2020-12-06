from cmath import e
from threading import Timer
import time
import datetime
from datetime import datetime

from selenium import webdriver


def rob(time_index, is_weekend):
    try:
        current_time = datetime.now()
        print("time: ", current_time)
        print("time range: ", time_index)
        print("is weekend: ", is_weekend)
        path = "/usr/local/bin/chromedriver"
        driver = webdriver.Chrome(path)
        driver.get(
            "https://www.lafitness.com/Pages/ClubReservation.aspx?from=mobile&CustID=mQhh5XLlz+J"
            "+clwI9cVmouJrkPJL38yno0HdrwXUu0M=&clubID=1096")
        # ctl13 = 9:00AM
        # ctl16 = 10:00AM
        # ctl19 = 11:00AM
        id05 = "ctl00_MainContent_ucScheduleBooking_rptWeekDates_ctl01_rptWeekSchedule_ctl01_btnReserve"
        id06 = "ctl00_MainContent_ucScheduleBooking_rptWeekDates_ctl01_rptWeekSchedule_ctl04_btnReserve"
        id07 = "ctl00_MainContent_ucScheduleBooking_rptWeekDates_ctl01_rptWeekSchedule_ctl07_btnReserve"
        id08 = "ctl00_MainContent_ucScheduleBooking_rptWeekDates_ctl01_rptWeekSchedule_ctl010_btnReserve"
        id09 = "ctl00_MainContent_ucScheduleBooking_rptWeekDates_ctl01_rptWeekSchedule_ctl13_btnReserve"
        id10 = "ctl00_MainContent_ucScheduleBooking_rptWeekDates_ctl01_rptWeekSchedule_ctl16_btnReserve"
        id11 = "ctl00_MainContent_ucScheduleBooking_rptWeekDates_ctl01_rptWeekSchedule_ctl19_btnReserve"
        id12 = "ctl00_MainContent_ucScheduleBooking_rptWeekDates_ctl01_rptWeekSchedule_ctl22_btnReserve"
        id13 = "ctl00_MainContent_ucScheduleBooking_rptWeekDates_ctl01_rptWeekSchedule_ctl25_btnReserve"
        id14 = "ctl00_MainContent_ucScheduleBooking_rptWeekDates_ctl01_rptWeekSchedule_ctl28_btnReserve"
        id15 = "ctl00_MainContent_ucScheduleBooking_rptWeekDates_ctl01_rptWeekSchedule_ctl31_btnReserve"
        id16 = "ctl00_MainContent_ucScheduleBooking_rptWeekDates_ctl01_rptWeekSchedule_ctl34_btnReserve"
        id17 = "ctl00_MainContent_ucScheduleBooking_rptWeekDates_ctl01_rptWeekSchedule_ctl37_btnReserve"
        id18 = "ctl00_MainContent_ucScheduleBooking_rptWeekDates_ctl01_rptWeekSchedule_ctl40_btnReserve"
        id19 = "ctl00_MainContent_ucScheduleBooking_rptWeekDates_ctl01_rptWeekSchedule_ctl43_btnReserve"
        id20 = "ctl00_MainContent_ucScheduleBooking_rptWeekDates_ctl01_rptWeekSchedule_ctl46_btnReserve"
        id21 = "ctl00_MainContent_ucScheduleBooking_rptWeekDates_ctl01_rptWeekSchedule_ctl49_btnReserve"

        ids = {'5': id05, '6': id06, '7': id07, '8': id08,
               '9': id09, '10': id10, '11': id11, '12': id12, '13': id13,
               '14': id14, '15': id15, '16': id16, '17': id17, '18': id18,
               '19': id19, '20': id20, '21': id21
               }

        idw08 = "ctl00_MainContent_ucScheduleBooking_rptWeekDates_ctl01_rptWeekSchedule_ctl01_btnReserve"
        idw09 = "ctl00_MainContent_ucScheduleBooking_rptWeekDates_ctl01_rptWeekSchedule_ctl04_btnReserve"
        idw10 = "ctl00_MainContent_ucScheduleBooking_rptWeekDates_ctl01_rptWeekSchedule_ctl07_btnReserve"
        idw11 = "ctl00_MainContent_ucScheduleBooking_rptWeekDates_ctl01_rptWeekSchedule_ctl10_btnReserve"
        idw12 = "ctl00_MainContent_ucScheduleBooking_rptWeekDates_ctl01_rptWeekSchedule_ctl13_btnReserve"
        idw13 = "ctl00_MainContent_ucScheduleBooking_rptWeekDates_ctl01_rptWeekSchedule_ctl16_btnReserve"
        idw14 = "ctl00_MainContent_ucScheduleBooking_rptWeekDates_ctl01_rptWeekSchedule_ctl19_btnReserve"
        idw15 = "ctl00_MainContent_ucScheduleBooking_rptWeekDates_ctl01_rptWeekSchedule_ctl22_btnReserve"
        idw16 = "ctl00_MainContent_ucScheduleBooking_rptWeekDates_ctl01_rptWeekSchedule_ctl25_btnReserve"

        weekend_ids = {'8': idw08,
                       '9': idw09, '10': idw10, '11': idw11,
                       '12': idw12, '13': idw13, '14': idw14,
                       '15': idw15, '16': idw16,

                       }
        element_id = weekend_ids[time_index] if is_weekend == 1 else ids[time_index]

        element = driver.find_element_by_id(
            element_id)
        element.click()
        time.sleep(1)
        d2 = driver.switch_to.active_element
        element2 = d2.find_element_by_xpath("//button[text()='OK']")
        element2.click()
        time.sleep(5)
        driver.close()
    except:
        print("rob gets something wrong")


def inCase():
    print('dddd')

# element = driver.find_element("pool")
# element.click()

# print(element.id)
