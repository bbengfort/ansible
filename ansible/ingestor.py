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

import json

from datetime import datetime
from collections import defaultdict
from twisted.protocols import basic
from twisted.internet.protocol import Factory

HISTORY = 10

def get_timestamp(fmt="%Y-%m-%d %H:%M:%S"):
    return datetime.now().strftime(fmt)

def parse_action(line):
    action, value = line.split()
    return action.upper(), float(value)

class Ingestor(basic.LineReceiver):

    def __init__(self, factory):
        self.factory = factory

    def connectionMade(self):
        print "[%s] client connected" % get_timestamp()
        self.factory.clients.append(self)
        self.sendLine(self.json_state())

    def connectionLost(self, reason):
        print "[%s] client disconnected" % get_timestamp()
        if self in self.factory.clients:
            self.factory.clients.remove(self)

    def lineReceived(self, line):
        print "[%s] recieved: \"%s\"" % (get_timestamp(), line)
        action, value = parse_action(line)
        self.factory.actions[action].append(value)
        if len(self.factory.actions[action]) > HISTORY:
            self.factory.actions[action] = self.factory.actions[action][-1 * HISTORY:]
        self.broadcast()

    def broadcast(self, message=None):
        message = message or self.json_state()
        for protocol in self.factory.clients:
            if protocol != self:
                protocol.sendLine(message)

    def json_state(self):
        return json.dumps(self.factory.actions)

class IngestorFactory(Factory):

    def __init__(self):
        self.clients = []
        self.actions = defaultdict(list)

    def buildProtocol(self, addr):
        return Ingestor(self)

