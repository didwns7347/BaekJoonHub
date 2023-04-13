import sys
from collections import deque
sys.setrecursionlimit(200000)
n , m = map(int,input().split())
board=[]
check=[[0 for _ in range(m)] for _ in range(n)]
num={}
def BFS(mk,q):
    dx=[1,-1,0,0]
    dy=[0,0,1,-1]
    num[mk]=0
    while q:
        a,b=q.popleft()
        board[a][b]=mk
        num[mk]+=1
        for i in range(4):
            nx=a+dx[i]
            ny=b+dy[i]
            if 0<=nx<n and 0<=ny<m:
                if check[nx][ny]==0 and board[nx][ny]==0:
                    check[nx][ny]=1
                    q.append([nx,ny])

    

    
for x in range(n):
    tmp=list(input())
    t=[]
    for y in range(m):
        t.append(int(tmp[y]))
    board.append(t)

cnt=2
for x in range(n):
    for y in range(m):
        if board[x][y]==0:
            q=deque()
            q.append([x,y])
            BFS(cnt,q)
            cnt+=1


for x in range(n):
    for y in range(m):
        if board[x][y]==1:
            tmp=set()
            ans=1
            if x+1<n and board[x+1][y]!=1:
                if board[x+1][y] not in tmp:
                    ans+=num[board[x+1][y]]
                    tmp.add( board[x+1][y] )
            if x-1>=0 and board[x-1][y]!=1:
                if board[x-1][y] not in tmp:
                    ans+=num[board[x-1][y]]
                    tmp.add(board[x-1][y])
            if y+1<m and board[x][y+1]!=1:
                if board[x][y+1] not in tmp:
                    ans+=num[board[x][y+1]]
                    tmp.add(board[x][y+1])
            if y-1>=0 and board[x][y-1]!=1:
                if board[x][y-1] not in tmp:
                    ans+=num[board[x][y-1]]
                    tmp.add(board[x][y-1])
            print(ans%10,end="")
        else:
            print(0,end="")
    print()
            
            
