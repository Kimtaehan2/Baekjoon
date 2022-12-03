import sys
input=sys.stdin.readline

n,m,r =map(int,input().split())

# 아이템 개수 입력
items : list =list(map(int,input().split()))

# 무한
INF : int =1e9

# 길 양 끝에 존재하는 지역의 번호 a, b, 그리고 길의 길이 l (1 ≤ l ≤ 15)가 주어진다
node : list =[list(map(int,input().split())) for i in range(r)]

graph : list =[ [INF]*n for i in range(n)]

# 노드를 이용하여 그래프 초기화를 해준다
for i in node:
    l=i[2]
    graph[i[0]-1][i[1]-1]=l
    graph[i[1]-1][i[0]-1]=l

for i in range(n):
    for j in range(n):
        if i==j: graph[i][j]=0

# 플루이드 위셜 알고리즘 구현
def FW(n):
    for i in range(n):
        for A in range(n):
            for B in range(n):
                if A==B: pass
                for C in range(n):
                    if B==C or A==C: pass
                    else: graph[A][B]=min(graph[A][B],graph[A][C]+graph[C][B])

FW(n)

# 최대 아이템 개수를 구하기 위해 count 리스트 만들기
count=[0 for i in range(n)]
# 그래프를 돌면서 1~n 번에 착륙했을 경우에 얻을 수 있는 아이템의 개수를 count에 저장
for i in range(len(graph)):
    cnt=0
    for j in range(len(graph[i])):
        if graph[i][j] <= m:
            cnt+=items[j]
    count[i]=cnt
print(max(count))