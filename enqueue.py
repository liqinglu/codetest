"""
There is a queue, people can line up behind the queue or insert into the queue, but all people whose rank in queue impacted will be notified

It use publish-subscrible mode
"""

import os
import random

class center(object):
    def __init__(self):
        self.msgcenter = []
    def output(self):
        for i in self.msgcenter:
            print "name : %s , rank : %d"%(i.name,i.rank)
    def update(self,insertobject):
        print "%s insert to rank %d"%(insertobject.name,insertobject.rank)
        print
        self.msgcenter.insert(insertobject.rank-1,insertobject)

        for i in self.msgcenter[insertobject.rank:]:
            i.rank += 1
            i.notify(i.rank)

class people(object):
    def __init__(self,name):
        self.name = name
        self.rank = 0
        self.ctr = None
    def behindqueue(self,ctr):
        self.ctr = ctr
        self.rank = len(self.ctr.msgcenter) + 1
        self.ctr.msgcenter.append(self)
    def insertqueue(self,ctr):
        self.ctr = ctr
        if len(self.ctr.msgcenter) == 0:
            self.behindqueue(ctr)
            return

        self.rank = random.randint(1,len(self.ctr.msgcenter))
        self.ctr.update(self)
    def notify(self,current):
        print "I'm %s, now I am in rank %d"%(self.name,current)

def main():
    ctr = center()
    zs = people('zs')
    zs.behindqueue(ctr)
    lw = people('lw')
    lw.behindqueue(ctr)
    wl = people('wl')
    wl.behindqueue(ctr)
    wbs = people('wbs')
    wbs.insertqueue(ctr)
    #ctr.output()

if __name__ == "__main__":
    main()
