"""
One point: xrange instead of range in case of big number
"""

import os

for i in xrange(1,100000000):
    if not i%2:
        print i,
