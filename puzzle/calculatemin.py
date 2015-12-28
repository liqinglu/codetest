import logging
import logging.config

logging.config.fileConfig("mylogger.conf")
logger = logging.getLogger("puzzle02logger")

class calculate(object):
    def __init__(self,number=1):
        self.allcomb = {}
        self.minrecordernumber = number
    def calcsum(self, lst, pz):
        logger.info("the list being calculated : %s"%lst)
        sum = 0
        for each in lst:
            #print "*** ",each
            sum += pz[each[0]][each[1]]
            #print "*** %d"%sum
        #print "sum is %d ( %s )"%(sum,lst)
        self.allcomb.setdefault(sum,[]).append(lst)
    def findmin(self):
        logger.info("find min combination")
        pathmin = sorted([x for x in self.allcomb.iterkeys()],reverse=False)
        #print "min path is %d"%pathmin[0]
        logger.warning("min path is %d"%pathmin[0])
        for i in self.allcomb[pathmin[0]]:
            #print i
            logger.warning("min combination is %s"%i)
