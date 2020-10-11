'''
Run all the numpy tests using pytest. Exits with error code 1 if a test failed.
'''
import sys

import angela2

if not angela2.test('numpy', test_codegen_independent=False):  # If the test fails, exit with a non-zero error code
    sys.exit(1)
