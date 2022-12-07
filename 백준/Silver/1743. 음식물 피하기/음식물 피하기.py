import sys
from collections import deque
input=sys.stdin.readline

n,m,k = map(int,input().split())
graph = [[0 for i in range(m)] for i in range(n)]
for i in range(k):
    food = list(map(int,input().split()))
    graph[food[0]-1][food[1]-1] = 1

l = [(0,1),(0,-1),(1,0),(-1,0)]
result = []

def bfs(x,y):
    que = deque([[x,y]])
    cnt = 0
    while que:
        new = deque.popleft(que)
        if graph[new[1]][new[0]] == 1:
            graph[new[1]][new[0]] = 0
            cnt += 1
            for i in l:
                if new[0]+i[0]<0 or new[0]+i[0]>=m:
                    continue
                if new[1]+i[1]<0 or new[1]+i[1]>=n:
                    continue
                que.append([new[0]+i[0],new[1]+i[1]])
    result.append(cnt)

for i in range(n):
    for j in range(m):
        bfs(j,i)

print(max(result))