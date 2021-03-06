# philote.urls
# Main controller for the entire app
#
# Author:   Benjamin Bengfort <benjamin@bengfort.com>
# Created:  Sat Apr 12 11:43:09 2014 -0400
#
# Copyright (C) 2014 Bengfort.com
# For license information, see LICENSE.txt
#
# ID: urls.py [] benjamin@bengfort.com $

"""
Main controller for the entire app
"""

##########################################################################
## Imports
##########################################################################

from django.conf.urls import patterns, include, url
from django.views.generic import RedirectView
from django.contrib import admin

##########################################################################
## URL Patterns
##########################################################################


admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', RedirectView.as_view(url='/flowr/')),
    url(r'flowr/', include('flowr.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
