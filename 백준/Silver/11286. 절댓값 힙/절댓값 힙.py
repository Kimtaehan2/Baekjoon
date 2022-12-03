import sys
import heapq
result=[]
T=int(sys.stdin.readline())
hp=[]
def heap(n):
    
    if n==0 and len(hp)==0: result.append('0')
    elif n==0: result.append(str(heapq.heappop(hp)[1]))
    else:
        heapq.heappush(hp,(abs(n),n))
for i in range(T):
    n=int(sys.stdin.readline())
    heap(n)
print('\n'.join(result))