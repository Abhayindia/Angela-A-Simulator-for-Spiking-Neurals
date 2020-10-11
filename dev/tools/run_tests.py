'''
Run all the non-standalone tests using pytest. Exits with error code 1 if a test failed.
'''
import sys

import angela2

if __name__ == '__main__':
    if not angela2.test():  # If the test fails, exit with a non-zero error code
        sys.exit(1)
