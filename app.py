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


# loads config.json and set some variables about user settings on launch
def read_settings():
    with open(config_json_file, "r") as file:
        data = json.load(file)
        work_time_setting = data[0]["work_time_target"]
        break_time_setting = data[0]["break_time"]
        pomodoro = data[0]["pomodoro?"]
        afk_tracker_setting = data[0]["afk_tracker"]
        return (
            work_time_setting,
            break_time_setting,
            pomodoro,
            afk_tracker_setting,
        )


# triggers read settings to set config on start
settings = read_settings()
print(settings)


# target time timer variables declaration
target_sec, target_min, target_h = settings[0][2], settings[0][1], settings[0][0]
break_time_sec, break_time_min, break_time_h = (
    settings[1][2],
    settings[1][1],
    settings[1][0],
)
target_timer_id = None
target_timer_text = f"{target_h:02d}:{target_min:02d}:{target_sec:02d}"
break_time_timer_id = None
break_time_text = f"{break_time_h:02d}:{break_time_min:02d}:{break_time_sec:02d}"
break_time_timer_id = None


# counts down to 0 from target_time
def countdown_target():
    global target_timer_id, target_timer_text, target_sec, target_min, target_h

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

    if target_sec == 0 and target_min == 0 and target_h == 0:
        stop_countdown_target()


# stop countdown logic
def stop_countdown_target():
    global target_timer_id
    if target_timer_id is not None:
        target_timer_label.after_cancel(target_timer_id)
        target_timer_id = None
    print("Your target is complete!")


# counts down to 0 from break_time
def countdown_break_time():
    global break_time_timer_id, break_time_text, break_time_sec, break_time_min, break_time_h

    if break_time_sec == 0:
        break_time_sec = 59
        if break_time_min == 0:
            break_time_min = 59
            if break_time_h != 0:
                break_time_h -= 1
        else:
            break_time_min -= 1
    else:
        break_time_sec -= 1

    break_time_text = f"{break_time_h:02d}:{break_time_min:02d}:{break_time_sec:02d}"
    break_time_timer_id = break_time_label.after(1000, countdown_break_time)
    break_time_label.configure(text=break_time_text)

    if break_time_sec == 0 and break_time_min == 0 and break_time_h == 0:
        stop_countdown_break_time()
        start_timer()


# stop countdown logic
def stop_countdown_break_time():
    global break_time_timer_id
    if break_time_timer_id is not None:
        break_time_label.after_cancel(break_time_timer_id)
        break_time_timer_id = None
    print("Your break is over!")


# appends new settings after hitting save button, and sets work_time_target and break_time to proper values
def save_settings():
    global target_timer_text, target_sec, target_min, target_h, break_time_h, break_time_min, break_time_sec

    work_time = work_time_input_status.get()
    break_time = break_time_input_status.get()
    pomodoro = check_pomodoro.get() == "true"
    afk_time_cycle = check_state_afk_tracker.get() == "true"

    with open(config_json_file, "r") as file:
        data = json.load(file)

    target_h, target_min, target_sec = [int(i) for i in work_time.split(":")]
    break_time_h, break_time_min, break_time_sec = [
        int(i) for i in break_time.split(":")
    ]
    data[0]["work_time_target"] = [int(i) for i in work_time.split(":")]
    data[0]["break_time"] = [int(i) for i in break_time.split(":")]
    data[0]["pomodoro?"] = pomodoro
    data[0]["afk_tracker"] = afk_time_cycle

    with open(config_json_file, "w") as outfile:
        json.dump(data, outfile, indent=4)

    if pomodoro:
        target_h, target_min, target_sec = 0, 25, 0
        break_time_h, break_time_min, break_time_sec = 0, 5, 0
        target_timer_text = f"{target_h:02d}:{target_min:02d}:{target_sec:02d}"
        target_timer_label.configure(text=target_timer_text)
        break_time_text = (
            f"{break_time_h:02d}:{break_time_min:02d}:{break_time_sec:02d}"
        )
        break_time_label.configure(text=break_time_text)
    else:
        target_timer_text = f"{target_h:02d}:{target_min:02d}:{target_sec:02d}"
        target_timer_label.configure(text=target_timer_text)
        break_time_text = (
            f"{break_time_h:02d}:{break_time_min:02d}:{break_time_sec:02d}"
        )
        break_time_label.configure(text=break_time_text)


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
        break_time_start()
        timer()
        countdown_target()


# stop timer logic
def stop_timer():
    global timer_id
    if timer_id is not None:
        timer_label.after_cancel(timer_id)
        target_timer_label.after_cancel(target_timer_id)
        timer_id = None


# break time start logic
def break_time_start():
    global timer_id
    if timer_id is not None:
        timer_label.after_cancel(timer_id)
        target_timer_label.after_cancel(target_timer_id)
        countdown_break_time()
        timer_id = None


# reset timer logic
def reset_timer():
    global sec, min, h, timer_text
    sec, min, h = 0, 0, 0
    timer_text = f"{h:02d}:{min:02d}:{sec:02d}"
    timer_label.configure(text=timer_text)


# save session logic. Open files, appends data, save file
def save_session(entry):
    with open(session_json_file, "r") as file:
        data = json.load(file)

    # if true append new entry, else change data work time to int value
    if data[-1]["date"] != entry["date"]:
        data.append(entry)
    else:
        # change entry work time to int value
        data_int = [int(i) for i in data[-1]["work_time"].split(":")]
        # add both lists value
        entry_int = [int(i) for i in entry["work_time"].split(":")]
        new_work_time_int = [d + e for d, e in zip(data_int, entry_int)]

        # Check if seconds are bigger than 59 sec, and then add it to minutes
        if new_work_time_int[2] >= 59:
            x = divmod(new_work_time_int[2], 60)
            new_work_time_int[1] += x[0]
            new_work_time_int[2] = x[1]

        # Chcek if minutes are bigger than 59, and than add it to hours
        if new_work_time_int[1] >= 59:
            x = divmod(new_work_time_int[1], 60)
            new_work_time_int[0] += x[0]
            new_work_time_int[1] = x[1]

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
    session = {"date": cur_date, "work_time": timer_text, "break_time": break_time_text}
    stop_timer()
    save_session(session)
    reset_timer()


# Check if pomodoro setting is true, if true dynamically sets state of setting inputs to disabled else to normal.
def checkbox_pomodoro_influence():
    chceckbox_state = check_pomodoro.get()
    if chceckbox_state == "true":
        settings_input_work_time.configure(state="disabled", text_color="#821514")
        settings_input_break_time.configure(state="disabled", text_color="#821514")
    else:
        settings_input_work_time.configure(state="normal", text_color="#fff")
        settings_input_break_time.configure(state="normal", text_color="#fff")


def checkbox_test():
    checkbox_state = check_state_afk_tracker.get()
    print(checkbox_state)


# menu tabs logic
def show_tab(tab):
    # Hide all tabs
    for frame_name, frame in tabs.items():
        frame.pack_forget()
    # Show the selected tab
    tabs[tab].pack(fill="both", expand=0)


# Setting variables to the initial values read from config.json.
def set_initial_settings():
    check_pomodoro.set(str(settings[2]).lower())
    check_state_afk_tracker.set(str(settings[3]).lower())
    work_time = work_time_input_status.get()
    target_h, target_min, target_sec = [int(i) for i in work_time.split(":")]

    if settings[2] == True:
        settings_input_work_time.configure(state="disabled", text_color="#821514")
        settings_input_break_time.configure(state="disabled", text_color="#821514")
        target_h, target_min, target_sec = 0, 25, 0
        target_timer_text = f"{target_h:02d}:{target_min:02d}:{target_sec:02d}"
        target_timer_label.configure(text=target_timer_text)
        break_time_h, break_time_min, break_time_sec = 0, 5, 0
        break_time_text = (
            f"{break_time_h:02d}:{break_time_min:02d}:{break_time_sec:02d}"
        )
        break_time_label.configure(text=break_time_text)
    else:
        settings_input_work_time.configure(state="normal", text_color="#fff")
        settings_input_break_time.configure(state="normal", text_color="#fff")


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
timer_button_break = create_timer_button(frame1, "break", break_time_start, 2)
button_end = create_timer_button_end(frame1, end_session)

# Content for target timer tab
target_timer_label = create_target_timer_label(frame2, target_timer_text, 0)
break_time_label = create_target_timer_label(frame2, break_time_text, 1)

# Content for settings tab
settings_label_work_time_target = create_settings_label(
    frame3, "Set your target time to work", 2
)
work_time_input_status = ctk.StringVar(value=target_timer_text)
settings_input_work_time = create_settings_input(frame3, work_time_input_status, 3)

settings_label_break_time = create_settings_label(frame3, "Set your break time", 4)
break_time_input_status = ctk.StringVar(value=break_time_text)
settings_input_break_time = create_settings_input(frame3, break_time_input_status, 5)

check_pomodoro = ctk.StringVar(value="false")
settings_checkbox_cycle_breaktime = create_settings_checkbox(
    frame3, "🍅 pomodoro? 🍅", check_pomodoro, checkbox_pomodoro_influence, 6
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

set_initial_settings()

root.mainloop()
