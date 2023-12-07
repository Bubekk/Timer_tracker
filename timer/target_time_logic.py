target_h, target_min, target_sec = (0, 0, 0)
target_time_id = None
target_time_text = f"{target_h:02d}:{target_min:02d}:{target_sec:02d}"


# Refreshes variables to work dynamically with settings options
def refresh_target_time_variables(config_time):
    global target_h, target_min, target_sec, target_time_text

    target_time_config = config_time
    target_h, target_min, target_sec = (
        target_time_config[0],
        target_time_config[1],
        target_time_config[2],
    )
    target_time_text = f"{target_h:02d}:{target_min:02d}:{target_sec:02d}"


#  Stops counting down from target time
def stop_countdown_target(label):
    global target_time_id

    if target_time_id is not None:
        label.after_cancel(target_time_id)
        target_time_id = None


# Starts counting down from target time
def target_time_countdown(label):
    global target_h, target_min, target_sec, target_time_id, target_time_text

    if target_sec == 0:
        target_sec = 59
        if target_min == 0:
            target_min = 59
            if target_h != 0:
                target_h -= 1
        else:
            target_min -= 1
    else:
        target_sec -= 1

    target_time_text = f"{target_h:02d}:{target_min:02d}:{target_sec:02d}"
    target_time_id = label.after(1000, lambda: target_time_countdown(label))
    label.configure(text=target_time_text)

    if target_h == 0 and target_min == 0 and target_sec == 0:
        stop_countdown_target(label)
        print("Your target is complete!")
