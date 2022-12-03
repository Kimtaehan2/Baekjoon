import sys
input=sys.stdin.readline

N=int(input())
M=int(input())

INF = 1e9
node = [list(map(int,input().split()))for i in range(M)]
# 자신과의 비교 결과를 알수 없으면 INF
# 자신보다 더 작다면 1 크다면 2
graph=[([INF]*N) for i in range(N)]

for i in node:
  graph[i[0]-1][i[1]-1]=1
  graph[i[1]-1][i[0]-1]=2

for X in range(N):
  for A in range(N):
    for B in range(N):
      if B==A: pass
      for C in range(N):
        if B==C: pass
        else: 
          if graph[A][C]+graph[C][B]==2: graph[A][B]=1
          if graph[A][C]+graph[C][B]==4: graph[A][B]=2
            

for i in graph:
  count=-1
  for j in i:
    if j==INF:
      count+=1
  print(count)