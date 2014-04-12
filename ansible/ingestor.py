# ansible.ingestor
# The Basic LineReceiver Protocol for ingesting action predicates.
#
# Author:   Benjamin Bengfort <benjamin@bengfort.com>
# Created:  Sat Apr 12 12:22:23 2014 -0400
#
# Copyright (C) 2014 Bengfort.com
# For license information, see LICENSE.txt
#
# ID: ingestor.py [] benjamin@bengfort.com $

"""
The Basic LineReceiver Protocol for ingesting action predicates.

Right now, just implementing websockets using Twisted...
"""

##########################################################################
## Imports
##########################################################################

import time

from twisted.protocols import basic
from twisted.internet.protocol import Factory

class Ingestor(basic.LineReceiver):

    def connectionMade(self):
        print "Got new client!"
        self.transport.write('connected ...\n')
        self.factory.clients.append(self)

    def connectionLost(self, reason):
        print "Lost a client!"
        self.factory.clients.remove(self)

    def dataReceived(self, data):
        print "received", repr(data)
        self.factory.messages[float(time.time())] = data
        self.updateClients(data)

    def updateClients(self, data):
        for client in self.factory.clients:
            client.message(data)

    def message(self, message):
        self.transport.write("message" + "\n")

class IngestorFactory(Factory):

    protocol = Ingestor
    clients  = []
    messages = {}
