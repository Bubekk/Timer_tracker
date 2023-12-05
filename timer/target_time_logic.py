from settings.settings_logic import target_time_config

target_h, target_min, target_sec = (
    target_time_config[0],
    target_time_config[1],
    target_time_config[2],
)
target_time_id = None
target_time_text = f"{target_h:02d}:{target_min:02d}:{target_sec:02d}"


def stop_countdown_target(label):
    global target_time_id

    if target_time_id is not None:
        label.after_cancel(target_time_id)
        target_time_id = None
    print("Your target is complete!")


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
