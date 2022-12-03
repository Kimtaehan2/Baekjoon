import sys
#시간 초과가 발생하여 내장함수 이용
import collections
result=[]
n=int(sys.stdin.readline())
#리스트에 1부터 n까지 저장한다
que=collections.deque([i for i in range(1,n+1)])
#que의 크기가 1이 될때까지
while len(que)!=1:
    #제일 앞의 값을 pop
    result.append(collections.deque.popleft(que))
    #맨 앞의 값을 맨 뒤에 추가 해 준 뒤에 맨 앞의 값을 pop 해준다
    collections.deque.append(que,collections.deque.popleft(que))

print(*(result+list(que)))