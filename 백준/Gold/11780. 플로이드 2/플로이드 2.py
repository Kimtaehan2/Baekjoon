import sys
input=sys.stdin.readline

n : int =int(input())
m : int =int(input())

# 무한
INF : int = 99999999999

# 플로이드 위셜 알고리즘을 위한 간선 리스트 입력받기
node : list =[list(map(int,input().split())) for i in range(m)]

# 인덱스[0] : 도시 번호 / 인덱스[1] : 이동하려는 도시 번호 / 값 : 각 도시로 가는 비용 / 각 도시에 연결된 경로가 없다면 INF
# 인덱스[2][1] : 거쳐가는 도시 + 도착 도시 번호
graph : list =[ [[INF,[i]] for i in range(n+1)] for i in range(n+1)]

# 노드를 이용하여 그래프 초기화를 해준다
for i in node:
    if graph[i[0]][i[1]][0]>i[2]: graph[i[0]][i[1]][0] = i[2]

# 먼저 그래프를 돌면서 시작 도시와 도착 도시가 같다면, 즉 graph[x][x] 라면 [0,각 도시 번호]으로 초기화 해준다
for i in range(1,n+1):
    for j in range(1,n+1):
        if i==j: graph[i][j]=[0,[i]]

# 플루이드 위셜 알고리즘 구현
def FW(n):
        for C in range(1,n+1):
            for A in range(1,n+1):
                if C==A: continue
                for B in range(1,n+1):
                    if A==B or B==C: continue
                    MIN = min(graph[A][B][0],graph[A][C][0]+graph[C][B][0])
                    if graph[A][B][0]==graph[A][C][0]+graph[C][B][0]:
                        continue
                    elif MIN==graph[A][C][0]+graph[C][B][0]:
                        graph[A][B]=[MIN,(graph[A][C][1]+graph[C][B][1])]

FW(n)
for i in graph[1:]:
    for j in range(1,len(i)):
        if j==len(i)-1:
            if i[j][0]==INF:
               print(0,end='\n')
            else: print(i[j][0],end='\n')
        else:
            if i[j][0]==INF:
                print(0,end=' ')
            else: print(i[j][0],end=' ')

result = [[[j+1] for i in range(n)] for j in range(n)]

for i in range(1,len(graph)):
    for j in range(1,len(graph)):
        result[i-1][j-1]+=graph[i][j][1]
for i in range(len(result)):
    for j in range(len(result[i])):
        if i==j or graph[i+1][j+1][0]==INF: print(0)
        else: print(len(result[i][j]),*result[i][j])