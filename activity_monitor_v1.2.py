from pynput import mouse, keyboard
import csv
import datetime
import os
import concurrent.futures

delay = 16

log_in = os.getlogin()

user_path = os.path.expandvars('%userprofile%\Desktop')
today = datetime.datetime.today()
print(f'Today is {today:%Y.%m.%d}')

script_start_time = datetime.datetime.now()
print(f'Start Script time {script_start_time}')

total_time_list = []


def ms_track_time(start_time):
    print(f'*****Mouse Start time***** {start_time}')
    report_info['Last_Start'] = f'{start_time:%Y.%m.%d %I:%M:%S %p}'
    mouse_listener = mouse.Listener()
    mouse_listener.start()
    mouse_listener.wait()
    print(f'Listening for mouse {mouse_listener.native_id}')
    movement = True
    while movement is True:
        with mouse.Events() as mouse_events:
            ms_event = mouse_events.get(timeout=delay)
            if ms_event is None:
                print(f'You did not interact with the mouse within {delay} seconds')
                end_time = datetime.datetime.now()
                print(f'End Time {end_time}')
                mouse_listener.stop()
                print(f'Stopped Listening to Mouse {mouse_listener.native_id}')
                movement = False
            else:
                event_time = datetime.datetime.now()
                if ms_event:
                    print(f'Received Mouse event {event_time}')
                movement = True
                continue
        time_elapsed = (end_time - start_time) - datetime.timedelta(seconds=delay)
        print(f'Time Elapsed {time_elapsed}')
        # add_time(time_elapsed)
        return time_elapsed

def kb_track_time(start_time):
    print(f'*****Keyboard Start time***** {start_time}')
    report_info['Last_Start'] = f'{start_time:%Y.%m.%d %I:%M:%S %p}'
    keyboard_listener = keyboard.Listener()
    keyboard_listener.start()
    keyboard_listener.wait()
    print(f'Listening for keyboard {keyboard_listener.native_id}')
    movement = True
    while movement is True:
        with keyboard.Events() as keyboard_events:
            kb_event = keyboard_events.get(timeout=delay)
            if kb_event is None:
                print(f'You did not interact with the keyboard within {delay} seconds')
                end_time = datetime.datetime.now()
                print(f'End Time {end_time}')
                keyboard_listener.stop()
                print(f'Stopped Listening to Keyboard {keyboard_listener.native_id}')
                movement = False
            else:
                event_time = datetime.datetime.now()
                if kb_event:
                    print(f'Received Keyboard event {event_time}')
                movement = True
                continue
        time_elapsed = (end_time - start_time) - datetime.timedelta(seconds=delay)
        print(f'Time Elapsed {time_elapsed}')
        # add_time(time_elapsed)
        return time_elapsed

def add_time(time_elapsed):
    print(f'Adding Time Elapsed {time_elapsed}')
    total_time_list.append(time_elapsed)
    added_time = datetime.timedelta()
    if len(total_time_list) > 1:
        for t in total_time_list:
            # print(t)
            added_time = added_time + t
        print(f'Total Time Today {added_time}')
        # report_info['Total'] = str(added_time)
        report_info['Total'] = f'Total Time Today {str(added_time)}'
    # return added_time


def report_csv():
    path = os.path.join(
        '{}/{} Time-{}-TEST.csv'.format(new_backup_folder, log_in, f'{script_start_time:%Y.%m.%d %I.%M.%S %p}'))
    with open(path, 'w') as csvfile:
        if len(report_info) > 2:
            spamwriter = csv.DictWriter(csvfile, report_info.keys())
            spamwriter.writeheader()
            spamwriter.writerow(report_info)


def backup_folder():
    location = os.path.expandvars('{}/Time Report'.format(user_path))
    try:
        os.mkdir(location)
    except:
        error = 'File already exists'
    return location


today = datetime.date.today()
report_info = {}
report_info['Day_Start'] = f'{script_start_time:%Y.%m.%d %I:%M:%S %p}'
new_backup_folder = backup_folder()
while today == datetime.date.today():
    with concurrent.futures.ThreadPoolExecutor() as executor:
        mouse_ex = executor.submit(ms_track_time, datetime.datetime.now())
        keyboard_ex = executor.submit(kb_track_time, datetime.datetime.now())
        add_time(mouse_ex.result())
        add_time(keyboard_ex.result())
    if len(report_info) > 2:
        report = report_csv()
