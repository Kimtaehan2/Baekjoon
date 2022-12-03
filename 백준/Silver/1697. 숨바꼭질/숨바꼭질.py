import sys
from collections import deque

N,K=map(int,input().split())

visited=[0]*1000000

def bfs(N,K):
    que=deque([[N,0]])
    while que:
        q=deque.popleft(que)
        if visited[q[0]]==1: pass
        else:
            visited[q[0]]=1
            if q[0]==K:
                return q[1]
            if q[0]+1<=100000:
                que.append([q[0]+1,q[1]+1])
            if q[0]-1>=0:
                que.append([q[0]-1,q[1]+1])
            if N<K and q[0]*2<200000:
                que.append([q[0]*2,q[1]+1])

print(bfs(N,K))