import sys

def calc(sep,opr):
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

    print tmp[0]

def interpreter(expression):
    seperators = ['+','-']
    seps = []
    oprs = []

    epr = expression.strip().replace(' ','')
    initialpos = 0
    for i in xrange(len(epr)):
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

    #print "seps : %s"%seps
    #print "oprs : %s"%oprs
    calc(seps,oprs)

def main():
    while 1:
        incalc = raw_input(">>>")
        if incalc in ["exit","quit","q"]:
            sys.exit()
        elif len(incalc)==0:
            continue

        interpreter(incalc)

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
