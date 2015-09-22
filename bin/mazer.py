#!/usr/bin/env python
# mazer
# Executable Script for the Ansible Software
#
# Author:   Benjamin Bengfort <benjamin@bengfort.com>
# Created:  Sun Apr 13 10:26:18 2014 -0400
#
# Copyright (C) 2014 Bengfort.com
# For license information, see LICENSE.txt
#
# ID: mazer.py [] benjamin@bengfort.com $

"""
Executable Script for the Ansible Software
"""

##########################################################################
## Imports
##########################################################################

import os
import sys
import argparse
from ansible import *

config = {
    'description': 'Run Ansible servers and clients from the command line.',
    'epilog': 'This is just a simple demo, use twistd in the future'
}

##########################################################################
## Handlers
##########################################################################

def serve(options):
    app = App(options.port)
    app.run()

def generate(options):
    app = Generator(options.host, options.port)
    app.run()

##########################################################################
## Main Method
##########################################################################

def main(*argv):

    handler = {
        'listen': serve,
        'generate': generate,
    }

    parser  = argparse.ArgumentParser(**config)
    parser.add_argument('-H', '--host', type=str, default='127.0.0.1', help='Ansible host to connect to.')
    parser.add_argument('-P', '--port', type=int, default=1025, help='Ansible port to connect on.')
    parser.add_argument('command', choices=handler.keys(), nargs=1, help='Specify the Ansible action.')
    options = parser.parse_args()

    command = handler[options.command[0]]
    command(options)

if __name__ == '__main__':
    main(*sys.argv)
