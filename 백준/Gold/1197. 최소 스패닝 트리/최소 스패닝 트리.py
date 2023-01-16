import sys
import heapq
input = sys.stdin.readline

sys.setrecursionlimit(10*6)

v,e = map(int,input().split())

# 유니온 파인드
def find(x):
    if disjointed_set[x] == x:
        return x
    disjointed_set[x] = find(disjointed_set[x])
    return disjointed_set[x]

def union(a,b):
    pa = find(a)
    pb = find(b)
    if pa > pb:
        disjointed_set[pa] = pb
    else:
        disjointed_set[pb] = pa

disjointed_set = [i for i in range(v+1)]

# 힙을 사용하여 가중치가 가장 작은 간선부터 연결한다
heap = []

for i in range(e):
    a,b,c = map(int,input().split())
    heapq.heappush(heap,[c,a,b])

result = 0

while heap:
    c,a,b = heapq.heappop(heap)
    # 유니온 파인드로 사이클이 형성되지 않을 때를 찾고
    if find(a) != find(b):
        # union 하고 가중치를 result 에 더한다
        union(a,b)
        result += c

print(result)