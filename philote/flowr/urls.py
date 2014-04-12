# flowr.urls
# URL Controller for the flowr app
#
# Author:   Benjamin Bengfort <benjamin@bengfort.com>
# Created:  Sat Apr 12 11:45:38 2014 -0400
#
# Copyright (C) 2014 Bengfort.com
# For license information, see LICENSE.txt
#
# ID: urls.py [] benjamin@bengfort.com $

"""
URL Controller for the flowr app
"""

##########################################################################
## Imports
##########################################################################

from flowr.views import *
from django.conf.urls import patterns, url

##########################################################################
## URL Patterns
##########################################################################

urlpatterns = patterns('',
    url(r'^$', ActionsList.as_view(), name='action-index'),
    url(r'^(?P<pk>\d+)/$', ActionDetail.as_view(), name='action-detail'),
)
