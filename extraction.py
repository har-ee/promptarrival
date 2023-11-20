import re

def extract_time_from_message(message):
    # Match words preceding a promise of a certain timeframe
    announcement_pattern = r'(?:in|be|brb|give\s*me)'

    # Match various ways of representing a time as a string
    timestr_pattern = r'(\d+|\d+\s*-\s*\d+)\s*(sec(?:ond)?|s|min(?:ute)?|m|hour|h)s?\s*(\d+)?'

    time_pattern = re.compile(announcement_pattern + r'\s*' + timestr_pattern, re.IGNORECASE)
    match = time_pattern.search(message)

    if match:
        whole_str = match.group(0)

        # The number in the time, can be a range like 10-20
        time_str = match.group(1).replace(' ', '')

        # The units of time, such as 'minutes'
        time_units = match.group(2).lower()

        # Capture cases like the 30 in '1 hour 30'
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
