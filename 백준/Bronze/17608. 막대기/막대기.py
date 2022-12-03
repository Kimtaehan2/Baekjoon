import sys

n=int(sys.stdin.readline())
stack=[]
result=[]
#막대기가 스택에 저장
for i in range(n):
    stick=int(sys.stdin.readline())
    stack.append(stick)
    
#맨 위의 스택으로 스틱 초기화
stick=stack.pop()
result.append(stick)
#스틱이 더 큰 값으로 옮겨 가며 결과에 저장
while len(stack)!=0:
    if stick<stack[-1]: 
        stick=stack.pop()
        result.append(stick)
    else: stack.pop()


print(len(result))