import customtkinter as ctk
import tkinter as tk
from ui_elements.timer_ui import timer_create_label, timer_create_button
from ui_elements.settings_ui import (
    settings_create_button,
    settings_create_checkbox,
    settings_create_input,
    settings_create_label,
)
from timer.timer_logic import *
from timer.timer_elements import create_timer_elements
from settings.settings_elements import create_settings_element


def create_tabs(root):
    frame1 = ctk.CTkFrame(root)
    frame2 = ctk.CTkFrame(root)

    tabs = {"Timer": frame1, "Settings": frame2}

    def show_tab(tab):
        # Hide all tabs
        for frame_name, frame in tabs.items():
            frame.pack_forget()
        # Show the selected tab
        tabs[tab].pack(fill="both", expand=0)

    menu_bar = tk.Menu(root)

    for tab_name, tab_frame in tabs.items():
        menu_bar.add_command(label=tab_name, command=lambda t=tab_name: show_tab(t))

    (
        full_time_label,
        target_time_label,
        break_time_label,
        start_timer_button,
        stop_timer_button,
        end_session_button,
    ) = create_timer_elements(frame1)

    (
        settings_target_time_label,
        target_time_input,
        settings_break_time_label,
        break_time_input,
        pomodoro_checkbox,
        save_settings_button,
    ) = create_settings_element(frame2)

    frame1.pack(fill="both", expand=0)
    frame1.columnconfigure(0, weight=1)
    frame1.rowconfigure(0, weight=1)
    frame2.columnconfigure(0, weight=1)
    frame2.rowconfigure(0, weight=1)

    root.configure(menu=menu_bar)
