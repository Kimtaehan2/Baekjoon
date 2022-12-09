import sys
import heapq
input = sys.stdin.readline
INF = 1e9

N = int(input()) # 도시의 개수
M = int(input()) # 버스의 개수

graph = [[] for i in range(N)]

for i in range(M):
    node = list(map(int,input().split()))
    graph[node[0]-1].append((node[2],node[1]-1))

start, arrival = map(int,input().split())

new_list = [INF]*N
new_list[start-1] = 0
que = []
heapq.heappush(que,(0,start-1))
while que:
    new = heapq.heappop(que)
    graph[new[1]].sort()
    for distance,idx in graph[new[1]]:
        if new[0] + distance < new_list[idx]:
            new_list[idx] = new[0] + distance
            heapq.heappush(que,(new_list[idx],idx))
print(new_list[arrival-1])
