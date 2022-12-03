import sys
from collections import deque
input=sys.stdin.readline

n : int =int(input())
m : int =int(input())

# 무한
INF : int =1e9

# 플로이드 위셜 알고리즘을 위한 간선 리스트 입력받기
node : list =[list(map(int,input().split())) for i in range(m)]

# 인덱스[0] : 도시 번호 / 인덱스[1] : 이동하려는 도시 번호 / 값 : 각 도시로 가는 비용 / 각 도시에 연결된 경로가 없다면 INF
graph : list =[ [INF]*(n+1) for i in range(n+1)] 

# 노드를 이용하여 그래프 초기화를 해준다
for i in node:
    graph[i[0]][i[1]]=min(i[2],graph[i[0]][i[1]])

# 먼저 그래프를 돌면서 시작 도시와 도착 도시가 같다면, 즉 graph[x][x] 라면 0으로 초기화 해준다
for i in range(1,n+1):
    for j in range(1,n+1):
        if i==j: graph[i][j]=0

# 플루이드 위셜 알고리즘 구현
def FW(n):
    for i in range(n):
        for A in range(1,n+1):
            for B in range(1,n+1):
                for C in range(1,n+1):
                    if A==B or B==C or A==C or A==C: pass
                    else: graph[A][B]=min(graph[A][B],graph[A][C]+graph[C][B])

FW(n)
for i in range(1,len(graph)):
    for j in range(len(graph[i])):
        if graph[i][j]>=1e9: graph[i][j]=0
    print(*graph[i][1:])