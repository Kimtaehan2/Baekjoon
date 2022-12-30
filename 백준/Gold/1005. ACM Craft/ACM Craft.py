import sys
from collections import deque
input = sys.stdin.readline

def bfs(l,win_building,temp):
    que = deque(l)
    while que:
        new = deque.popleft(que)
        # 찾고자 하는 정점에 도달했다면 리턴하여 함수를 종료
        if new == win_building:
            return dp_table[new]

        for i in graph[new]:
            # 현재 정점과 연결된 정점의 간선 제거
            in_degree[i] -= 1
            # 이전 순서의 정점 중 가장 시간이 많이 걸리는 건물 시간을 더해줘야 하기에 
            # dp를 이용해 전까지의 가장 긴 건설 시간을 dp_table 에 저장해 줌
            dp_table[i] = max(dp_table[i],dp_table[new]+build_time[i-1])
            # 진입 차수가 0인 정점은 방문처리 후 큐에 넣어줌
            if in_degree[i] == 0 and visited[i] == 0:
                visited[i] = 1
                que.append(i)
    
# 테스트 케이스 수
t = int(input())

for _ in range(t):
    # 건물의 개수 n, 건설순서 규칙의 총 개수 k
    n,k = map(int,input().split())
    # 각 건물의 건설 시간 (건물 번호 : 인덱스 + 1)
    build_time = list(map(int,input().split()))
    # 각 정점의 진입 차수
    in_degree = [0]*(n+1)
    # 간선 리스트
    graph = [[] for _ in range(n+1)]
    # 방문 체크 리스트
    visited = [0]*(n+1)
    for _ in range(k):
        x,y = map(int,input().split())
        graph[x].append(y)
        in_degree[y] += 1
    # 승리하기 위해 건설해야 할 건물의 번호 
    win_building = int(input())
    # dp_table
    dp_table = [0]*(n+1)
    # 진입 차수가 0인 정점 리스트
    start_in_degree = []
    for i in range(1,n+1):
        if in_degree[i] == 0:
            dp_table[i] = build_time[i-1]
            start_in_degree.append(i)

    print(bfs(start_in_degree,win_building,len(start_in_degree)))