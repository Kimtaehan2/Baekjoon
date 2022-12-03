import sys
input=sys.stdin.readline

n,m=map(int,input().split())
hashset=set()
graph=[[] for i in range(n)]
for i in range(m):
    node=list(map(int,input().split()))
    graph[node[0]-1].append(node[1])
    graph[node[1]-1].append(node[0])
# count 초기화
count=0
#모든 그래프를 돌면서 정점으로 노드를 모으는 것과 동시에 노드를 해시 셋에 저장
for i in range(n):
    #실행 전 해시 셋의 길이를 저장해 놓고 전과 달라졌다면 연결요소의 개수+1
    lastlen=len(hashset)
    while graph[i]:
        q=graph[i].pop()
        hashset.add(q)
        if q-1==i: 
            hashset.add(q)
        else:
            while graph[q-1]:
                p=graph[q-1].pop()
                graph[i].append(p)
                hashset.add(p)
    if len(hashset)!=lastlen: count+=1
# 간선 정보가 주어지지 않은 정점도 연결 요소로 취급함
count+=n-len(hashset)

print(count)