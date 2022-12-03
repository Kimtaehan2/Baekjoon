import sys
from collections import deque
input=sys.stdin.readline
n,m=map(int,input().split())
que=deque([[0,0]])
def bfs(y,x):
  while que:
    q=deque.popleft(que)
    if check[q[0]][q[1]]==1: pass
    else: 
      check[q[0]][q[1]]=1
      if q[0]>0 and graph[q[0]-1][q[1]]==1:
        que.append([q[0]-1,q[1]])
        count[q[0]-1][q[1]].append(min(count[q[0]][q[1]])+1)
      if q[1]>0 and graph[q[0]][q[1]-1]==1:
        que.append([q[0],q[1]-1])
        count[q[0]][q[1]-1].append(min(count[q[0]][q[1]])+1)
      if q[0]<n-1 and graph[q[0]+1][q[1]]==1:
        que.append([q[0]+1,q[1]])
        count[q[0]+1][q[1]].append(min(count[q[0]][q[1]])+1)
      if q[1]<m-1 and graph[q[0]][q[1]+1]==1:
        que.append([q[0],q[1]+1])
        count[q[0]][q[1]+1].append(min(count[q[0]][q[1]])+1)
      

graph=[list(map(int,input().strip())) for i in range(n)]
check=[[0 for i in range(m)] for i in range(n)]
count=[[[] for i in range(m)] for i in range(n)]
count[0][0].append(1)

bfs(0,0)
print(min(count[n-1][m-1]))