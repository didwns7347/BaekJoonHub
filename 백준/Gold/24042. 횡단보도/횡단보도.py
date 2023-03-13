import math
import heapq
import sys
n,m = map(int,input().split())
info = [[] for _ in range(n+1)]
for i in range(m):
    x,y = map(int,sys.stdin.readline().split())
    info[x].append([y,i])
    info[y].append([x,i])

dist = [ math.inf for _ in range(n+1)]
dist[1]=0
q = []
heapq.heappush(q,[0,1])
#print(q)
while q:
    time,node = heapq.heappop(q)
    #print(time,node)
    tmp = time % m
    if node == n:
        break
    for next,ntime in info[node]:
        cost = 0
        if tmp > ntime :
            cost = (m-tmp+ntime ) + 1
        else:
            cost = ntime -tmp + 1
        if dist[next] > time + cost:
            dist[next] = time + cost
            heapq.heappush(q,[dist[next],next])
        



#print(dist)
print(dist[n])