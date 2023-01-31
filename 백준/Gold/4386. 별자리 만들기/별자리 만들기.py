import sys
import heapq
input = sys.stdin.readline

N = int(input())

heap = []

parents = [i for i in range(N)]

def find(x):
    if x == parents[x]:
        return x
    
    parents[x] = find(parents[x])
    return parents[x]

def union(a,b):
    a = find(a)
    b = find(b)
    if a > b:
        parents[a] = b
    else:
        parents[b] = a

def get_distance(ax,ay,bx,by):
    d = (ax-bx)**2 + (ay-by)**2
    return pow(d,0.5)

coordinates = []

for _ in range(N):
    x,y = map(float,input().split())
    coordinates.append([x,y])

for i in range(N-1):
    ax,ay = coordinates[i][0],coordinates[i][1]
    for j in range(i+1,N):
        bx,by = coordinates[j][0],coordinates[j][1]
        heapq.heappush(heap,[get_distance(ax,ay,bx,by),i,j])

result = 0

while heap:
    distance,a,b = heapq.heappop(heap)

    if find(a) != find(b):
        union(a,b)
        result += distance

print(result)