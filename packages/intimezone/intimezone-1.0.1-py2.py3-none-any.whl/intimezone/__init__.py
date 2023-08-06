# -*- coding: utf8 -*-

from intimezone.convert import convert
from intimezone import Error
import intimezone.__about__ as about

__all__ = ['convert', 'Error', 'version']


version = about.__version__
