# philote.settings.development
# Development settings for Philote
#
# Author:   Benjamin Bengfort <benjamin@bengfort.com>
# Created:  Sat Apr 12 11:30:41 2014 -0400
#
# Copyright (C) 2014 Bengfort.com
# For license information, see LICENSE.txt
#
# ID: development.py [] benjamin@bengfort.com $

"""
Development settings for Philote
"""

##########################################################################
## Imports
##########################################################################

from .base import *

##########################################################################
## Development Settings
##########################################################################

## Debugging Settings
DEBUG            = True
TEMPLATE_DEBUG   = True

## Hosts
ALLOWED_HOSTS    = ('127.0.0.1', 'localhost')

## Secret Key doesn't matter in Dev
SECRET_KEY = 'anspap!yf)+@$*rli4!icf(7vxx1nh9*ro*1ro&9bgo^v+&-rowf$ible'
