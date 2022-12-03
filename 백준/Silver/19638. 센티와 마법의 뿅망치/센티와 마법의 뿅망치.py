import sys
import heapq
N,H,T=map(int,input().split())

maxheap=[]
def hpush(n):
    heapq.heappush(maxheap,-n)

#망치 구현
def hammer():
    n=heapq.heappop(maxheap)
    #일단 가장 큰 거인의 키를 팝 한것을 n에 저장 후
    #n이 1이라면 그대로 1을 다시 푸쉬 
    if int(n)==-1:
        heapq.heappush(maxheap,-1)
    #아니라면 정수로 n/2 저장
    else: heapq.heappush(maxheap,int(n/2))

#힙에 거인의 키를 힙 푸쉬
for i in range(N):
    hpush(int(sys.stdin.readline()))

#망치를 쓰기도 전에 가장 큰 거인의 키가 센티보다 작으면 0번을 출력 (예외처리)
if -maxheap[0]<H:
    print('YES')
    print(0)

else:
    #아니라면 망치를 사용하고 횟수를 count에 저장
    for i in range(T):
        hammer()
        count=i
        if -maxheap[0]<H: break

    #가장 큰 거인의 키가 센티보다 작을때
    if -maxheap[0]<H:
        print('YES')
        print(count+1)
    #아닐때
    else: 
        print('NO')
        print(int(-maxheap[0]))
