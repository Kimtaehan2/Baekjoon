import sys
from collections import deque

T=int(sys.stdin.readline())

for i in range(T):
    N,id=map(int,sys.stdin.readline().split())
    V=deque(list(map(int,sys.stdin.readline().split())))
    count=1
    while V[0]!=max(V) or id!=0:
        if V[0]!=max(V):
            if id==0:
                id=len(V)-1
                deque.append(V,deque.popleft(V))
            else:
                id-=1
                deque.append(V,deque.popleft(V))
        else:
            if id==0:
                break
            else:
                count+=1
                id-=1
                deque.popleft(V)
    print(count)