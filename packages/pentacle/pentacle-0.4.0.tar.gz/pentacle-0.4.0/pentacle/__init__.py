# Pentacle O-O P2P RPC
#
# Copyright (C) 2011-2023 Thetaplane
# Author: Thetaplane <cbanis@gmail.com>

'''\
Object-Oriented Peer-to-Peer RPC access library and server application framework.

:Author: `%(__author__)s <%(__author_email__)s>`__
:Requires: Python 2.6+
:Version: %(__version__)s

:Group Application: application, config, debugging, security, storage
:Group Core: architecture, encoding, packaging, runtime
:Group Networking: network, client, server
:Group Service Partner Bus: bus, bus.partners, bus.services, bus.spline

:Bug: Some synchronization issues cause intermittant network failures
:Todo: Optimize the package format to eliminate unnecessary marks

:Copyright: |copyright| %(__copyright__)s
.. |copyright| unicode:: 0xA9 .. copyright sign
'''

__author__ = 'Thetaplane' # __contact__
__author_email__ = 'cbanis@gmail.com'
__copyright__ = '2011-2023 Thetaplane' # __license__

__version__ = '0.4.0'
__docformat__ = 'restructuredtext en'

__url__ = 'http://thetaplane.com'
__doc__ = __doc__ % vars()

def buildApplicationVersion(appName, busVersion):
    return '%s/%s' % (appName, busVersion)

# Yeah, this is for me:
def DEBUG(*args):
    pass # print '[DEBUG]', ' '.join(map(str, args))

import builtins as builtin
builtin.DEBUG = DEBUG
