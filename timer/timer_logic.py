from .target_time_logic import target_time_countdown, stop_countdown_target
from .new_break_time import break_time_countdown, stop_countdown_break

h, min, sec = 0, 0, 0
timer_id = None
timer_text = f"{h:02d}:{min:02d}:{sec:02d}"


# Temporary test function!
def timer_button_test():
    print("timer button works")


# If timer id is None it triggers timer()
def start_timer(label, target_label, break_label):
    if timer_id is None:
        timer(label)
        target_time_countdown(target_label)
        stop_countdown_break(break_label)
    else:
        pass


# stop timer logic
def stop_timer(label, target_label, break_label):
    global timer_id, target_timer_id
    if timer_id is not None:
        label.after_cancel(timer_id)
        timer_id = None
        stop_countdown_target(target_label)
        break_time_countdown(break_label)


# convert time into proper format and modifies main timer label
def timer(label):
    global timer_text, sec, min, h, timer_id
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
    timer_id = label.after(1000, lambda: timer(label))
    label.configure(text=timer_text)
