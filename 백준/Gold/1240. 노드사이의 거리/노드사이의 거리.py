import sys
sys.setrecursionlimit(10*6)
input = sys.stdin.readline

N,M = map(int,input().split())

distance = [[0]*N for _ in range(N)]
graph = [[] for _ in range(N)]



for _ in range(N-1):
    a,b,c = map(int,input().split())
    graph[a-1].append(b-1)
    graph[b-1].append(a-1)
    distance[a-1][b-1] = c
    distance[b-1][a-1] = c

def dfs(x,target,d):
    if x == target:
        print(d)
        return
    visited[x] = 1
    
    for a in graph[x]:
        if visited[a] == 0:
            dfs(a,target,d+distance[x][a])

for _ in range(M):
    a,b = map(int,input().split())
    visited = [0]*N
    dfs(a-1,b-1,0)