'''
A dummy package to allow importing numpy and the unit-aware replacements of
numpy functions without having to know which functions are overwritten.

This can be used for example as ``import angela2.numpy_ as np``
'''

from numpy import *
from angela2.units.unitsafefunctions import *

# These will not be imported with a wildcard import to not overwrite the
# builtin names (mimicking the numpy behaviour)
from builtins import bool, int, float, complex, object, bytes, str

from numpy.core import round, abs, max, min

import numpy
import angela2.units.unitsafefunctions as angela2_functions
__all__ = []
__all__.extend(numpy.__all__)
__all__.extend(angela2_functions.__all__)
