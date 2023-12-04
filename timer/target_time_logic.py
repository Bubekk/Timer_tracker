from settings.settings_logic import target_time_config

target_h, target_min, target_sec = (
    target_time_config[0],
    target_time_config[1],
    target_time_config[2],
)
target_time_id = None
target_time_text = f"{target_h:02d}:{target_min:02d}:{target_sec:02d}"
