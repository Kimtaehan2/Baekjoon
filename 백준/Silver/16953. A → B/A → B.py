import sys
from collections import deque
input=sys.stdin.readline

x,target=map(int,input().split())
que=deque([[x,0]])

while 1:
    q=deque.popleft(que)
    if q[0]==target:
        print(q[1]+1)
        break

    if q[0]*2<=target:
        que.append([q[0]*2,q[1]+1])
    if (q[0]*10+1)<=target:
        que.append([(q[0]*10+1),q[1]+1])
    
    if len(que)==0:
        print(-1)
        break