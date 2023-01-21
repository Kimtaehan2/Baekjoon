import sys
from collections import deque
input = sys.stdin.readline

N,M = map(int,input().split())

indegree = [0]*N
graph = [[] for _ in range(N)]


for _ in range(M):
    a,b = map(int,input().split())
    indegree[b-1] += 1
    graph[a-1].append(b-1)

start = []
for i in range(N):
    if indegree[i] == 0:
        start.append(i)
    
def bfs(start):
    que = deque(start)
    while que:
        new = deque.popleft(que)
        for x in graph[new]:
            indegree[x] -= 1
            if indegree[x] == 0:
                que.append(x)
        print(new+1,end=' ')

bfs(start)