import sys
from collections import deque
def check():
  for j in range(H):
      for i in visited[j]:
          if 0 in i: return False
  return True

M,N,H=map(int,input().split())
graph=[[list(map(int,input().split())) for i in range(N)]for i in range(H)]
visited=[[[0 for i in range(M)]for i in range(N)]for i in range(H)]
for i in range(H):
  for j in range(N):
    visited[i][j]=graph[i][j]
result=[]
count=[]

def bfs(list):
    global count
    Quex=deque([])
    Quey=deque([])
    for i in list:
        visited[i[2]][i[0]][i[1]]=0
        Quex.append([i[1],0,i[2]])
        Quey.append([i[0],0,i[2]])
    
    while Quex or Quey:
        QX=deque.popleft(Quex)
        QY=deque.popleft(Quey)
        
        if visited[QX[2]][QY[0]][QX[0]]==1: pass
        else:
            count.append(QX[1])
            visited[QX[2]][QY[0]][QX[0]]=1
            if QX[0]-1>=0 and graph[QX[2]][QY[0]][QX[0]-1]==0 and visited[QX[2]][QY[0]][QX[0]-1]==0: 
                Quex.append([QX[0]-1,QX[1]+1,QX[2]])
                Quey.append([QY[0],QY[1]+1,QX[2]])
            if QX[0]+1<M and graph[QX[2]][QY[0]][QX[0]+1]==0 and visited[QX[2]][QY[0]][QX[0]+1]==0:
                Quex.append([QX[0]+1,QX[1]+1,QX[2]])
                Quey.append([QY[0],QY[1]+1,QX[2]])
            if QY[0]-1>=0 and graph[QX[2]][QY[0]-1][QX[0]]==0 and visited[QX[2]][QY[0]-1][QX[0]]==0:
                Quex.append([QX[0],QX[1]+1,QX[2]])
                Quey.append([QY[0]-1,QY[1]+1,QX[2]])
            if QY[0]+1<N and graph[QX[2]][QY[0]+1][QX[0]]==0 and visited[QX[2]][QY[0]+1][QX[0]]==0:
                Quex.append([QX[0],QX[1]+1,QX[2]])
                Quey.append([QY[0]+1,QY[1]+1,QX[2]])
            if QX[2]-1>=0 and visited[QX[2]-1][QY[0]][QX[0]]==0:
                Quex.append([QX[0],QX[1]+1,QX[2]-1])
                Quey.append([QY[0],QY[1]+1,QX[2]-1])
            if QX[2]+1<H and visited[QX[2]+1][QY[0]][QX[0]]==0:
                Quex.append([QX[0],QX[1]+1,QX[2]+1])
                Quey.append([QY[0],QY[1]+1,QX[2]+1])
        

for h in range(H):
  for i in range(N):
      for j in range(M):
          if graph[h][i][j]==1:
              result.append((i,j,h))
bfs(result)

if check():
    print(max(count))
else: print(-1)
