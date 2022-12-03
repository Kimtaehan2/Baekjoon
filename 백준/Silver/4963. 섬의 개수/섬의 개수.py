import sys
input=sys.stdin.readline
sys.setrecursionlimit(10**6)
l=[(0,1),(0,-1),(1,1),(1,0),(1,-1),(-1,1),(-1,0),(-1,-1)]


def dfs(y,x):
    global h
    global w
    if world[y][x]==0: return
    world[y][x]=0
    for i in l:
        if y+i[0]<0 or y+i[0]>h-1 or x+i[1]<0 or x+i[1]>w-1: pass
        else:   
            if world[y+i[0]][x+i[1]]==1:
                dfs(y+i[0],x+i[1])

while 1:
    w,h=map(int,input().split())
    if w==0 and h==0: break
    world=[list(map(int,input().split())) for i in range(h)]
    count=0
    for i in range(h):
        for j in range(w):
            if world[i][j]==1: count+=1
            dfs(i,j)
    print(count)
