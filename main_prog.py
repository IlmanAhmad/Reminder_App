import pandas as pd
from datetime import datetime
from pygame import mixer
from win10toast import ToastNotifier
import time


def musicloop(file):
    """This function is to play music file"""
    mixer.init()
    mixer.music.load(file)
    mixer.music.play()


toaster = ToastNotifier()
alarm_time = []
event_name = []


def set_alarm_time(times):
    """This function is for appending alarm_time list post reading the time inputs from excel file"""
    alarm_time.append(times)


def set_event_type(event_names):
    """This function is for appending event_name list post reading the time inputs from excel file"""
    event_name.append(event_names)


datastore = pd.read_excel(r'C:\Users\shane\PycharmProjects\pythonProject\Reminderapp\Datastore.xlsx')
"""This variable is for reading excel file"""

datalength = range(len(datastore))

for i in datalength:
    """This loop is for setting up the reminder time based on excel sheet inputs"""
    times = str(datastore.at[i, 'Time'])
    event_names = str(datastore.at[i, 'Event Name'])
    set_alarm_time(times)
    set_event_type(event_names)




while True:
    """This loop will run endlessly to keep checking below conditions to play reminder music"""
    time.sleep(1)
    for i in range(len(alarm_time)):
        """This loop is for playing reminder music when time comes"""
        user_alarm_time = str(alarm_time[i])
        curr_datetime = datetime.now()
        curr_time = curr_datetime.strftime("%H:%M:%S")
        if curr_time == user_alarm_time:
            musicloop("alarmtone.mp3")
            event_display_name = event_name[i]
            toaster.show_toast("Sample", event_display_name)
            break


