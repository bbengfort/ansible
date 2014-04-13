# ansible.client
# Data Generators
#
# Author:   Benjamin Bengfort <benjamin@bengfort.com>
# Created:  Sat Apr 12 23:57:12 2014 -0400
#
# Copyright (C) 2014 Bengfort.com
# For license information, see LICENSE.txt
#
# ID: client.py [] benjamin@bengfort.com $

"""
Data Generators - simulates incoming data from sensors.
"""

##########################################################################
## Imports
##########################################################################

import time
import random
import string

from ingestor import get_timestamp
from twisted.internet import reactor, protocol
from twisted.internet.task import deferLater
from twisted.internet.protocol import ClientFactory
from twisted.internet.error import ReactorNotRunning

##########################################################################
## Generator Protocol
##########################################################################

NL = "\r\n"

def random_action():
    a = random.choice(string.ascii_uppercase)
    b = random.choice('AEIOU')
    c = random.choice(string.ascii_uppercase)
    return a+b+c

class GeneratorClient(protocol.Protocol):

    def __init__(self, action=None, **kwargs):
        self.action = action or random_action()
        self.value  = random.random() * 100

    def connectionMade(self):
        print "[%s] connection made" % get_timestamp()
        self.generate()

    def sendLine(self, line):
        print "[%s] sending: \"%s\"" % (get_timestamp(), line)
        self.transport.write(line + NL)

    def dataReceived(self, data):
        pass

    def defer(self):
        defer = deferLater(reactor, 1, lambda: None)
        defer.addErrback(self.onerror)
        defer.addCallback(self.generate)
        return defer

    def onerror(self, failure):
        failure.trap(Exception)
        self.loseConnection()

    def generate(self, increment=None):
        increment = increment or random.random() * 10
        increment = increment * -1 if random.randrange(2) > 0 else increment
        self.value += increment
        self.send_action()
        self.defer()

    def send_action(self):
        self.sendLine("%s %0.3f" % (self.action, self.value))

class GeneratorFactory(ClientFactory):

    def buildProtocol(self, addr):
        return GeneratorClient()

    def clientConnectionFailed(self, connector, reason):
        self.shutdown()

    def clientConnectionLost(self, connector, reason):
        self.shutdown()

    def shutdown(self):
        print "[%s] connection lost" % get_timestamp()
        try:
            reactor.stop()
        except ReactorNotRunning:
            pass

if __name__ == '__main__':
    factory = GeneratorFactory()
    reactor.connectTCP('127.0.0.1', 1025, factory)
    reactor.run()
