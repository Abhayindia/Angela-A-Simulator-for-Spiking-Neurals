
import numpy as np
from numpy.testing import assert_allclose as numpy_allclose

from angela2 import prefs
from angela2.units.fundamentalunits import have_same_dimensions


def assert_allclose(actual, desired, rtol=4.5e8, atol=0, **kwds):
    '''
    Thin wrapper around numpy's `~numpy.testing.utils.assert_allclose` function. The tolerance depends on the floating
    point precision as defined by the `core.default_float_dtype` preference.

    Parameters
    ----------
    actual : `numpy.ndarray`
        The results to check.
    desired : `numpy.ndarray`
        The expected results.
    rtol : float, optional
        The relative tolerance which will be multiplied with the machine epsilon of the type set as
        `core.default_float_type`.
    atol : float, optional
        The absolute tolerance
    '''
    assert have_same_dimensions(actual, desired)
    eps = np.finfo(prefs['core.default_float_dtype']).eps
    rtol = eps*rtol
    numpy_allclose(np.asarray(actual), np.asarray(desired), rtol=rtol, atol=atol, **kwds)
