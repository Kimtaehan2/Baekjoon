import sys
input=sys.stdin.readline
n=int(input())

top=list(map(int,input().split()))
# result 초기화
result=[0]*n
#스택에 인덱스 저장
stack=[0]

for i in range(1,n):
    while stack:
        #현재 탑보다 왼쪽의 있는 탑을 가장 가까운 것부터 탐색
        #만약 현재의 탑보다 작다면 스택에서 팝
        if top[stack[-1]]<top[i]:
            stack.pop()
        #크다면 현재의 탑보다 큰 탑의 인덱스를 result에 저장 후 반복문을 종료
        else: 
            result[i]=stack[-1]+1
            break
    #현재 탑의 바로 전의 탑이 더 크다면 바로 전의 탑의 인덱스+1을 result에 저장
    if top[i-1]>=top[i]: result[i]=i
    #현재 탑의 인덱스를 스택에 푸쉬
    stack.append(i)

print(*result)