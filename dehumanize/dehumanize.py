from datetime import datetime, timedelta
import re


def naturaltime(text, now=None):
    """Convert a django naturaltime string to a datetime object."""
    if not now:
        now = datetime.now()

    if text == 'now':
        return now
    if "ago" in text:
        multiplier = -1
    elif "from now" in text:
        multiplier = 1
    else:
        raise ValueError("%s is not a valid naturaltime" % text)

    text = text.replace('an ', '1 ')
    text = text.replace('a ', '1 ')

    days = get_first(r'(\d*) day', text)
    hours = get_first(r'(\d*) hour', text)
    minutes = get_first(r'(\d*) minute', text)
    seconds = get_first(r'(\d*) second', text)
    delta = timedelta(days=days, hours=hours, minutes=minutes, seconds=seconds)
    delta *= multiplier
    return now + delta


def get_first(pattern, text):
    """Return either a matched number or 0."""
    matches = re.findall(pattern, text)
    if matches:
        print(matches[0], pattern.split()[-1])
        return int(matches[0])
    else:
        return 0
