# -*- coding: utf8 -*-

from intimezone.UTC import utc_convert
from intimezone.UTC import utc_localize
from intimezone.Error import ErrorFormatTimeZone
from intimezone.Error import ErrorFormatTime
from intimezone.Error import ErrorFlag

__all__ = ['convert']


# director
def convert(moment_time, tz='Etc/GMT+0', f=None, flag=None):
    """
    Converts incoming data to a date depending on the selected options.

    Can convert a unix date using the timezone.
    Converts to a localized date with utc tail,
    or add utc tail to the date itself.
    You can specify templates for the date that will be returned.

    :param moment_time: unix time; may be format: int, float
    :param tz: timezone; format: str("Region/City")
    :param f: template datetime.datetime; format: str("%a, %d %b %Y %H:%M:%S")
    :param flag:
        flag=None, "convert" - converts utc to a common date.
        flag="localize" - adds utc to the end of the shared date.
    :return: str("%a, %d %b %Y %H:%M:%S") + "%z(%Z)" or your datetime`s template

    Example:
    >>> convert(946684800, tz='Europe/London')
    Sat, 01 Jan 2000 00:00:00
    >>> convert(946684800, tz='Europe/Madrid', flag="convert")
    Sat, 01 Jan 2000 01:00:00
    >>> convert(946684800, tz='Europe/Moscow', flag="localize")
    Sat, 01 Jan 2000 00:00:00 +0300(MSK)
    """
    if not isinstance(moment_time, (float, int)):
        raise ErrorFormatTime('moment_time must be integer or float in format UTC.')
    if not isinstance(tz, str):
        raise ErrorFormatTimeZone('tz must be integer or float in format template "Region/city".')

    if flag is None or flag is 'convert':
        return utc_convert(moment_time, f=f, tz=tz)
    elif flag is 'localize':
        return utc_localize(moment_time, f=f, tz=tz)
    else:
        raise ErrorFlag('The flag is set incorrectly, can be: None, "convert", ""localize".')
