import math
from collections import deque
def solution(board):
    answer = -1
    dx = [1,0,-1,0]
    dy = [0,1,0,-1]
    sx = 0
    sy = 0
    tx,ty = 0,0
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j]=='G':
                tx = i
                ty = j
            if board[i][j]=="R":
                sx = i
                sy = j
    
    visited = [[math.inf for _ in range(len(board[0]))] for _ in range(len(board))]
    visited[sx][sy] = 0
    q = deque([[sx,sy]])
    def moveUp(x,y):
        if board[x][y]=="D" and x>=0 :
            return (x+1,y)
        if x == 0:
            return (x,y)
      
        return moveUp(x-1,y)
    
    def moveDown(x,y):
        if board[x][y]=="D" and x<len(board):
            return (x-1,y)
        if  x == len(board)-1:
            return (x,y)
        return moveDown(x+1,y)
    
    def moveRight(x,y):
        if board[x][y]=="D" and y<len(board[0]):
            return (x,y-1)
        if y == len(board[0])-1:
            return (x,y)
        return moveRight(x,y+1)

    def moveLeft(x,y):
        if board[x][y]=="D" and y>=0:
            return (x,y+1)
        if y == 0:
            return (x,y)
        return moveLeft(x,y-1)
        

    while q:
        info = q.popleft()
        nx,ny = info[0],info[1]
        ncost = visited[nx][ny]
        if nx == tx and ny ==ty:
            answer = visited[nx][ny]
            break
        nextx,nexty = moveLeft(nx,ny)
        if visited[nextx][nexty] > ncost + 1:
            q.append([nextx,nexty])
            visited[nextx][nexty]=ncost+1
        
        nextx,nexty = moveRight(nx,ny)
        if visited[nextx][nexty] > ncost + 1:
            q.append([nextx,nexty])
            visited[nextx][nexty]=ncost+1

        nextx,nexty = moveUp(nx,ny)
        if visited[nextx][nexty] > ncost + 1:
            q.append([nextx,nexty])
            visited[nextx][nexty]=ncost+1

        nextx,nexty = moveDown(nx,ny)
        if visited[nextx][nexty] > ncost + 1:
            q.append([nextx,nexty])
            visited[nextx][nexty]=ncost+1


    
    return answer