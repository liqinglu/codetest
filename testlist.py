"""
Use list expression to build a special list
"""

import os

n = 20

def whoisme(x,y):
    if x==y:
        return str(x)+'*'
    else:
        return x

testlist = [ [ whoisme(x,i) for x in range(1,n+1) ] for i in range(1,n+1) ]
print testlist
