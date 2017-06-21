from datetime import datetime, timedelta
import re


def naturaltime(text, now=None):
    """Convert a naturaltime string to a datetime object."""
    text = text.lower().strip()
    if not now:
        now = datetime.now()

    if text == 'now':
        return now
    if text == 'yesterday':
        return now - timedelta(days=1)
    if text == 'tomorrow':
        return now + timedelta(days=1)

    if "ago" in text:
        multiplier = -1
    elif "from now" in text:
        multiplier = 1
    else:
        raise ValueError("%s is not a valid naturaltime" % text)

    text = text.replace('an ', '1 ')
    text = text.replace('a ', '1 ')

    years = get_first(r'(\d*) year', text)
    months = get_first(r'(\d*) month', text)
    weeks = get_first(r'(\d*) week', text)
    days = get_first(r'(\d*) day', text)
    days = days + weeks * 7 + months * 30 + years * 365

    hours = get_first(r'(\d*) hour', text)
    minutes = get_first(r'(\d*) minute', text)
    seconds = get_first(r'(\d*) second', text)
    delta = timedelta(
        days=days,
        hours=hours,
        minutes=minutes,
        seconds=seconds)
    delta *= multiplier
    return now + delta


def get_first(pattern, text):
    """Return either a matched number or 0."""
    matches = re.findall(pattern, text)
    if matches:
        return int(matches[0])
    else:
        return 0
