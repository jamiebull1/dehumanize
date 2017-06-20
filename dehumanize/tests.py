"""Test suite for reversing Django humanize.naturaltime strings.
"""
from datetime import datetime, timedelta
import dehumanize


def test_parse_time_past():
    """Test that the various string patterns are recognised and converted."""
    now = datetime.now()
    tests = [
        ('57 seconds ago', -timedelta(seconds=57)),
        ('4 minutes ago', -timedelta(minutes=4)),
        ('4 hours ago', -timedelta(hours=4)),
        ('an hour ago', -timedelta(hours=1)),
        ('a minute ago', -timedelta(minutes=1)),
        ('now', -timedelta(hours=0)),
        ('1 day ago', -timedelta(days=1)),
        ('2 days ago', -timedelta(days=2)),
        ('1 day ago', -timedelta(days=1)),
        ('1 day, 1 hour ago', -timedelta(days=1, hours=1)),
        ('1 day, 2 hours ago', -timedelta(days=1, hours=2)),
        ('2 days, 1 hour ago', -timedelta(days=2, hours=1)),
        ('2 days, 2 hours ago', -timedelta(days=2, hours=2)),
        ]
    for naturaltime, delta in tests:
        parsed = dehumanize.naturaltime(naturaltime, now)
        expected = (now + delta)
        assert(parsed == expected)


def test_parse_time_future():
    """Test that the various string patterns are recognised and converted."""
    now = datetime.now()
    tests = [
        ('57 seconds from now', timedelta(seconds=57)),
        ('4 minutes from now', timedelta(minutes=4)),
        ('4 hours from now', timedelta(hours=4)),
        ('an hour from now', timedelta(hours=1)),
        ('a minute from now', timedelta(minutes=1)),
        ('now', timedelta(hours=0)),
        ('1 day from now', timedelta(days=1)),
        ('2 days from now', timedelta(days=2)),
        ('1 day from now', timedelta(days=1)),
        ('1 day, 1 hour from now', timedelta(days=1, hours=1)),
        ('1 day, 2 hours from now', timedelta(days=1, hours=2)),
        ('2 days, 1 hour from now', timedelta(days=2, hours=1)),
        ('2 days, 2 hours from now', timedelta(days=2, hours=2)),
        ]
    for naturaltime, delta in tests:
        parsed = dehumanize.naturaltime(naturaltime, now)
        expected = (now + delta)
        assert(parsed == expected)
