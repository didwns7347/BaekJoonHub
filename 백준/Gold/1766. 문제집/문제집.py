import sys
import heapq

n, m = map(int,input().split())
indegree = [ 0 for _ in range(n+1)]

preSolved = [ [] for _ in range(n+1)]

for _ in range(m):
    a,b = map(int,sys.stdin.readline().split())
    preSolved[a].append(b)
    indegree[b] += 1
q = []


for i in range(1,n+1):
    if indegree[i] == 0 :
        heapq.heappush(q,i)
    
ans = ""
while q:
    node = heapq.heappop(q)
    ans = ans+str(node)+" "

    for nextable in preSolved[node]:
        indegree[nextable] -= 1
        if indegree[nextable] == 0:
            heapq.heappush(q,nextable)
print(ans)