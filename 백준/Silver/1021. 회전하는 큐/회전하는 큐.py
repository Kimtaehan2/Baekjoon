import sys
from collections import deque

N,M=map(int,sys.stdin.readline().split())

que=deque([i for i in range(1,N+1)])

arr=list(map(int,sys.stdin.readline().split()))

count2=0
count3=0

for i in range(M):
    id=que.index(arr[i])+1
    if id<=len(que)//2+1:
        anwser=deque.popleft(que)
        while anwser!=arr[i]:
            deque.append(que,anwser)
            count2+=1
            anwser=deque.popleft(que)

    else:
        anwser=deque.pop(que)
        while anwser!=arr[i]:
            deque.appendleft(que,anwser)
            count3+=1
            anwser=deque.pop(que)
        count3+=1
print(count3+count2)