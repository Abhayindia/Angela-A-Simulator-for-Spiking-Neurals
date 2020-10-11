import os

import angela2

from setversion import setversion, setreleasedate
# Ask for version number
print('Current version is: ' + angela2.__version__)
version = input('Enter new angela2 version number: ').strip()

# Set the version numbers
print('Changing to new version', version)
setversion(version)
setreleasedate()
print('Done')

# generate the default preferences file
base, _ = os.path.split(angela2.__file__)
fname = os.path.join(base, 'default_preferences')
with open(fname, 'w') as f:
    f.write(angela2.prefs.as_file)

# commit
os.system('git commit -a -v -m "***** Release angela2 %s *****"' % version)
# add tag
os.system('git tag -a -m "Release angela2 %s" %s' % (version, version))

# print commands necessary for pushing
print('Review the last commit: ')
os.system('git show %s' % version)
print('')
print('To push, using the following command:')
print('git push --tags origin master')
