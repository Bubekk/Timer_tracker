import customtkinter as ctk


def create_timer_label(parent_frame, text):
    label = ctk.CTkLabel(parent_frame, text=text, bg_color="#030303", width=350)
    label.grid(row=0, pady=10)
    return label


def create_timer_button(parent_frame, text, command, row):
    timer_button = ctk.CTkButton(parent_frame, text=text, width=180, command=command)
    timer_button.grid(row=row, pady=10)
    return timer_button


def create_timer_button_end(parent_frame, command):
    button_stop = ctk.CTkButton(
        parent_frame, text="End Session", width=180, command=command
    )
    button_stop.grid(row=3, pady=10)
    return button_stop
