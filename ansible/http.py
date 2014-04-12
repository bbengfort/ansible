# ansible.http
# Implements HTTP long polling using Twisted
#
# Author:   Benjamin Bengfort <benjamin@bengfort.com>
# Created:  Sat Apr 12 14:45:41 2014 -0400
#
# Copyright (C) 2014 Bengfort.com
# For license information, see LICENSE.txt
#
# ID: http.py [] benjamin@bengfort.com $

"""
Implements HTTP long polling using Twisted.

Uses an HTTP transport protocol as the base application.
"""

##########################################################################
## Imports
##########################################################################

import time
import json
import thread
import datetime

from ansible.ingestor import IngestorFactory
from twisted.web.resource import Resource
from twisted.internet import task
from twisted.web.server import NOT_DONE_YET

##########################################################################
## HTTP Resource
##########################################################################

class HttpIngestor(Resource):

    isLeaf = True

    def __init__(self):
        self.throttle = 1
        self.delayed_requests = []
        self.messages = {}
        self.factory = IngestorFactory()

        # Optimization
        loopingCall = task.LoopingCall(self.processDelayedRequests)
        loopingCall.start(self.throttle, False)

        self.factory.messages = self.messages

        Resource.__init__(self)

    def render_POST(self, request):
        request.setHeader('Content-Type', 'application/json')
        request.setHeader('Access-Control-Allow-Origin', '*')
        if 'new_message' in request.args:
            self.messages[float(time.time())] = request.args['new_message'][0]
            if len(self.factory.clients) > 0:
                self.factory.clients[0].updateClients(request.args['new_message'][0])
            self.processDelayedRequests()
        return ''

    def render_GET(self, request):
        request.setHeader('Content-Type', 'application/json')

        if 'callback' in request.args:
            request.jsonpcallback = request.args['callback'][0]

        if 'lastupdate' in request.args:
            request.lastupdate = float(request.args['lastupdate'][0])
        else:
            request.lastupdate = 0.0

        if request.lastupdate < 0:
            return self.format_response(request, 1, "connected ...", timestamp=0.0)

        data = self.getData(request)
        if data:
            return self.format_response(request, 1, data.message, timestamp=data.published_at)

        self.delayed_requests.append(request)
        return NOT_DONE_YET

    def getData(self, request):
        for published_at in sorted(self.messages):
            if published_at > request.lastupdate:
                return type('obj', (object,), {'published_at' : published_at, "message": self.messages[published_at]})();
        return

    def processDelayedRequests(self):
        for request in self.delayed_requests:
            data = self.getData(request)

            if data:
                try:
                    request.write(self.format_response(request, 1, data.message, data.published_at))
                    request.finish()
                except:
                    print 'connection lost before complete.'
                finally:
                    self.delayed_requests.remove(request)

    def format_response(self, request, status, data, timestamp=float(time.time())):
        response = json.dumps({'status':status,'timestamp': timestamp, 'data':data})

        if hasattr(request, 'jsonpcallback'):
            return request.jsonpcallback+'('+response+')'
        else:
            return response
