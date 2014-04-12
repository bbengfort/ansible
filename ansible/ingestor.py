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

REGISTER = "REGISTER"
CHAT     = "CHAT"

class Ingestor(basic.LineReceiver):

    def __init__(self, factory):
        self.factory = factory
        self.name    = None
        self.state   = REGISTER

    def connectionMade(self):
        print "Got new client!"
        self.sendLine("What's your name?")

    def connectionLost(self, reason):
        print "Lost a client!"
        if self.name in self.factory.clients:
            del self.factory.clients[self.name]
            self.broadcast("%s has left the channel." % self.name)

    def lineReceived(self, line):
        print "recieved:", line
        if self.state == REGISTER:
            self.handle_registration(line)
        elif self.state == CHAT:
            self.handle_chat(line)
        else:
            raise Exception("Unknown State- '%s'!!!" % self.state)

    def broadcast(self, message):
        for name, protocol in self.factory.clients.iteritems():
            if protocol != self:
                protocol.sendLine(message)

    def handle_registration(self, name):
        if name in self.factory.clients:
            self.sendLine("Name taken, please choose another.")
            return
        self.sendLine("Welcome, %s!" % name)
        self.broadcast("%s has joined the channel." % name)
        self.name = name
        self.factory.clients[name] = self
        self.state = CHAT

    def handle_chat(self, message):
        message = "<%s> %s" % (self.name, message)
        self.broadcast(message)

class IngestorFactory(Factory):

    def __init__(self):
        self.clients = {}

    def buildProtocol(self, addr):
        return Ingestor(self)
