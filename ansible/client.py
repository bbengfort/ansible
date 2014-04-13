# ansible.client
# A blocking client that can read data from the Twisted Server
#
# Author:   Benjamin Bengfort <benjamin@bengfort.com>
# Created:  Sun Apr 13 10:54:40 2014 -0400
#
# Copyright (C) 2014 Bengfort.com
# For license information, see LICENSE.txt
#
# ID: client.py [] benjamin@bengfort.com $

"""
A blocking client that can read data from the Twisted Server
"""

##########################################################################
## Imports
##########################################################################

import json
import socket

NL = "\r\n"

class AnsibleConnection(object):

    def __init__(self, host, port, timeout=3):
        self.host = host
        self.port = port
        self.timeout = timeout
        self.connect()

    def connect(self):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.connect((self.host, self.port))
        self.sock.settimeout(self.timeout)

    def close(self):
        self.sock.close()

    def fetch(self):
        """
        Returns JSON data from the server, if timeout, returns None.
        """
        data = ""
        while True:
            try:
                data += self.sock.recv(1024)
            except socket.timeout:
                return None

            if NL in data: break
        return json.loads(data)

    def __enter__(self):
        return self

    def __exit__(self, *args, **kwargs):
        self.close()

connect = AnsibleConnection

if __name__ == '__main__':
    with connect('localhost', 1025) as conn:
        for x in xrange(0, 10):
            print json.dumps(conn.fetch(), indent=2)

