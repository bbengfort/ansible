# flowr.views
# Views for the flowr app
#
# Author:   Benjamin Bengfort <benjamin@bengfort.com>
# Created:  Sat Apr 12 11:50:49 2014 -0400
#
# Copyright (C) 2014 Bengfort.com
# For license information, see LICENSE.txt
#
# ID: views.py [] benjamin@bengfort.com $

"""
Views for the flowr app
"""

##########################################################################
## Imports
##########################################################################

from flowr.models import *
from django.views.generic import ListView, DetailView

##########################################################################
## Views
##########################################################################

class ActionsList(ListView):

    model = Action

class ActionDetail(DetailView):

    model = Action
