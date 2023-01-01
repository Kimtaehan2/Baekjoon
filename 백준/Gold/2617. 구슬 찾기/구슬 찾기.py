import sys
input = sys.stdin.readline

n,m = map(int,input().split())

INF = 1e9

graph = [[0]*n for _ in range(n)]

for _ in range(m):
    a,b = map(int,input().split())
    graph[a-1][b-1] = 1
    graph[b-1][a-1] = -1

def FW():
    for C in range(n):
        for A in range(n):
            if C == A: continue
            for B in range(n):
                if B == C or B == A: continue
                # A가 C보다 무겁고 C가 B보다 무거울 때
                if graph[A][C] == 1 and graph[C][B] == 1:
                    graph[A][B] = 1
                    graph[B][A] = -1
                # A가 C보다 가볍고 C가 B보다 가벼울 때
                if graph[A][C] == -1 and graph[C][B] == -1:
                    graph[A][B] = -1
                    graph[B][A] = 1

FW()
result = 0
for i in range(n):
    if graph[i].count(1) > n//2 or graph[i].count(-1) > n//2:
        result += 1
    
print(result)
