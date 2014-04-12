# flowr.admin
# Register models with the Django Admin
#
# Author:   Benjamin Bengfort <benjamin@bengfort.com>
# Created:  Sat Apr 12 11:50:06 2014 -0400
#
# Copyright (C) 2014 Bengfort.com
# For license information, see LICENSE.txt
#
# ID: admin.py [] benjamin@bengfort.com $

"""
Register models with the Django Admin
"""

##########################################################################
## Imports
##########################################################################

from flowr.models import Action
from django.contrib import admin

##########################################################################
## Model Registration
##########################################################################

admin.site.register(Action)
