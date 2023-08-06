# -*- coding: utf8 -*-

import pytz
from datetime import datetime, timedelta
from intimezone.Error import ErrorFormatTemplate

__all__ = ['utc_localize', 'utc_convert']


def utc_(moment_time, tz):
    """
    Converts unix time to datetime.datetime.

    :param moment_time: unix time; may be format: int, float
    :param tz: timezone; format: str("Region/City")
    :return: datetime.datetime + utc
    """
    local_tz = pytz.timezone(tz)
    dt = local_tz.localize(datetime.utcfromtimestamp(moment_time))
    dt = dt.astimezone(pytz.timezone(tz))
    return dt


def add_hour_and_minute(dt):
    """
    Converts utc tail

    Converts utc tail to hours and minutes and
    adds to date and returns a new
    datetime object.datetime, the old one is deleted.

    :param dt: date and time; format: datetime.datetime
    :return: new datetime.datetime, old datetime deleted
    """
    h = int(str(dt.strftime('%z'))[:3])
    m = int(str(dt.strftime('%z'))[3:])
    dt = dt + timedelta(hours=h, minutes=m)
    return dt


def utc_convert(moment_time, tz, f=None):
    """
    Adds a time zone to the base time.

    :param moment_time: unix time; may be format: int, float
    :param tz: timezone; format: str("Region/City")
    :param f: template datetime.datetime; format: str("%a, %d %b %Y %H:%M:%S")
    :return: str("%a, %d %b %Y %H:%M:%S")
    """
    f = f or '%a, %d %b %Y %H:%M:%S'
    if not isinstance(f, str):
        raise ErrorFormatTemplate('f must be string in format template datetime.')
    dt = utc_(moment_time, tz=tz)
    dt = add_hour_and_minute(dt)
    return dt.strftime(f)


def utc_localize(moment_time, tz, f=None):
    """
    Outputs a localized time + utc tail.

    :param moment_time: unix time; may be format: int, float
    :param tz: timezone; format: str("Region/City")
    :param f: template datetime.datetime; format: str("%a, %d %b %Y %H:%M:%S %z(%Z)")
    :return: str("%a, %d %b %Y %H:%M:%S %z(%Z)")
    """
    dt = utc_(moment_time, tz=tz)
    f = f or '%a, %d %b %Y %H:%M:%S %z(%Z)'
    if not isinstance(f, str):
        raise ErrorFormatTemplate('f must be string in format template datetime.')
    return dt.strftime(f)
