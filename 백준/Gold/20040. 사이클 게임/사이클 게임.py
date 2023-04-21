n,m = map(int,input().split())
parents = [x for x in range(n+1)]

def find(a):
    if parents[a] == a:
        return a
    parents[a] = find(parents[a])
    return parents[a]
def union(a,b):
    a = find(a)
    b = find(b)
    if a < b:
        parents[b] = a

    else :
        parents[a] = b
answer = 0
for i in range(m):
    a,b = map(int,input().split())
    if find(a) == find(b):
        answer = i+1 
        break
    else:
        union(a,b)
print(answer)