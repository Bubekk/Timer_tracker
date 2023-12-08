break_h, break_min, break_sec = 0, 0, 0
break_time_id = None
break_time_text = f"{break_h:02d}:{break_min:02d}:{break_sec:02d}"
quantity_breaks = 0


def refresh_break_time_variables(config_time):
    global break_h, break_min, break_sec, break_time_text

    break_time_config = config_time
    break_h, break_min, break_sec = (
        break_time_config[0],
        break_time_config[1],
        break_time_config[2],
    )
    break_time_text = f"{break_h:02d}:{break_min:02d}:{break_sec:02d}"


#  Stops counting down from break time
def stop_countdown_break(label):
    global break_time_id

    if break_time_id is not None:
        label.after_cancel(break_time_id)
        break_time_id = None


# Starts counting down from break time
def break_time_countdown(label):
    global break_h, break_min, break_sec, break_time_id, break_time_text, quantity_breaks

    if break_sec == 0:
        break_sec = 59
        if break_min == 0:
            break_min = 59
            if break_h != 0:
                break_h -= 1
        else:
            break_min -= 1
    else:
        break_sec -= 1

    break_time_text = f"{break_h:02d}:{break_min:02d}:{break_sec:02d}"
    break_time_id = label.after(1000, lambda: break_time_countdown(label))
    label.configure(text=break_time_text)

    if break_h == 0 and break_min == 0 and break_sec == 0:
        stop_countdown_break(label)
        quantity_breaks += 1
        print("Your break is complete!", quantity_breaks)
