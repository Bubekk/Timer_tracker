import customtkinter as ctk


def create_target_timer_label(parent_frame, text, row):
    target_timer_label = ctk.CTkLabel(
        parent_frame, text=text, bg_color="#030303", width=350
    )
    target_timer_label.grid(row=row)
    return target_timer_label


def create_target_timer_button(parent_frame, text, command, row):
    target_timer_button = ctk.CTkButton(parent_frame, text=text, command=command)
    target_timer_button.grid(row=row)
    return target_timer_button
