import sys
from collections import deque
input=sys.stdin.readline
n : int = int(input())

# 방향은 R RD D
graph : list = [list(map(int,input().split())) for i in range(n)]
count : int = 0

# dfs
def dfs(x,y,D):
    global count
    if x==n-1 and y==n-1:
        count+=1
        return
    # 대각선
    if y+1<n and x+1<n and (graph[y][x+1]!=1 and graph[y+1][x+1]!=1 and graph[y+1][x]!=1):
        dfs(x+1,y+1,'RD')
    # 아래
    if D!='R':
        if y+1<n and (graph[y+1][x]!=1):
            dfs(x,y+1,'D')
    # 오른쪽
    if D!='D':
        if x+1<n and (graph[y][x+1]!=1):
            dfs(x+1,y,'R')
    return

# bfs
def bfs(n):
    if n==1: return 1
    que=deque([[0,1,'R']])
    count : int = 0
    while que:
        p=deque.popleft(que)
        if p[0]==n-1 and p[1]==n-1:
            count+=1
        # 대각선
        if p[0]+1<n and p[1]+1<n and (graph[p[0]][p[1]+1]!=1 and graph[p[0]+1][p[1]+1]!=1 and graph[p[0]+1][p[1]]!=1):
            que.append([p[0]+1,p[1]+1,'RD'])
        # 아래
        if p[0]+1<n and (graph[p[0]+1][p[1]]!=1):
            if p[2]=='R': pass
            else: que.append([p[0]+1,p[1],'D'])
        # 오른쪽
        if p[1]+1<n and (graph[p[0]][p[1]+1]!=1):
            if p[2]=='D': pass
            else: que.append([p[0],p[1]+1,'R'])
    return count

dfs(1,0,'R')
print(count)