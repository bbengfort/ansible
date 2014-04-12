# tests
# Testing package for the Ansible library
#
# Author:   Benjamin Bengfort <benjamin@bengfort.com>
# Created:  Sat Apr 12 11:07:04 2014 -0400
#
# Copyright (C) 2014 Bengfort.com
# For license information, see LICENSE.txt
#
# ID: __init__.py [] benjamin@bengfort.com $

"""
Testing package for the Ansible library
"""

##########################################################################
## Imports
##########################################################################

import unittest

##########################################################################
## Initialization Tests
##########################################################################

class InitializationTests(unittest.TestCase):
    """
    Ensure that our testing package is ready
    """

    def test_sanity(self):
        """
        Assert the world is sane and 2+2=4
        """
        self.assertEqual(2+2, 4)

    def test_import(self):
        """
        We are able to import our library?
        """
        try:
            import ansible
        except ImportError:
            self.fail("Unable to import the ansible library!")
