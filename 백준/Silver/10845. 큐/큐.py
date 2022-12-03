import sys

n=int(sys.stdin.readline())
#큐를 리스트로 생성
Que=[]
#출력을 위한 result 생성
result=[]

for i in range(n):
    #입력을 띄어쓰기 기준으로 받는다
    order=sys.stdin.readline().split()
    #result에 문자열으로 추가하는 이유: join을 사용하기 위해서
    if order[0]=='push':
        Que.append(order[1])
    if order[0]=='pop':
        if len(Que)==0: result.append('-1')
        else: result.append(str(Que.pop(0)))
    if order[0]=='size':
        result.append(str(len(Que)))
    if order[0]=='empty':
        if len(Que)==0: result.append('1')
        else: result.append('0')
    if order[0]=='front':
        if len(Que)==0: result.append('-1')
        else: result.append(str(Que[0]))

    if order[0]=='back':
        if len(Que)==0: result.append('-1')
        else: result.append(str(Que[-1]))

print('\n'.join(result))