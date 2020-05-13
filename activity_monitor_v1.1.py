from pynput import mouse, keyboard
import csv
import datetime
import os

delay = 10

log_in = os.getlogin()

user_path = os.path.expandvars('%userprofile%\Desktop')
today = datetime.datetime.today()
print(f'Today is {today:%Y.%m.%d}')

script_start_time = datetime.datetime.now()
print(f'Start Script time {script_start_time}')

total_time_list = []


# def on_move(x, y):
#     mouse_listener.start()
#     mouse_listener.wait()
#     print(f'Listening for mouse {mouse_listener.native_id}')
#     start_time = datetime.datetime.now()
#     track_time(start_time)
#
#
# def on_click(x, y, button, pressed):
#     mouse_listener.start()
#     mouse_listener.wait()
#     print(f'Listening for mouse {mouse_listener.native_id}')
#     start_time = datetime.datetime.now()
#     track_time(start_time)
#     if not pressed:
#         # Stop listener
#         return False
#
#
# def on_scroll(x, y, dx, dy):
#     mouse_listener.start()
#     mouse_listener.wait()
#     print(f'Listening for mouse {mouse_listener.native_id}')
#     start_time = datetime.datetime.now()
#     track_time(start_time)
#
#
# def on_press(key):
#     start_time = datetime.datetime.now()
#     keyboard_listener.start()
#     keyboard_listener.wait()
#     print(f'Listening for keyboard {keyboard_listener.native_id}')
#     try:
#         track_time(start_time)
#     except AttributeError:
#         track_time(start_time)

def track_time(start_time):
    print(f'*****Start time**** {start_time}')
    report_info['Last_Start'] = f'{start_time:%Y.%m.%d %I:%M:%S %p}'
    movement = True
    while movement is True:
        with mouse.Events() as mouse_events, keyboard.Events() as keyboard_events:
            ms_event = mouse_events.get(timeout=delay/2)
            kb_event = keyboard_events.get(timeout=delay/2)
            if (ms_event is None) and (kb_event is None):
                print(f'You did not interact within {delay} seconds')
                end_time = datetime.datetime.now()
                print(f'End Time {end_time}')
                mouse_listener.stop()
                print(f'Stopped Listening to Mouse {mouse_listener.native_id}')
                keyboard_listener.stop()
                print(f'Stopped Listening to Keyboard {keyboard_listener.native_id}')
                movement = False
            else:
                event_time = datetime.datetime.now()
                if kb_event:
                    print(f'Received Keyboard event {event_time}')
                if ms_event:
                    print(f'Received Mouse event {event_time}')
                movement = True
                continue
        time_elapsed = (end_time - start_time) - datetime.timedelta(seconds=delay)
        print(f'Time Elapsed {time_elapsed}')
        add_time(time_elapsed)
        return time_elapsed

def add_time(time_elapsed):
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
        '{}/{} Time-{}.csv'.format(new_backup_folder, log_in, f'{script_start_time:%Y.%m.%d %I.%M.%S %p}'))
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
    mouse_listener = mouse.Listener()
    keyboard_listener = keyboard.Listener()
    mouse_listener = mouse.Listener()
    mouse_listener.start()
    mouse_listener.wait()
    print(f'Listening for mouse {mouse_listener.native_id}')
    keyboard_listener = keyboard.Listener()
    keyboard_listener.start()
    keyboard_listener.wait()
    print(f'Listening for keyboard {keyboard_listener.native_id}')
    if mouse_listener.running and keyboard_listener.running:
        start_time = datetime.datetime.now()
        track_time(start_time)
        report_info['Last_Start'] = f'{start_time:%Y.%m.%d %I:%M:%S %p}'
    if len(report_info) > 2:
        report = report_csv()
