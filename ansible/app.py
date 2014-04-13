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

from ingestor import *
from generate import *
from twisted.internet import reactor

##########################################################################
## Runables
##########################################################################

DPORT = 1025    # Default Port

class App(object):
    """
    A class wrapper for the Ansible App
    """

    Factory = IngestorFactory

    def __init__(self, port=DPORT):
        self.port    = port

    def run(self):
        reactor.listenTCP(self.port, self.Factory())
        reactor.run()

class Connection(object):
    """
    A client connector to the app.
    """

    Factory = None

    def __init__(self, host, port=DPORT):
        self.host = host
        self.port = port

    def run(self):
        reactor.connectTCP(self.host, self.port, self.Factory())
        reactor.run()

class Generator(Connection):
    """
    A class wrapper for the Sensor simulator
    """

    Factory = GeneratorFactory

if __name__ == '__main__':
    app = App()
    app.run()
