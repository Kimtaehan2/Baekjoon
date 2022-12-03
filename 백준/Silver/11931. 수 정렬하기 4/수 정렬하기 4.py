import heapq
import sys
input=sys.stdin.readline

n=int(input())

heap=[]
for i in range(n):
    heapq.heappush(heap,-(int(input())))

for i in range(n):
    print(-(heapq.heappop(heap)))