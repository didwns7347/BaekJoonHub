import sys
sys.setrecursionlimit(100000)
ans = ""
def solution(n, m, x, y, r, c, k):
    answer = "imposible"
    check = [[[-1 for _ in range(m+1)] for _ in range(n+1) ] for _ in range(k+1)]
    dx = [1,0,0,-1]
    dy = [0,-1,1,0]
    ways = ["d","l","r","u"]
    def BF(nowx,nowy,way):
        # print(way)
        global ans
        if ans != "":
            return
        if len(way) == k:
            if nowx==r and nowy==c:
                print(ans)
                ans = way
            return
        if check[len(way)][nowx][nowy] != -1:
            return
        check[len(way)][nowx][nowy] = 1

        for i in range(4):
            nx = nowx+dx[i]
            ny = nowy+dy[i]
            if 0<nx<=n and 0<ny<=m:
                BF(nx,ny,way+ways[i])
    BF(x,y,"")
    if ans == "":
        return "impossible"
    return ans