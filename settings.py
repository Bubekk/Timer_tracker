import customtkinter as ctk
import tkinter as tk


def create_settings_label(parent_frame, text, row):
    settings_label = ctk.CTkLabel(parent_frame, text=text)
    settings_label.grid(row=row, pady=10)
    return settings_label


def create_settings_input(parent_frame, variable, row):
    settings_input = ctk.CTkEntry(parent_frame, textvariable=variable)
    settings_input.grid(row=row)
    return settings_input


def create_settings_checkbox(parent_frame, text, variable, command, row):
    settings_checkbox = ctk.CTkCheckBox(
        parent_frame,
        text=text,
        variable=variable,
        onvalue="true",
        offvalue="false",
        command=command,
    )
    settings_checkbox.grid(row=row)
    return settings_checkbox


def create_settings_button(parent_frame, text, command, row):
    settings_button = ctk.CTkButton(parent_frame, text=text, width=180, command=command)
    settings_button.grid(row=row, pady=10)
    return settings_button
