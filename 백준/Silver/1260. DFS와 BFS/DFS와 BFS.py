import sys
from collections import deque
input=sys.stdin.readline
sys.setrecursionlimit(10**6)

N,M,V=map(int,input().split())

#간선 초기화
visit=[[0 for i in range(N+1)]for i in range(N+1)]
check=[0]*(N+1)

#출력을 저장하는 리스트
dfs_result=[V]
bfs_result=[]


#간선 입력
for i in range(M):
  o=list(map(int,input().split()))
  visit[o[0]][o[1]]=1
  visit[o[1]][o[0]]=1

#dfs
def dfs(v):
  check[v]=1
  for i in range(N+1):
    if visit[v][i]==1 and check[i]==0:
      dfs_result.append(i)
      dfs(i)

#bfs
def bfs(v):
  que=deque([v])
  while que:
    q=deque.popleft(que)
    bfs_result.append(q)
    for i in range(N+1):
      if visit[q][i]==1 and check[i]==0:
        check[i]=1
        que.append(i)

dfs(V)
print(*dfs_result)


check=[0]*(N+1)
check[V]=1
bfs(V)
print(*bfs_result)