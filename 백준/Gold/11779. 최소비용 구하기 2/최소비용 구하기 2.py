import sys
import heapq
cityNum = int(input())
busNum = int(input())

busInfo = [[] for _ in range(cityNum + 1)]


distAt = [1e9 for _ in range(cityNum + 1 )] 
minPath = [ [] for _ in range(cityNum + 1 )]
for i in range(busNum):
    a,b,cost = map(int,sys.stdin.readline().split())
    busInfo[a].append([b,cost])
    # busInfo[b].append([a,cost])

start,fin = map(int,input().split())

q = []

heapq.heappush(q,[0,start])
distAt[start] = 0

while q:
    # print(q)
    dist, now = heapq.heappop(q)
    if distAt[now] < dist :
        continue

    for info in busInfo[now]:
        cost = dist + info[1]

        if cost < distAt[info[0]]:
            distAt[info[0]] = cost
            minPath[info[0]] = minPath[now] + [info[0]]
            heapq.heappush(q,(cost,info[0]))

print(distAt[fin])
print(len(minPath[fin]) + 1)
print(" ".join(str(s) for s in [start] + minPath[fin]))
