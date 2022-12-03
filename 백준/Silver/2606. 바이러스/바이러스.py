import sys
input=sys.stdin.readline
C=int(input())
N=int(input())

#해시 셋과 다이렉트 그래프 초기화
hashset=set()
graph=[[] for i in range(C)]
#각 컴퓨터를 그래프의 인덱스로 생각하고 인덱스에 각 컴퓨터와 연결된 컴퓨터의 번호를 저장함
for i in range(N):
    num=list(map(int,input().split()))
    graph[num[0]-1].append(num[1])
    graph[num[1]-1].append(num[0])

#첫번째 컴퓨터의 노드가 모두 없어질 때까지 노드를 팝 해주면서 중복을 제거해주는 해시 셋에 저장하고
#그 노드와 연결된 노드를 팝 해주며 다시 0번째 인덱스로 가져와줌
while graph[0]:
    q=graph[0].pop()
    if q==1: pass
    else: 
        hashset.add(q)
        while graph[q-1]:
            graph[0].append(graph[q-1].pop())
#결과는 해시 셋에 저장됨
print(len(hashset))