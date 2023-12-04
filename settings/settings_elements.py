import customtkinter as ctk
from ui_elements.settings_ui import *
from timer.target_time_logic import target_time_text
from timer.break_time_logic import break_time_text
from settings.settings_logic import *


# Creates all elements of settings tab from settings_ui functions
def create_settings_element(parent_frame, target_label, break_label):
    settings_target_time_label = settings_create_label(
        parent_frame, "Set your work time target", 1
    )
    target_time_status = ctk.StringVar(value=target_time_text)
    target_time_input = settings_create_input(parent_frame, target_time_status, 2)

    settings_label_break_time = settings_create_label(
        parent_frame, "Set your break time", 3
    )
    break_time_status = ctk.StringVar(value=break_time_text)
    break_time_input = settings_create_input(parent_frame, break_time_status, 4)

    pomodoro_status = ctk.BooleanVar(value=pomodoro_config)
    pomodoro_checkbox = settings_create_checkbox(
        parent_frame, "🍅 pomodoro? 🍅", pomodoro_status, checkbox_test, 5
    )

    save_settings_button = settings_create_button(
        parent_frame,
        "Save Settings",
        lambda: save_settings(
            target_time_input.get(),
            break_time_input.get(),
            pomodoro_checkbox.get(),
            target_label,
            break_label,
        ),
        6,
    )

    return (
        settings_target_time_label,
        target_time_input,
        settings_label_break_time,
        break_time_input,
        pomodoro_checkbox,
        save_settings_button,
    )
