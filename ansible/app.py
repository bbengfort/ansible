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
from twisted.internet import reactor

class App(object):
    """
    A class wrapper for the Ansible App
    """

    Factory = IngestorFactory

    def __init__(self, port=1025):
        self.port    = port

    def run(self):
        reactor.listenTCP(self.port, self.Factory())
        reactor.run()

if __name__ == '__main__':
    app = App()
    app.run()
