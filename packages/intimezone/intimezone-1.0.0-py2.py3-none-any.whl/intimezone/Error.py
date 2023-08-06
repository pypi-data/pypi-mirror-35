# -*- coding: utf8 -*-


__all__ = ['ErrorFormatTemplate', 'ErrorFormatTime',
           'ErrorFormatTimeZone', 'ErrorFlag']


class Except(Exception):
    """Base class"""


class ErrorFormatTime(Except):
    """The time does not meet the specified criteria"""


class ErrorFormatTemplate(Except):
    """The template does not meet the specified criteria"""


class ErrorFormatTimeZone(Except):
    """The timezone does not meet the specified criteria"""


class ErrorFlag(Except):
    """Flag value error"""
