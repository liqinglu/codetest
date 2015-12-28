"""
classic puzzle problem

find all possible path from an array, entrance is (0,0), exit is (m,n)
"""
import logging
import logging.config

logging.config.fileConfig("mylogger.conf")
logger = logging.getLogger("puzzle02logger")

#
#def outpuzzle(pz,tr,v,curr=(0,0),prev=None):
#    if curr[0] > len(pz[0]) - 1 or curr[1] > len(pz) -1: # if border
#        return
#    #elif tr[curr[0]][curr[1]] == 1:
#    #    return
#
#    #print curr
#    #tr[curr[0]][curr[1]] = 1
#    if curr[0] == len(pz[0]) - 1 and curr[1] == len(pz) - 1: # end point
#        yield [curr]
#    else:
#        probe = [(curr[0]+1,curr[1]),
#                (curr[0],curr[1]+1),
#                (curr[0]-1,curr[1]),
#                (curr[0],curr[1]-1)]
#        for eachtry in probe:
#            if eachtry == curr:
#                continue
#            if 0 <= eachtry[0] <= len(pz[0])-1 and 0 <= eachtry[1] <= len(pz) -1:
#                for c in outpuzzle(pz,tr,pz[eachtry[0]][eachtry[1]],eachtry,curr):
#                    if curr in c:
#                        continue
#                    else:
#                        c.insert(0,curr)
#                        yield c
#
#def main():
#    #puzzle = [[1,2,3,4],[5,4,6,2],[3,1,7,8],[9,2,3,4]]
#    puzzle = [[1,2],[5,4]]
#    #puzzle = [[3,5]]
#    trail = [ [ 0 for x in range(len(puzzle[0])) ] for y in range(len(puzzle)) ]
#
#    #print trail
#    for i in outpuzzle(puzzle,trail,puzzle[0][0],(0,0)):
#        print i

from calculatemin import calculate

class cell(object):
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.orientation = 0
    def neworitation(self):
        logger.debug('in cell class, next direction is %d'%(self.orientation+1))
        relativeoffset = {1:(1,0),2:(0,-1),3:(-1,0),4:(0,1)}
        self.orientation += 1
        return (self.x + relativeoffset[self.orientation][0],
                self.y + relativeoffset[self.orientation][1])

def outpuzzle(pz):
    if len(pz) == 1:
        return

    stack = []
    stack.append(cell(0,0))
    calcmin = calculate()
    while(stack):
        curcell = stack[-1]
        if curcell.x == len(pz[0]) - 1 and curcell.y == len(pz) - 1:
            logger.info('got one path')
            calcmin.calcsum([(point.x,point.y) for point in stack],pz)
            #print [(point.x,point.y) for point in stack]
            # break
            stack.pop()
        elif curcell.orientation < 4:
            logger.info('find another direction')
            nncell = curcell.neworitation()
            if nncell[0] in range(len(pz[0])) and nncell[1] in range(len(pz)):
                if (nncell not in [(cl.x,cl.y) for cl in stack]):
                    stack.append(cell(nncell[0],nncell[1]))
        else:
            logger.info('four direction already, stack pop')
            stack.pop()

    calcmin.findmin()

def main():
    puzzle = [[1,2,3,4],[5,4,6,2],[3,1,7,8],[9,2,3,4]]
    #puzzle = [[1,2,3],[5,4,6],[3,1,7]]
    #puzzle = [[1,2],[5,4]]
    logger.warning('puzzle is %s'%puzzle)
    outpuzzle(puzzle)

if __name__ == "__main__":
    main()
