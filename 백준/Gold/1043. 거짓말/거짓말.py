import sys
from collections import deque
input=sys.stdin.readline
n,m=map(int,input().split())
True_man_list=list(map(int,input().split()))
True_man_list.pop(0)

party=[list(map(int,(input().split())))for i in range(m)]
graph1=[[0]*(m+1) for i in range(n+1)]
graph2=[[0]*(n+1) for i in range(m+1)]

# 방문 체크는 파티에 관해서만 하였음
visited=[0]*(m+1)

# 각 번호의 인원이 참석해 있는 파티를  사람 기준 그래프와 파티 기준 그래프로 나타냄
for i in range(len(party)):
    party[i].pop(0)
    for j in party[i]:
        graph1[j][i+1]=1
        graph2[i+1][j]=1

def bfs(x):
    que=deque([x])
    count=0
    while que:
        q=deque.popleft(que)
        # q번의 사람이 방문한 파티의 인덱스 = i
        for i in range(1,m+1):
            if graph1[q][i]==1:
                # 파티가 이미 방문한 파티일 때
                if visited[i]==1: pass
                # 파티가 방문하지 않은 파티 일 때
                else:
                    # 그 파티에 간 구성원을 탐색
                    for j in range(1,n+1):
                        if graph2[i][j]==1:
                            que.append(j)
                    visited[i]=1
        
for i in True_man_list:
    bfs(i)

print(m-sum(visited))