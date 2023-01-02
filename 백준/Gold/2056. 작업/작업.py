import sys
from collections import deque
input = sys.stdin.readline

n = int(input())

graph = [[] for _ in range(n)]
work_time = [0]*n
in_degree = [0]*n
visited = [0]*n
time = [0]*n
maxtime = [0]*n

start_indegree = []

for i in range(n):
    cmd = list(map(int,input().split()))
    work_time[i] = cmd[0]
    if cmd[1] > 0:
        for x in cmd[2:]:
            graph[x-1].append(i)
            in_degree[i] += 1
    else:
        time[i] = cmd[0]
        maxtime[i] = cmd[0]
        start_indegree.append(i)

for i in start_indegree:
    visited[i] = 1

def bfs():
    que = deque(start_indegree)
    while que:
        new = deque.popleft(que)
        for x in graph[new]:
            in_degree[x] -= 1
            if maxtime[x] < time[new]:
                maxtime[x] = time[new]
            
            if in_degree[x] == 0:
                time[x] += (maxtime[x]+work_time[x])
                que.append(x)
      

bfs()
print(max(time))