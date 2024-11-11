import re

def calculate_time_seconds(time_value, time_unit, time_value_extra):
    if time_value is None or time_unit is None:
        return None

    if '-' in time_value:
        # Handle time range, use higher end
        time_value = time_value.split('-')[1]
        time_seconds = int(time_value)
    else:
        time_seconds = int(time_value)

    if 'min' in time_unit or 'minute' in time_unit:
        time_seconds *= 60
    elif 'h' in time_unit or 'hour' in time_unit:
        time_seconds *= 3600
        if time_value_extra is not None:
            extra_mins = int(time_value_extra)
            time_seconds += (extra_mins * 60)

    return time_seconds

def create_time_regex():
    # Match words preceding a promise of a certain timeframe
    announcement_pattern = r'(?:in|be|brb|give\s*me|gimme|like|at)\s*(?:like|roughly|about)?'

    # Match various ways of representing a time as a string
    timestr_pattern = r'(\d+|\d+\s*-\s*\d+)\s*(sec(?:ond)?|s|min(?:ute)?|m|hour|h)s?\s*(\d+)?'

    return re.compile(announcement_pattern + r'\s*' + timestr_pattern, re.IGNORECASE)

def extract_time_from_message(message):
    time_regex = create_time_regex()
    match = time_regex.search(message)

    if match:
        whole_str = match.group(0)

        # The number in the time, can be a range like 10-20
        time_value = match.group(1).replace(' ', '')

        # The units of time, such as 'minutes'
        time_unit = match.group(2).lower()

        # Capture cases like the 30 in '1 hour 30'
        time_value_extra = match.group(3)

        time_seconds = calculate_time_seconds(time_value, time_unit, time_value_extra)

        return time_seconds, whole_str.strip().lower()

    return None, None
