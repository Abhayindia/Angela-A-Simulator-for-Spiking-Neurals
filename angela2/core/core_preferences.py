'''
Definitions, documentation, default values and validation functions for core
angela preferences.
'''

from numpy import float32, float64, int32

from angela2.core.preferences import angelaPreference, prefs

__all__ = []


def dtype_repr(dtype):
    return dtype.__name__


def default_float_dtype_validator(dtype):
    return dtype in [float32, float64]


prefs.register_preferences('core', 'Core angela preferences',
    default_float_dtype=angelaPreference(
        default=float64,
        docs='''
        Default dtype for all arrays of scalars (state variables, weights, etc.).
        ''',
        representor=dtype_repr,
        validator=default_float_dtype_validator,
        ),
    default_integer_dtype=angelaPreference(
        default=int32,
        docs='''
        Default dtype for all arrays of integer scalars.
        ''',
        representor=dtype_repr,
        ),
    outdated_dependency_error=angelaPreference(
        default=True,
        docs='''
        Whether to raise an error for outdated dependencies (``True``) or just
        a warning (``False``).
        '''
        )
    )

prefs.register_preferences('legacy', 'Preferences to enable legacy behaviour',
    refractory_timing=angelaPreference(
        default=False,
        docs='''
        Whether to use the semantics for checking the refractoriness condition
        that were in place up until (including) version 2.1.2. In that
        implementation, refractory periods that were multiples of dt could lead
        to a varying number of refractory timesteps due to the nature of
        floating point comparisons). This preference is only provided for exact
        reproducibility of previously obtained results, new simulations should
        use the improved mechanism which uses a more robust mechanism to
        convert refractoriness into timesteps. Defaults to ``False``.
        ''')
    )