"""Utility classes and functions."""
from . import math
from . import inspect
from . import pretty
from .estimator_checks import check_estimator
from .histogram import Histogram
from .param_grid import expand_param_grid
from .sdft import SDFT
from .skyline import Skyline
from .vectordict import VectorDict
from .window import Window
from .window import SortedWindow
# Data convertion utilities: to be removed in the future
from .data_conversion import dict2numpy
from .data_conversion import numpy2dict


__all__ = [
    'check_estimator',
    'dict2numpy',
    'expand_param_grid',
    'inspect',
    'Histogram',
    'numpy2dict',
    'SDFT',
    'Skyline',
    'SortedWindow',
    'VectorDict',
    'Window'
]
