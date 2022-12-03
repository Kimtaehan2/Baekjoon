import sys
import copy
from collections import deque
input = sys.stdin.readline

N,M =map(int,input().split())

graph = [list(map(int,input().split())) for i in range(N)]

# 백트래킹으로 모든 경우의 수를 탐색하여 안전 영역의 넓이를 count에 저장 후 가장 큰 값을 도출

l = [(0,1),(0,-1),(1,0),(-1,0)]

check = [([False]*M)for i in range(N)]

count = []

# 백트래킹
def Back_tracking(depth,MAP):
    if depth == 3:
        copy_MAP = copy.deepcopy(MAP)
        visited : list = [([False]*M)for i in range(N)]
        for i in range(N):
            for j in range(M):
                if MAP[i][j]==2:
                    bfs(j,i,visited,copy_MAP)
        count.append(counting_safe_area(copy_MAP))
        return 
    
    for i in range(N):
        for j in range(M):
            if not check[i][j] and MAP[i][j]==0:
                check[i][j] = True
                MAP[i][j] = 1
                Back_tracking(depth+1,MAP)
                MAP[i][j] = 0
                check[i][j] = False

#BFS
def bfs(x : int, y : int, visited : list, graph : list):
    que = deque([[x,y]])
    while que:
        P = deque.popleft(que)
        if visited[P[1]][P[0]]: pass
        else:
            visited[P[1]][P[0]] = True
            graph[P[1]][P[0]] = 2
            for X in l:
                if P[0]+X[0]<0 or P[0]+X[0]>=M: continue
                elif P[1]+X[1]<0 or P[1]+X[1]>=N: continue
                else:
                    if graph[P[1]+X[1]][P[0]+X[0]]==0:
                        que.append([P[0]+X[0],P[1]+X[1]])
    return

# 안전 구역을 세 주는 함수
def counting_safe_area(MAP : list) -> int:
    cnt = 0
    for i in MAP:
        cnt += i.count(0)
    return cnt
    
Back_tracking(0,graph)
print(max(count))