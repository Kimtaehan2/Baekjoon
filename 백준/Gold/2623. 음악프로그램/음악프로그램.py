import sys
from collections import deque
input = sys.stdin.readline

N,M = map(int,input().split())

indegree = [0]*N

graph = [[] for _ in range(N)]

for _ in range(M):
    order = list(map(int,input().split()))

    for i in range(2,len(order)):
        indegree[order[i]-1] += 1
        graph[order[i-1]-1].append(order[i]-1)


start = []
for i in range(N):
    if indegree[i] == 0:
        start.append(i)

result = []

def bfs():
    # que에는 인덱스를 저장
    que = deque(start)
    while que:
        # 진입차수가 0인 정점
        new = deque.popleft(que)
        for i in range(len(graph[new])):
            # 진입차수 감소
            indegree[graph[new][i]] -= 1
            # 진입차수가 0이 된 정점이 있다면 그 정점을 que에 append
            if indegree[graph[new][i]] == 0:
                que.append(graph[new][i])
        # 탐색이 끝난 정점은 result에 저장
        result.append(new+1)

bfs()

# result의 길이가 가수 수와 같다면 문제가 없으므로 result 출력
if len(result) == N:
    for x in result:
        print(x)
else:
    print(0)
