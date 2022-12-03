import sys
from collections import deque
def check():
    for i in visited:
        if 0 in i: return False
    return True

M,N=map(int,input().split())
graph=[list(map(int,input().split())) for i in range(N)]
visited=[[0 for i in range(M)]for i in range(N)]
for i in range(len(graph)):
    visited[i]=graph[i]
result=[]
count=[]
def bfs(list):
    global count
    Quex=deque([])
    Quey=deque([])
    for i in list:
        visited[i[0]][i[1]]=0
        Quex.append([i[1],0])
        Quey.append([i[0],0])
    
    while Quex or Quey:
        QX=deque.popleft(Quex)
        QY=deque.popleft(Quey)

        if visited[QY[0]][QX[0]]==1: pass
        else:
            count.append(QX[1])
            visited[QY[0]][QX[0]]=1
            if QX[0]-1>=0 and graph[QY[0]][QX[0]-1]==0 and visited[QY[0]][QX[0]-1]==0: 
                Quex.append([QX[0]-1,QX[1]+1])
                Quey.append([QY[0],QY[1]+1])
            if QX[0]+1<M and graph[QY[0]][QX[0]+1]==0 and visited[QY[0]][QX[0]+1]==0:
                Quex.append([QX[0]+1,QX[1]+1])
                Quey.append([QY[0],QY[1]+1])
            if QY[0]-1>=0 and graph[QY[0]-1][QX[0]]==0 and visited[QY[0]-1][QX[0]]==0:
                Quex.append([QX[0],QX[1]+1])
                Quey.append([QY[0]-1,QY[1]+1])
            if QY[0]+1<N and graph[QY[0]+1][QX[0]]==0 and visited[QY[0]+1][QX[0]]==0:
                Quex.append([QX[0],QX[1]+1])
                Quey.append([QY[0]+1,QY[1]+1])
        
            
for i in range(N):
    for j in range(M):
        if graph[i][j]==1:
            result.append((i,j))
bfs(result)

if check():
    print(max(count))
else: print(-1)