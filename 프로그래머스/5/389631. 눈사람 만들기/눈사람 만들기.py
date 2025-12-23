import sys
sys.setrecursionlimit(10**9)
def solution(grid):
    N=len(grid)
    M=len(grid[0])
    v=[[0 for _ in range(M)] for _ in range(N)]
    f=1
    ct=[0,1,1,0]
    def getN(x,y):
        if x:
            yield x-1,y
        if y:
            yield x,y-1
        if x<N-1:
            yield x+1,y
        if y<M-1:
            yield x,y+1

    def search(x,y,flag):
        for nx,ny in getN(x,y):
            if grid[nx][ny]=="." and ((v[nx][ny]&flag)==0):
                v[nx][ny]+=flag
                ct[v[nx][ny]]+=1
                search(nx,ny,flag)
    starto = []
    for i,row in enumerate(grid):
        for j,val in enumerate(row):
            if val=="o":
                v[i][j]=f
                search(i,j,f)
                starto.append((i,j))
                f+=1
    ct[1]-=ct[3]
    def checkmiddle():
        sx,sy = starto[0]
        ex,ey = starto[1]
        v[ex][ey]=3
        step = -1
        q=[(sx,sy)]
        while q:
            nq=[]
            for x,y in q:
                if (x,y)==(ex,ey):
                    v[ex][ey]=2
                    return step
                for nx,ny in getN(x,y):
                    if v[nx][ny]==3:
                        v[nx][ny]=4
                        nq.append((nx,ny))
            step+=1
            q=nq
    mid = checkmiddle()
    upperbound = sum(ct)
    def f(n):
        return (n//2)*((n+1)//2)

    if mid<ct[3]:
        return f(upperbound)-f(mid+1)

    def search_intersection(sx, sy):
        q=[(sx,sy)]
        flag = v[sx][sy]
        v[sx][sy]+=7
        step = 0
        while q:
            nq = []
            step+=1
            for x,y in q:
                for nx,ny in getN(x,y):
                    if v[nx][ny]==flag:
                        v[nx][ny]+=7
                        nq.append((nx,ny))
            if len(nq)>=2:
                return step
            q=nq
        return 2600000
    l=[]
    for i,(x,y) in enumerate(starto,1):
        l.append((search_intersection(x,y),ct[i]))
    l.sort()
    if l[1][0]<2600000:
        return f(upperbound) - f(mid+1)

    ans = 0
    if l[0][0]==2600000:
        for up in range((ct[3]+3)//2, ct[3]+l[1][1]+1):
            ans += len(range(max(1, ct[3]+2-up), min(up+1, ct[3]+l[0][1]+1, upperbound+1 - up)))
        return ans
    if l[0][0]<=l[1][1]+ct[3]:
        return f(upperbound) - f(mid+1)
    for up in range((ct[3]+3)//2, upperbound+1):
        if up<=l[0][0]:
            ans += len(range(max(1, ct[3]+2-up), min(up+1, ct[3]+l[1][1]+1, upperbound+1-up)))
        else:
            ans += len(range(max(1,ct[3]+2-up), min(up+1, upperbound+1-up)))
    return ans