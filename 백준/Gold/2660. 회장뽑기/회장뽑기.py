import sys
input=sys.stdin.readline

n : int =int(input())
m : int =0
node : list =[]

# 플로이드 위셜 알고리즘을 위한 간선 리스트 입력받기
while 1:
    V=list(map(int,input().split()))
    if V==[-1,-1]: break
    node.append(V)

# 무한
INF : int =1e9

# 인덱스[0] : 회장 후보 번호 / 인덱스[1] : 친구인 회장 후보 번호 / 값 : 점수 / 친구가 아니라면 INF
graph : list =[ [INF]*(n+1) for i in range(n+1)] 

# 노드를 이용하여 그래프 초기화를 해준다
for i in node:
    graph[i[0]][i[1]]=1
    graph[i[1]][i[0]]=1

# 먼저 그래프를 돌면서 자기 자신이라면, 즉 graph[x][x] 라면 0으로 초기화 해준다
for i in range(1,n+1):
    for j in range(1,n+1):
        if i==j: graph[i][j]=0

# 플루이드 위셜 알고리즘 구현
def FW(n):
    for i in range(n):
        for A in range(1,n+1):
            for B in range(1,n+1):
                for C in range(1,n+1):
                    if A==B or B==C or A==C or A==C: pass
                    else: graph[A][B]=min(graph[A][B],graph[A][C]+graph[C][B])

FW(n)
result : list = []

# 그래프를 돌면서 가장 높은 점수를 result에 추가해 준다
for i in range(1,len(graph)):
    result.append([max(graph[i][1:]),i])

# 회장 후보 점수
KING : int = min(result)[0]
# 회장 후보 리스트
KING_list : list = []
# 회장 후보 수
count : int = 0
for i in result:
    if i[0]==KING:
        count+=1
        KING_list.append(i[1])
KING_list.sort()
print(KING,count)
print(*KING_list)