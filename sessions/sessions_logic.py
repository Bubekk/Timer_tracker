import json
import time

session_file_path = "./data/session/session.json"

current_session_date = {
    "year": time.localtime().tm_year,
    "month": time.localtime().tm_mon,
    "day": time.localtime().tm_mday,
}


def save_session(work_time, break_time):
    with open(session_file_path, "r") as file:
        data = json.load(file)

    entry = {
        "date": current_session_date,
        "work_time": work_time,
        "break_time": break_time,
    }

    # if data[-1]["date"] != entry["date"]:
    #     data.append(entry)
    # else:
    #     data[-1]["date"] = entry["date"]
    #     data[-1]["work_time"] = entry["work_time"]
    #     data[-1]["break_time"] = entry["break_time"]
    print(data)
