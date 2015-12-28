"""
How to use decorator
"""

import os
import datetime

def deco(fn):
    def _deco(name):
        print "<function name> : %s"%fn.__name__
        print "<function start>"
        tnow = datetime.datetime.now()
        fn(name)
        tdura = datetime.datetime.now() - tnow
        print "<function duration> : %s"%tdura
        print "<function end>"
    return _deco

@deco
def hello(name):
    print "hello,%s"%name
    
hello("liqinglu")
