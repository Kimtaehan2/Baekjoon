import sys
input=sys.stdin.readline

n,k = map(int,input().split())
graph = [[0 for i in range(n)]for i in range(n)]

for i in range(k):
    node = list(map(int,input().split()))
    graph[node[0]-1][node[1]-1] = -1
    graph[node[1]-1][node[0]-1] = 1

def FW():
    for C in range(n):
        for A in range(n):
            if A==C: continue
            for B in range(n):
                if B==C or B==A: continue
                if graph[A][C] + graph[C][B]==-2:
                    graph[A][B]=-1
                    graph[B][A]=1
                elif graph[A][C] + graph[C][B]==2:
                    graph[A][B]=1
                    graph[B][A]=-1

FW()
s = int(input())
for i in range(s):
    ac = list(map(int,input().split()))
    print(graph[ac[0]-1][ac[1]-1])