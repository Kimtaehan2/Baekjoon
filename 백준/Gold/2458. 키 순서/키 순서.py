import sys
input = sys.stdin.readline

N,M =map(int,input().split())

INF : float = 1e9
graph : list[list[int]] = [[0 for _ in range(N)] for i in range(N)]

for i in range(M):
    A,B = map(int,input().split())
    graph[A-1][B-1]=1
    graph[B-1][A-1]=-1

for i in range(N):
    for j in range(N):
        if i == j: graph[i][j]=1

def FW():
    for C in range(N):
        for A in range(N):
            if A==C: continue
            for B in range(N):
                if A==B or C==B: continue
                if graph[A][C]+graph[C][B]==2:
                    graph[A][B]=1
                if graph[A][C]+graph[C][B]==-2:
                    graph[A][B]=-1
                

count : list[int] = [0]*N
FW()
for i in range(N):
    for j in range(N):
        if graph[i][j]==0:
            count[i]=1

print(N-sum(count))
