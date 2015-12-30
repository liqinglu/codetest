from __future__ import division
import sys

"""
A simple calculater
"""

class interpreter(object):
    def __init__(self,expr):
        self.expr = expr
    def gotit(self):
        seperators = ['+','-','*','/','(',')']
        seps = []
        oprs = []
        #parentflag = 0

        epr = self.expr.strip().replace(' ','')
        initialpos = 0
        for i in xrange(len(epr)):
            #if epr[i] is '(':
            #    parentflag = 1
            #    continue
            #if epr[i] is ')':
            #    parentflag = 0
            #    continue
            if epr[i] in seperators:
                seps.append(epr[i])
                oprs.append(''.join(epr[initialpos:i]))
                if not oprs[-1].isdigit():
                    print "input error"
                    return
                initialpos = i+1
            if i == len(epr)-1:
                oprs.append(''.join(epr[initialpos:]))
                if not oprs[-1].isdigit():
                    print "input error"
                    return

        #if parentflag > 0:
        #    print "input error"
        #    return
        #print "seps : %s"%seps
        #print "oprs : %s"%oprs
        return self.calc(seps,oprs)
    def calc(self,sep,opr):
        highrank = ['*','/']
        lowrank = ['+','-']
        if len(list(set(highrank).intersection(set(sep)))) and len(list(set(lowrank).intersection(set(sep)))): # have "*","/" ; also have "+","-"
            while len(list(set(highrank).intersection(set(sep)))) > 0:
                for i in xrange(len(sep)):
                    if sep[i] in highrank:
                        tmp = []
                        tmp.append(opr[i])
                        tmp.append(sep[i])
                        tmp.append(opr[i+1])
                        res = eval(''.join(tmp))
                        sep.pop(i)
                        opr[i] = str(res)
                        opr.pop(i+1)
                        break
            #print sep
            #print opr
        # only '+" and "-" exist now
        tmp = []
        tmp.append(opr.pop(0))
        while len(sep)>0:
            tmp.append(sep.pop(0))
            tmp.append(opr.pop(0))
            res = eval(''.join(tmp))
            tmp.pop()
            tmp.pop()
            tmp.pop()
            tmp.append(str(res))

        return tmp[0]

def main():
    while 1:
        incalc = raw_input("calc>>>")
        if incalc in ["exit","quit","q"]:
            sys.exit()
        elif len(incalc)==0:
            continue

        exprinc = interpreter(incalc)
        print exprinc.gotit()
        del exprinc

def test():
    pass

if __name__ == "__main__":
    if len(sys.argv) == 2 and sys.argv[1] == 'test':
        test()
    elif len(sys.argv) == 1:
        main()
    else:
        print "Usage: "
        print " python <program>"
        print " python <program> test"
