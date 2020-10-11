'''
Generate the angela2/default_preferences file automatically from the default
values registered when you import angela.
'''

import os
import angela2

base, _ = os.path.split(angela2.__file__)
fname = os.path.join(base, 'default_preferences')

with open(fname, 'w') as f:
    f.write(angela2.prefs.as_file)
