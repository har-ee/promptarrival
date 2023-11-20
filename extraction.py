import re

def extract_time_from_message(message):
    time_pattern = re.compile(r'(?:in|be|brb|give\s*me)\s*(\d+|\d+\s*-\s*\d+)\s*(sec|secs|second|seconds|min|mins|minute|minutes|h|hour|hours)\s*(\d+)?', re.IGNORECASE)

    match = time_pattern.search(message)

    if match:
        whole_str = match.group(0)
        time_str = match.group(1).replace(' ', '')
        time_units = match.group(2).lower()
        time_str_extra = match.group(3)

        if '-' in time_str:
            time_value = time_str.split('-')[1]
            time_seconds = int(time_value)
        else:
            time_seconds = int(time_str)

        if 'min' in time_units or 'minute' in time_units:
            time_seconds *= 60
        elif 'h' in time_units or 'hour' in time_units:
            time_seconds *= 3600
            if time_str_extra is not None:
                extra_mins = int(time_str_extra)
                time_seconds += (extra_mins * 60)

        return time_seconds, whole_str.strip().lower()

    return None, None
