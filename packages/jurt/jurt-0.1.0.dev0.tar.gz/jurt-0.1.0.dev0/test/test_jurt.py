"""Unit tests for jurt"""
# jurt: Jeff's Unified Registration Tool
#
# Copyright (c) 2018, Jeffrey M. Engelmann
#
# jurt is released under the revised (3-clause) BSD license.
# For details, see LICENSE.txt
#

import unittest
import jurt

class test_jurt(unittest.TestCase):
    """Test the jurt module"""

    def test_version(self):
        """Test that the correct version number is returned"""

        # Set the expected version string
        # This is automatically updated by bumpversion (see .bumpversion.cfg)
        version = '0.1.0.dev0'

        ver_tuple = jurt.version()
        ver_str = '%d.%d.%d' % ver_tuple[:3]
        if ver_tuple[3] is not None:
            ver_str += '.dev%d' % ver_tuple[3]

        self.assertEqual(version, ver_str)

if __name__ == '__main__':
    unittest.main()

