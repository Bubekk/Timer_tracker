from .timer_logic import *
from .target_time_logic import *
from .break_time_logic import *
from ui_elements.timer_ui import *


# Creates all elements of timer tab from timer_ui functions
def create_timer_elements(parent_frame):
    full_time_label = timer_create_label(parent_frame, timer_text, 1)
    target_time_label = timer_create_label(parent_frame, target_time_text, 2)
    break_time_label = timer_create_label(parent_frame, break_time_text, 3)
    start_timer_button = timer_create_button(
        parent_frame, "start", lambda: start_timer(full_time_label), 4
    )
    stop_timer_button = timer_create_button(parent_frame, "break", timer_button_test, 5)
    end_session_button = timer_create_button(parent_frame, "End", timer_button_test, 6)

    return (
        full_time_label,
        target_time_label,
        break_time_label,
        start_timer_button,
        stop_timer_button,
        end_session_button,
    )
