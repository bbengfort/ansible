# philote.settings.production
# Production settings for Philote
#
# Author:   Benjamin Bengfort <benjamin@bengfort.com>
# Created:  Sat Apr 12 11:31:05 2014 -0400
#
# Copyright (C) 2014 Bengfort.com
# For license information, see LICENSE.txt
#
# ID: production.py [] benjamin@bengfort.com $

"""
Production settings for Philote
"""

##########################################################################
## Imports
##########################################################################

from .base import *

##########################################################################
## Production Settings
##########################################################################

## Debugging Settings
DEBUG            = False
TEMPLATE_DEBUG   = False

## Hosts
ALLOWED_HOSTS    = []   # Must set!

## Content
STATIC_ROOT      = "/var/www/philote/static/"
MEDIA_ROOT       = "/var/www/philote/media/"
