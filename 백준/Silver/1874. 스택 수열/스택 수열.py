import sys

#n 입력
n=int(sys.stdin.readline())

result=[]
stack=[]

#스택넘버
stacknum=0

for i in range(n):
    #m 입력
    m=(int(sys.stdin.readline()))

    #스택에 m이 없을 경우, 
    while m>stacknum:
        #스택오류
        if stacknum>n: 
            result.clear()
            result.append("NO")
            break
        stacknum+=1
        stack.append(stacknum)
        result.append('+')
    
#스택에 m이 있을 경우

    #스택 오류
    if stack[-1]!=m:
        result.clear()
        result.append("NO")
        break
    stack.pop()
    result.append('-')

print('\n'.join(result))