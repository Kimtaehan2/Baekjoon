import sys
import heapq
input=sys.stdin.readline

N : int = int(input())

cards : list[int] = [int(input()) for i in range(N)]

heapq.heapify(cards)

# 제일 작은 카드 묶음 2개 합치기
# 합친 카드를 힙에 넣음
# 반복
count : int = 0

while len(cards)>1:
    card1 : int = heapq.heappop(cards)
    card2 : int = heapq.heappop(cards)

    heapq.heappush(cards,card1+card2)
    count+=card1+card2

print(count)