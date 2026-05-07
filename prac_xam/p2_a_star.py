import heapq

g = {
    'A': {'B':1, 'C':3},
    'B': {'D':3},
    'C': {'D':1},
    'D': {}
}

h = {'A':4, 'B':2, 'C':1, 'D':0}

q = [(0,'A',0,['A'])]
v = []

while q:
    f,n,c,p = heapq.heappop(q)

    if n == 'D':
        print("Path =", p)
        print("Cost =", c)
        break

    v.append(n)

    for i in g[n]:
        if i not in v:
            x = c + g[n][i]
            heapq.heappush(q,(x+h[i],i,x,p+[i]))