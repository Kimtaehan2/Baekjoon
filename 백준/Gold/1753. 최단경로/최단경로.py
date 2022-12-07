import sys
import heapq
input = sys.stdin.readline

V,E = map(int,input().split())

INF = 1e9
start = int(input())-1

# 인접 행렬을 이용하여 메모리 초과 발생 -> 인접 리스트로 변경
graph = [[] for i in range(V)]

for i in range(E):
    node = list(map(int,input().split()))
    graph[node[0]-1].append([node[1]-1,node[2]])

def dijkstra(start):
    distance = [INF]*V
    distance[start] = 0
    heap = [[0,start]] # 힙의 초기값을 0,0 으로 잡아서 틀림
    while heap:
        new = heapq.heappop(heap)
        for d in graph[new[1]]: # d[0] : 인덱스, d[1] : 값
            if d[1] + new[0] < distance[d[0]]:
                distance[d[0]] = d[1] + new[0]
                # 바뀐 것만 힙에 넣어 준다 
                # distance를 이용하여 값을 넣어줘서 처음 말고 graph[start]를 다시 활용하지 않음
                heapq.heappush(heap,[distance[d[0]],d[0]])
    return distance


for i in dijkstra(start):
    if i == INF: print('INF')
    else: print(i)