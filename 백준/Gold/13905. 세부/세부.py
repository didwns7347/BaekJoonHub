import sys
import heapq
a,b = map(int,input().split())
s,f = map(int,input().split())

costInfo = [ [] for _ in range(a+1) ]

for i in range(b):
    n,m,c = map(int, sys.stdin.readline().split())
    costInfo[n].append([m,c])
    costInfo[m].append([n,c])
    
costs = [0 for _ in range(a + 1 )] 
costs[s] = 1e9
q = []
heapq.heappush(q,[0,s])
while q:
    cost,now = heapq.heappop(q)
    # print(cost,now)
    cost = -cost

    for next,c in costInfo[now]:
        minCost = min(costs[now], c)
        if costs[next] < minCost:
            costs[next] = minCost
            heapq.heappush(q, [-cost,next])

print(costs[f])