try:
    __import__("numpy")
except ImportError:
    print "Could not load numpy module, exiting..."
    exit()

try:
    __import__("scipy")
except ImportError:
    print "Could not load scipy module, exiting..."
    exit()

import logging
import parser, forcefield, optimizer, objective

# set up package-wide logger
logging.forcebalanceLogger=logging.getLogger('forcebalance')
logging.forcebalanceLogger.addHandler(logging.NullHandler())