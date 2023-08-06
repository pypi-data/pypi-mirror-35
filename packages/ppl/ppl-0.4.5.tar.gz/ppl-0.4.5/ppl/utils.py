def format_time(time, unit="s"):
    time_units = ["s", "m", "h", "days"]
    while time_units.index(unit) > -1 and time_units.index(unit) < len(time_units) - 1:
        if time > 60 and unit in ["s", "m", 'h']:
            time = time / (60 if unit in ['s', 'm'] else 24)
            unit = time_units[time_units.index(unit) + 1]
        else:
            break
    return time, unit
