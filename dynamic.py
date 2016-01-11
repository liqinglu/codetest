"""

direction weighted graph

solved by iter and nest two ways

"""

def memo(func):
    cache = {}
    def mefunc(*args):
        if args not in cache:
            cache[args] = func(*args)
        return cache[args]
    return mefunc

def calc_fib(W,s,t):
    @memo
    def d(u):
        if u == t: 
            return 0
        return min(W[u][v]+d(v) for v in W[u])
    return d(s)

"""
def calc_fib(W,s,t):
    d = {u:float('inf') for u in W}
    d[s] = 0
    for u in W:
        if u == t:
            break
        for v in W[u]:
            d[v] = min(d[v],d[u]+W[u][v])
    return d[t]
"""

if __name__ == "__main__":
    W={0:{5:9,1:2},1:{2:1,3:2,5:6},2:{3:7},3:{4:2,5:3},4:{5:4},5:{}}
    s,t = 0,5
    print calc_fib(W,s,t)
