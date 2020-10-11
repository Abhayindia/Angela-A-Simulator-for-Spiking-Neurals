'''
Run all the Cython tests using pytest. Exits with error code 1 if a test failed.
'''
import sys

import angela2

if not angela2.test('cython'):  # If the test fails, exit with a non-zero error code
    sys.exit(1)
