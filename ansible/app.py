# ansible.app
# Sets up the application to run.
#
# Author:   Benjamin Bengfort <benjamin@bengfort.com>
# Created:  Sat Apr 12 12:28:13 2014 -0400
#
# Copyright (C) 2014 Bengfort.com
# For license information, see LICENSE.txt
#
# ID: app.py [] benjamin@bengfort.com $

"""
Sets up the application to run.
"""

##########################################################################
## Imports
##########################################################################

from ansible.http import *
from ansible.ingestor import *
from twisted.web.resource import Resource
from twisted.web.server import Site
from twisted.internet import protocol
from twisted.application import service, internet

class App(object):
    """
    A class wrapper for the Ansible App
    """

    def run(self):
        self.resource = HttpIngestor()
        self.factory  = Site(self.resource)
        self.root = self.resource()
        self.root.putChild("", self.resource)
        self.service = service.Application("ingestor")

        internet.TCPServer(1025, Site(self.root)).setServiceParent(self.service)


# Run via $ twistd -n -y app.py
resource = HttpIngestor()
factory  = Site(resource)
root = Resource()
root.putChild("", resource)
application = service.Application("ingestor")

internet.TCPServer(1025, Site(root)).setServiceParent(application)
