import json
from timer.target_time_logic import refresh_target_time_variables
from timer.new_break_time import refresh_break_time_variables

settings_file_path = "./data/config/config.json"


# dummy test function. Temporary!
def checkbox_test():
    print("checkbox works")


# dummy test function. Temporary!
def btn_test():
    print("save works")


# Reads settings from config.json set them into global variables
def read_settings():
    global target_time_config, break_time_config, pomodoro_config
    with open(settings_file_path, "r") as file:
        data = json.load(file)

        target_time_config = data[0]["target_time"]
        break_time_config = data[0]["break_time"]
        pomodoro_config = data[0]["pomodoro"]

        refresh_target_time_variables(target_time_config)
        refresh_break_time_variables(break_time_config)

        return target_time_config, break_time_config, pomodoro_config


# Trigger function on app load to set initialy settings
read_settings()


# Saves settings from input spaces in settings tab
def save_settings(time_input, break_input, pomodoro, target_label, break_label):
    new_target_time_config = time_input
    new_break_time_config = break_input
    new_pomodoro_config = pomodoro

    # NEED TO PROTECT FUNCTION IF FILE DON'T EXISTS!!!

    with open(settings_file_path, "r") as file:
        data = json.load(file)

    data[0]["target_time"] = [int(i) for i in new_target_time_config.split(":")]
    data[0]["break_time"] = [int(i) for i in new_break_time_config.split(":")]
    data[0]["pomodoro"] = new_pomodoro_config

    with open(settings_file_path, "w") as outfile:
        json.dump(data, outfile, indent=4)

    # Sets labels to new inputs variables after save
    target_label.configure(text=new_target_time_config)
    break_label.configure(text=new_break_time_config)

    # Uses function from target_time_logic to refresh target time variables
    refresh_target_time_variables(data[0]["target_time"])
    refresh_break_time_variables(data[0]["break_time"])
