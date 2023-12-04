import customtkinter as ctk


def timer_create_label(parent_frame, text, row):
    label = ctk.CTkLabel(parent_frame, text=text)
    label.grid(row=row)
    return label


def timer_create_button(parent_frame, text, command, row):
    button = ctk.CTkButton(parent_frame, text=text, command=command)
    button.grid(row=row)
    return button
