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

import json

from flowr.models import *
from ansible import connect
from django.conf import settings
from django.http import HttpResponse
from django.views.generic import View, ListView, DetailView

##########################################################################
## JSONResponse Utility
##########################################################################

class JSONResponse(HttpResponse):

    def __init__(self, content, **kwargs):
        kwargs['content_type'] = 'application/json'
        content = json.dumps(content)
        super(JSONResponse, self).__init__(content, **kwargs)

##########################################################################
## Views
##########################################################################

class ActionsList(ListView):

    model = Action

class ActionDetail(DetailView):

    model = Action

class AnsibleView(View):

    def get(self, request):
        host = settings.ANSIBLE_HOST
        port = settings.ANSIBLE_PORT
        tmot = settings.ANSIBLE_TIMEOUT
        try:
            with connect(host, port, timeout=tmot) as conn:
                return JSONResponse(conn.fetch())
        except Exception as e:
            return JSONResponse({'error': str(e)})
