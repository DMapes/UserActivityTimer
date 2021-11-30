from pynput import mouse, keyboard
import csv
import datetime
import os
import concurrent.futures
import re

delay = 32

log_in = os.getlogin()

user_path = os.path.expandvars('%appdata%\Microsoft\Teams')
today = datetime.datetime.today()
print(f'Today is {today:%Y.%m.%d}')

script_start_time = datetime.datetime.now()
print(f'Start Script time {script_start_time}')

log_file = os.path.expandvars('{}\logs.txt'.format(user_path))

log_list = []

with open(log_file, 'r') as log_inputs:
    for input in log_inputs:
        log_list.append(input)

def last_log_read():
    idle = True
    last_log = str(log_list[-1:])
    log_date = last_log[2:].split('GMT')[0]
    log_datetime_object = datetime.datetime.strptime(log_date,'%a %b %d %Y %H:%M:%S ')
    if 'Machine has been idle' in last_log:
        idle = True
        idle_time = last_log.split('idle')[1] 
        seconds = re.findall('[0-9]+', idle_time)
        idle_seconds_datetime_object = datetime.datetime.strptime(str(seconds[0]),'%S')
        print (f'Machine has been idle {idle_seconds_datetime_object} seconds.')
    else:
        idle = False
        print (f'Log time is {log_datetime_object}.')
    return idle, log_datetime_object

def log_track_time(start_time, log_read):
    print(f'*****Log Start time***** {start_time}')
    report_info['Last_Start'] = f'{start_time:%Y.%m.%d %I:%M:%S %p}'
    while idle is False:
        time_elapsed = (start_time + log_read)
    print(f'Time Elapsed {time_elapsed}')
    # add_time(time_elapsed)
    return time_elapsed

# log_read = last_log_read()[1]
last_log_read()
# log_track_time(script_start_time,log_read)

# def add_time(time_elapsed):
#     print(f'Adding Time Elapsed {time_elapsed}')
#     total_time_list.append(time_elapsed)
#     added_time = datetime.timedelta()
#     if len(total_time_list) > 1:
#         for t in total_time_list:
#             # print(t)
#             added_time = added_time + t
#         print(f'Total Time Today {added_time}')
#         # report_info['Total'] = str(added_time)
#         report_info['Total'] = f'Total Time Today {str(added_time)}'
#     # return added_time

# def report_csv():
#     path = os.path.join(
#         '{}/{} Time-{}.csv'.format(new_backup_folder, log_in, f'{script_start_time:%Y.%m.%d %I.%M.%S %p}'))
#     with open(path, 'w') as csvfile:
#         if len(report_info) > 2:
#             spamwriter = csv.DictWriter(csvfile, report_info.keys())
#             spamwriter.writeheader()
#             spamwriter.writerow(report_info)

# def backup_folder():
#     location = os.path.expandvars('{}/Time Report'.format(user_path))
#     try:
#         os.mkdir(location)
#     except:
#         error = 'File already exists'
#     return location

# today = datetime.date.today()
# report_info = {}
# report_info['Day_Start'] = f'{script_start_time:%Y.%m.%d %I:%M:%S %p}'
# new_backup_folder = backup_folder()
# while today == datetime.date.today():
#     if last_log_read()[0] == True:
#        add_time(time_elapsed)
#     else:
#          print (f'Machine has been idle {idle_seconds_datetime_object} seconds.')
#     if len(report_info) > 2:
#         report = report_csv()


