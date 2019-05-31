import datetime
from datetime import date
import time

year = 0
month = 0
day = 0
current_year = 0
current_month = 0
current_day = 0
days_left = 0
strings_read = 0
event_array = " "

f = open("events.txt", "r")
lines = f.readlines()
f.close()

def get_current_time():
    global current_year
    global current_month
    global current_day

    date_str = str(datetime.datetime.now().date())
    list_date = list(date_str)

    cur_year = list_date[0] + list_date[1] + list_date[2] + list_date[3]
    cur_month = list_date[5] + list_date[6]
    cur_day = list_date[8] + list_date[9]

    current_year = int(cur_year)
    current_month = int(cur_month)
    current_day = int(cur_day)

def calculate_days_left():
    global days_left
    global year
    global month
    global day
    global current_year
    global current_month
    global current_day

    d0 = date(current_year, current_month, current_day)
    d1 = date(year, month, day)
    delta = d1 - d0
    days_left = str(delta.days)

def read_file():
    global strings_read
    global event_array
    global year
    global month
    global day
    global lines

    f = open("events.txt", "r")

    lines = f.readlines()
    string = lines[strings_read]
    list = string.split(',')
    list[-1] = list[-1].strip()
    f.close()

    event_array = list
    strings_read = strings_read + 1
    cur_year = event_array[2]
    cur_month = event_array[1]
    cur_day = event_array[0]
    year = int(cur_year)
    month = int(cur_month)
    day = int(cur_day)

    if strings_read >= len(lines):
        strings_read = 0

while True:

    times = len(lines)
    for i in range(0, 200):
        print(" ")

    print("            ________                                __              ")
    print("           /        |                              /  |             ")
    print("           $$$$$$$$/__     __  ______   _______   _$$ |_    _______ ")
    print("           $$ |__  /  \   /  |/      \ /       \ / $$   |  /       |")
    print("           $$    | $$  \ /$$//$$$$$$  |$$$$$$$  |$$$$$$/  /$$$$$$$/ ")
    print("           $$$$$/   $$  /$$/ $$    $$ |$$ |  $$ |  $$ | __$$      \ ")
    print("           $$ |_____ $$ $$/  $$$$$$$$/ $$ |  $$ |  $$ |/  |$$$$$$  |")
    print("           $$       | $$$/   $$       |$$ |  $$ |  $$  $$//     $$/ ")
    print("           $$$$$$$$/   $/     $$$$$$$/ $$/   $$/    $$$$/ $$$$$$$/  ")

    print("")
    print("")
    print("")
    print("")
    print("")

    for i in range(0, times):
        read_file()
        get_current_time()
        calculate_days_left()
        print("           " + event_array[-1])
        print("           Time left: " + days_left + "d")
        print("           ")
        print("           ")
    print("           ")

    time.sleep(300)
