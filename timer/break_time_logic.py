from settings.settings_logic import break_time_config

break_time_h, break_time_min, break_time_sec = (
    break_time_config[0],
    break_time_config[1],
    break_time_config[2],
)
break_time_timer_id = None
break_time_text = f"{break_time_h:02d}:{break_time_min:02d}:{break_time_sec:02d}"
