
from collections import deque

INF = 1e6
n,m = map(int,input().split())

dire = [(1,0),(-1,0),(0,1),(0,-1)]

graph = [list(map(int,input().strip())) for _ in range(n)]
visited = [[INF for _ in range(m)] for _ in range(n)]
visited_break = [[INF for _ in range(m)] for _ in range(n)]

def bfs():
    que = deque([[0,0,1,0]])
    
    while que:
        x,y,movecnt,breakcnt = deque.popleft(que)
        if y == n-1 and x == m-1:
            return

        for d in dire:
            if x+d[0] < 0 or x+d[0] > m-1:
                continue
            if y+d[1] < 0 or y+d[1] > n-1:
                continue

            # 앞이 벽일 때
            if graph[y+d[1]][x+d[0]] == 1 and breakcnt == 0:
                if visited_break[y+d[1]][x+d[0]] > movecnt:
                    visited_break[y+d[1]][x+d[0]] = movecnt
                    que.append([x+d[0],y+d[1],movecnt+1,1])

            # 앞이 벽이 아닐 때
            elif graph[y+d[1]][x+d[0]] == 0:
                if breakcnt == 0:
                    if visited[y+d[1]][x+d[0]] > movecnt:
                        visited[y+d[1]][x+d[0]] = movecnt
                        que.append([x+d[0],y+d[1],movecnt+1,breakcnt])
                else:
                    if visited_break[y+d[1]][x+d[0]] > movecnt:
                        if visited[y+d[1]][x+d[0]] != movecnt:
                            visited_break[y+d[1]][x+d[0]] = movecnt
                            que.append([x+d[0],y+d[1],movecnt+1,breakcnt])


bfs()
if visited[n-1][m-1] == INF and visited_break[n-1][m-1] == INF:
    if n==1 and m==1:
        print(1)
    else:
        print(-1)
else:
    print(min(visited[n-1][m-1]+1,visited_break[n-1][m-1]+1))
