import customtkinter as ctk


def settings_create_label(parent_frame, text, row):
    label = ctk.CTkLabel(parent_frame, text=text)
    label.grid(row=row)
    return label


def settings_create_input(parent_frame, variable, row):
    input = ctk.CTkEntry(parent_frame, textvariable=variable)
    input.grid(row=row)
    return input


def settings_create_checkbox(parent_frame, text, variable, command, row):
    checkbox = ctk.CTkCheckBox(
        parent_frame,
        text=text,
        variable=variable,
        onvalue=True,
        offvalue=False,
        command=command,
    )
    checkbox.grid(row=row)
    return checkbox


def settings_create_button(parent_frame, text, command, row):
    button = ctk.CTkButton(parent_frame, text=text, command=command)
    button.grid(row=row)
    return button
