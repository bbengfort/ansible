# flowr.models
# Database models for various actions
#
# Author:   Benjamin Bengfort <benjamin@bengfort.com>
# Created:  Sat Apr 12 11:48:19 2014 -0400
#
# Copyright (C) 2014 Bengfort.com
# For license information, see LICENSE.txt
#
# ID: models.py [] benjamin@bengfort.com $

"""
Database models for various actions
"""

##########################################################################
## Imports
##########################################################################

from django.db import models

##########################################################################
## Models
##########################################################################

class Action(models.Model):

    name = models.CharField(max_length=255)

    def __unicode__(self):
        return self.name
