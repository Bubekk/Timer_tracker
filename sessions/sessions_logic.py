import json
import time

session_file_path = "./data/session/session.json"

current_session_date = {
    "day": time.localtime().tm_mday,
    "month": time.localtime().tm_mon,
    "year": time.localtime().tm_year,
}


def update_work_time(h, min, sec):
    global work_h, work_min, work_sec
    work_h, work_min, work_sec = h, min, sec


# def update_break_time(h, min, sec):
#     global break_h, break_min, break_sec
#     break_h, break_min, break_sec = h, min, sec


def save_session(break_h, break_min, break_sec):
    with open(session_file_path, "r") as file:
        data = json.load(file)

    entry = {
        "date": current_session_date,
        "work_time": [work_h, work_min, work_sec],
        "break_time": [break_h, break_min, break_sec],
    }

    # if data[-1]["date"] != entry["date"]:
    #     data.append(entry)
    # else:
    #     data[-1]["date"] = entry["date"]
    #     data[-1]["work_time"] = entry["work_time"]
    #     data[-1]["break_time"] = entry["break_time"]
    print(entry)
