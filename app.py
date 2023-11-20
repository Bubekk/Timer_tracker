import customtkinter as ctk
import tkinter as tk
import json
import time
from timer import (
    create_timer_label,
    create_timer_button,
    create_timer_button_end,
)
from settings import (
    create_settings_label,
    create_settings_input,
    create_settings_checkbox,
    create_settings_button,
)

from target_timer import create_target_timer_label

# variables declaration
sec, min, h = 0, 0, 0
timer_id = None
timer_text = f"{h:02d}:{min:02d}:{sec:02d}"
session_json_file = "./session/session.json"
config_json_file = "./config/config.json"


# loads config.json and set some variables about user settings
def read_settings():
    with open(config_json_file, "r") as file:
        data = json.load(file)
        work_time_setting = data[0]["work_time_target"]
        break_time_setting = data[0]["break_time"]
        break_time_cycle = data[0]["break_time_cycle"]
        afk_tracker_setting = data[0]["afk_tracker"]
        return (
            work_time_setting,
            break_time_setting,
            break_time_cycle,
            afk_tracker_setting,
        )


# triggers read settings to set config on start
settings = read_settings()
target_sec, target_min, target_h = settings[0][2], settings[0][1], settings[0][0]
target_timer_id = None
target_timer_text = f"{target_h:02d}:{target_min:02d}:{target_sec:02d}"


# counts down to 0 from target_time
def countdown_target():
    global target_timer_id, target_timer_text, target_sec, target_min, target_h

    if target_sec == 0 and target_min == 0 and target_h == 0:
        print("Your target is complet!")

    if target_sec == 0:
        target_sec = 59
        if target_min == 0:
            target_min = 59
            if target_h != 0:
                target_h -= 1
        else:
            target_min -= 1
    else:
        target_sec -= 1

    target_timer_text = f"{target_h:02d}:{target_min:02d}:{target_sec:02d}"
    target_timer_id = target_timer_label.after(1000, countdown_target)
    target_timer_label.configure(text=target_timer_text)


# appends new settings after hitting save button
def save_settings():
    work_time = work_time_input_status.get()
    break_time = break_time_input_status.get()
    break_time_cycle = check_state_cycle_breaktime.get() == "true"
    afk_time_cycle = check_state_afk_tracker.get() == "true"

    with open(config_json_file, "r") as file:
        data = json.load(file)

        data[0]["work_time_target"] = [int(i) for i in work_time.split(":")]
        data[0]["break_time"] = [int(i) for i in break_time.split(":")]
        data[0]["break_time_cycle"] = break_time_cycle
        data[0]["afk_tracker"] = afk_time_cycle

    with open(config_json_file, "w") as outfile:
        json.dump(data, outfile, indent=4)


# overall timer logic
def timer():
    global timer_id, timer_text, sec, min, h

    if sec == 59:
        sec = 0
        if min == 59:
            min = 0
            h += 1
        else:
            min += 1
    else:
        sec += 1

    timer_text = f"{h:02d}:{min:02d}:{sec:02d}"
    timer_id = timer_label.after(1000, timer)
    timer_label.configure(text=timer_text)


# start timer logic
def start_timer():
    global timer_id
    if timer_id is None:
        stop_timer()
        timer()
        countdown_target()


# stop timer logic
def stop_timer():
    global timer_id
    if timer_id is not None:
        timer_label.after_cancel(timer_id)
        timer_id = None


def reset_timer():
    global sec, min, h, timer_text
    sec, min, h = 0, 0, 0
    timer_text = f"{h:02d}:{min:02d}:{sec:02d}"
    timer_label.configure(text=timer_text)


# save session logic. Open files, appends data, save file
def save_session(entry):
    with open(session_json_file, "r") as file:
        data = json.load(file)

    print(data[-1]["date"])

    # if true append new entry, else change data work time to int value
    if data[-1]["date"] != entry["date"]:
        data.append(entry)
    else:
        # change entry work time to int value
        data_int = [int(i) for i in data[-1]["work_time"].split(":")]
        # add both lists value
        entry_int = [int(i) for i in entry["work_time"].split(":")]
        new_work_time_int = [d + e for d, e in zip(data_int, entry_int)]
        # change last entry data worktime to update value
        new_work_time = ":".join([f"{num:02d}" for num in new_work_time_int])
        data[-1]["work_time"] = new_work_time

    with open(session_json_file, "w") as outfile:
        json.dump(data, outfile, indent=4)


# end session logic. Stops timer, get session data to save in json
def end_session():
    global timer_text
    cur_date = {
        "year": time.localtime().tm_year,
        "month": time.localtime().tm_mon,
        "day": time.localtime().tm_mday,
    }
    session = {"date": cur_date, "work_time": timer_text}
    stop_timer()
    save_session(session)
    reset_timer()


def checkbox_test():
    print("cycle is: " + check_state_afk_tracker.get())
    print("afk is: " + check_state_cycle_breaktime.get())


# menu tabs logic
def show_tab(tab):
    # Hide all tabs
    for frame_name, frame in tabs.items():
        frame.pack_forget()
    # Show the selected tab
    tabs[tab].pack(fill="both", expand=0)


root = ctk.CTk()
root.title("MyNewApp")
root.geometry("700x600")

# Create frames for each "tab"
frame1 = ctk.CTkFrame(root)
frame2 = ctk.CTkFrame(root)
frame3 = ctk.CTkFrame(root)

# Content for timer tab
timer_label = create_timer_label(frame1, timer_text)
timer_button_start = create_timer_button(frame1, "start", start_timer, 1)
timer_button_break = create_timer_button(frame1, "break", stop_timer, 2)
button_end = create_timer_button_end(frame1, end_session)

# Content for target timer tab
target_timer_label = create_target_timer_label(frame2, target_timer_text, 0)

# Content for settings tab
settings_label_work_time_target = create_settings_label(
    frame3, "Set your target time to work", 2
)
work_time_input_status = ctk.StringVar(value=target_timer_text)
settings_input_work_time = create_settings_input(frame3, work_time_input_status, 3)

settings_label_break_time = create_settings_label(frame3, "Set your break time", 4)
break_time_input_status = ctk.StringVar(value="00:00:00")
settings_input_break_time = create_settings_input(frame3, break_time_input_status, 5)

check_state_cycle_breaktime = ctk.StringVar(value="false")
settings_checkbox_cycle_breaktime = create_settings_checkbox(
    frame3, "is break cycle?", check_state_cycle_breaktime, checkbox_test, 6
)

check_state_afk_tracker = ctk.StringVar(value="false")
settings_checkbox_afk_tracker = create_settings_checkbox(
    frame3, "track afk status?", check_state_afk_tracker, checkbox_test, 7
)

settings_save_button = create_settings_button(frame3, "Save", save_settings, 8)


# Pack frames initially
frame1.pack(fill="both", expand=0)
frame1.columnconfigure(0, weight=1)
frame1.rowconfigure(0, weight=1)
frame2.columnconfigure(0, weight=1)
frame2.rowconfigure(0, weight=1)
frame3.columnconfigure(0, weight=1)
frame3.rowconfigure(0, weight=1)

# Dictionary to hold references to frames
tabs = {"Timer": frame1, "Target": frame2, "Settings": frame3}

# Menu to switch between tabs using tkinter
menu_bar = tk.Menu(root)

for tab_name, tab_frame in tabs.items():
    menu_bar.add_command(label=tab_name, command=lambda t=tab_name: show_tab(t))

root.config(menu=menu_bar)

root.mainloop()