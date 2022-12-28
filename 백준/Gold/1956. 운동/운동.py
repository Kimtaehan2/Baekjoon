import sys
input = sys.stdin.readline

v,e = map(int,input().split())

INF = 1e9

graph = [[INF]*v for _ in range(v)]

for _ in range(e):
    a,b,c = map(int,input().split())
    graph[a-1][b-1] = c

def FW():
    for C in range(v):
        for A in range(v):
            for B in range(v):
                if graph[A][B] > graph[A][C] + graph[C][B]:
                    graph[A][B] = graph[A][C] + graph[C][B]

FW()
result = []
for i in range(v):
    result.append(graph[i][i])

anwser = min(result)
if anwser == INF:
    print(-1)
else: print(anwser)