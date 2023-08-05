"""Jeff's Unified Registration Tool

Facilitate coregistration and spatial normalization of fMRI datasets.
"""
#
# Copyright (c) 2018, Jeffrey M. Engelmann
#
# jurt is released under the revised (3-clause) BSD license.
# For details, see LICENSE.txt
#

def version():
    """Return a tuple containing the major, minor, patch, and dev numbers"""

    import re

    # Set the version string
    # This is automatically updated by bumpversion (see .bumpversion.cfg)
    version = '0.1.0.dev0'

    # Parse the version string and return it as a tuple
    # Let exceptions propagate
    pattern = '^(?P<major>\d+)\.(?P<minor>\d+)\.(?P<patch>\d+)(\.(?P<release>[a-z]+)(?P<dev>\d+))?$'
    m = re.match(pattern, version)
    v = (
        int(m['major']),
        int(m['minor']),
        int(m['patch']),
        int(m['dev']) if m['release'] == 'dev' else None)
    return v

if __name__ == '__main__':
    raise RuntimeError('jurt/__init__.py cannot be directly executed')

