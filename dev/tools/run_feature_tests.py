from angela2 import *
from angela2.tests.features import *
from angela2.tests.features.base import *
from angela2.tests.features.monitors import SpikeMonitorTest, StateMonitorTest
from angela2.tests.features.input import SpikeGeneratorGroupTest

# Full testing
print(run_feature_tests().tables_and_exceptions)

# Quick testing
# print run_feature_tests(configurations=[DefaultConfiguration,
#                                         NumpyConfiguration],
#                         feature_tests=[SpikeGeneratorGroupTest]).tables_and_exceptions

# Specific testing
#from angela2.tests.features.synapses import SynapsesSTDP, SynapsesPost
#print run_feature_tests(feature_tests=[SynapsesPost]).tables_and_exceptions
#print run_feature_tests(feature_tests=[SynapsesPost],
#                        configurations=[DefaultConfiguration]).exceptions
