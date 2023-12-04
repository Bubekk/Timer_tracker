h, min, sec = 0, 0, 0
timer_id = None
timer_text = f"{h:02d}:{min:02d}:{sec:02d}"


def timer_button_test():
    print("timer button works")


def start_timer(label):
    if timer_id is None:
        timer(label)
    else:
        print("nie wiem coś tutej")


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
