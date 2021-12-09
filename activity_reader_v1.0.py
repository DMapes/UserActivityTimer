from pynput import mouse, keyboard
import csv
import datetime
import os
import re

delay = 32

log_in = os.getlogin()

user_path = os.path.expandvars('%userprofile%\Desktop')
# time_files_path = os.path.expandvars('{}\Time Report'.format(user_path))
time_files_path = r"C:\Users\dan.mapes\Desktop\Time Report"
print (time_files_path)

today = datetime.datetime.today()
print(f'Today is {today:%Y.%m.%d}')

for root, dirs, files in os.walk(time_files_path):
    # print(files)
    for file in files:
        # filepath = ('{}\{}'.format(time_files_path,file))
        filepath = os.path.expandvars('{}\{}'.format(root,file))
        # print(filepath)
        with open(filepath, 'r') as transactions:
            csv_reader = csv.DictReader(transactions)
            for item in csv_reader:
                day_start = item['Day_Start']
                day_end = item['Last_Start']
                total = item['Total']
            day_start_datetime_object = datetime.datetime.strptime(day_start,'%Y.%m.%d %I:%M:%S %p')
            day_end_datetime_object = datetime.datetime.strptime(day_end,'%Y.%m.%d %I:%M:%S %p')
            day_start_week = day_start_datetime_object.strftime("%V")
            time = total[16:-10]
            find_hour = re.findall('^[^:]*', time)
            hour = int(find_hour[0])
            find_minute = re.findall('[^:]*$', time)
            minute = int(find_minute[0])
        print(day_start_datetime_object)
        # print(day_end_datetime_object)
        print(time)
        # print (hour)
        # print (minute)
        print(day_start_week)

