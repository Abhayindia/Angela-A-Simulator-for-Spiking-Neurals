'''
A dummy package to allow wildcard import from angela2 without also importing
the pylab (numpy + matplotlib) namespace.

Usage: ``from angela2.only import *``

'''
# To minimize the problems with imports, import the packages in a sensible
# order

# The units and utils package does not depend on any other angela package and
# should be imported first

from angela2.units import *
from angela2.utils import *
from angela2.core.tracking import *
from angela2.core.names import *
from angela2.core.spikesource import *

# The following packages only depend on something in the above set
from angela2.core.variables import linked_var
from angela2.core.functions import *
from angela2.core.preferences import *
from angela2.core.clocks import *
from angela2.equations import *

# The base class only depends on the above sets
from angela2.core.base import *

# The rest...
from angela2.core.network import *
from angela2.core.magic import *
from angela2.core.operations import *
from angela2.stateupdaters import *
from angela2.codegen import *
from angela2.core.namespace import *
from angela2.groups import *
from angela2.groups.subgroup import *
from angela2.synapses import *
from angela2.monitors import *
from angela2.importexport import *
from angela2.input import *
from angela2.spatialneuron import *
from angela2.devices import set_device, get_device, device, all_devices, seed
import angela2.devices.cpp_standalone as _cpp_standalone

# preferences
import angela2.core.core_preferences as _core_preferences
prefs.load_preferences()
prefs.do_validation()

prefs._backup()

set_device(all_devices['runtime'])

def restore_initial_state():
    '''
    Restores internal angela variables to the state they are in when angela is imported

    Resets ``defaultclock.dt = 0.1*ms``, 
    `angelaGlobalPreferences._restore` preferences, and set
    `angelaObject._scope_current_key` back to 0.
    '''
    import gc
    prefs._restore()
    angelaObject._scope_current_key = 0
    defaultclock.dt = 0.1*ms
    gc.collect()

# make the test suite available via angela2.test()
from angela2.tests import run as test

from angela2.units import __all__ as _all_units

__all__ = [
    'get_logger', 'angelaLogger', 'std_silent',
    'Trackable',
    'Nameable',
    'SpikeSource',
    'linked_var',
    'DEFAULT_FUNCTIONS', 'Function', 'implementation', 'declare_types',
    'PreferenceError', 'angelaPreference', 'prefs', 'angela_prefs',
    'Clock', 'defaultclock',
    'Equations', 'Expression', 'Statements',
    'angelaObject',
    'angelaObjectException',
    'Network', 'profiling_summary', 'scheduling_summary',
    'MagicNetwork', 'magic_network',
    'MagicError',
    'run', 'stop', 'collect', 'store', 'restore',
    'start_scope',
    'NetworkOperation', 'network_operation',
    'StateUpdateMethod',
    'linear', 'exact', 'independent',
    'milstein', 'heun', 'euler', 'rk2', 'rk4', 'ExplicitStateUpdater',
    'exponential_euler',
    'gsl_rk2', 'gsl_rk4', 'gsl_rkf45', 'gsl_rkck', 'gsl_rk8pd',
    'NumpyCodeObject', 'CythonCodeObject',
    'get_local_namespace', 'DEFAULT_FUNCTIONS', 'DEFAULT_UNITS',
    'DEFAULT_CONSTANTS',
    'CodeRunner', 'Group', 'VariableOwner', 'NeuronGroup',
    'Subgroup',
    'Synapses',
    'SpikeMonitor', 'EventMonitor', 'StateMonitor',
    'PopulationRateMonitor',
    'ImportExport',
    'BinomialFunction', 'PoissonGroup', 'PoissonInput',
    'SpikeGeneratorGroup', 'TimedArray',
    'Morphology', 'Soma', 'Cylinder', 'Section', 'SpatialNeuron',
    'set_device', 'get_device', 'device', 'all_devices', 'seed',
    'restore_initial_state'
]
__all__.extend(_all_units)
