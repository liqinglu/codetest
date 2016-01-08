"""

It is very similar with 'puzzle.py', which describe a non-direction weighted graph, our question is figure out the shortest path between random two points and their weights

"""

#def removeonedimension(ff,start,points):
#    ff.pop(start)
#    for row in ff:
#        row.pop(start)
#
#    points.pop(start)
#    return ff,points
#
#def minweight(start,end,points,matrix):
#    mindict = {}
#
#    # init first point from start
#    idstart = points.index(start)
#    idend = points.index(end)
#    for each in range(len(matrix[start])):
#        if each == start:
#            continue
#        eachkey = points[start] + points[each]
#        mindict[eachkey] = matrix[start][each]
#
#    # remove one dimension
#    matrix,points = removeonedimension(matrix,idstart,points)
#    # calculate in loop
#    while 1:
#        if len(matrix) == 1:
#            break
#        break
#
#    key = start + end
#    return mindict[key]

class point(object):
    def __init__(self,name,m,pois):
        self.name = name
        self.m = m
        self.points = pois
        self.candidate = self._getcandidatepath()
    def hasnewpath(self):
        return len(self.candidate) > 0
    def getnewpath(self):
        return self.candidate.pop(0)
    def _getcandidatepath(self):
        ret = []
        idname = self.points.index(self.name)
        for ids,value in enumerate(self.m[idname]):
            if value > 0:
                ret.append(self.points[ids])

        return ret

def getminvalue(lst, who, mx):
    sumvalue = 0
    for rank in range(len(lst)-1):
        one = lst[rank]
        another = lst[rank+1]
        idone = who.index(one.name)
        idanother = who.index(another.name)
        sumvalue += mx[idone][idanother]

    return sumvalue

def minweight(start,end,points,matrix):
    stack = []
    minvalue = 1000
    minlst = []
    stack.append(point(points[start],matrix,points))

    while(stack):
        curpoint = stack[-1]
        if curpoint.name == points[end]:
            gotvalue = getminvalue(stack,points,matrix)
            if gotvalue < minvalue:
                minvalue = gotvalue
                minlst = [ p.name for p in stack ]
            #print [ poi.name for poi in stack ]
            stack.pop()
        elif curpoint.hasnewpath():
            newpoint = curpoint.getnewpath()
            if newpoint not in [cp.name for cp in stack]:
                stack.append(point(newpoint,matrix,points))
        else:
            stack.pop()

    return minvalue,minlst

def main():
    A = [[0,10,0,0,0,9,15],
         [10,0,0,0,0,2,0],
         [0,0,0,0,1,0,10],
         [0,0,0,0,7,0,0],
         [0,0,1,7,0,0,12],
         [9,2,0,0,0,0,3],
         [15,0,10,0,12,3,0]]
    points = ['a','b','c','d','e','f','g'] # index from 0--6

    idstart = 0
    idend = 3
    print minweight(idstart,idend,points,A)

if __name__ == "__main__":
    main()
