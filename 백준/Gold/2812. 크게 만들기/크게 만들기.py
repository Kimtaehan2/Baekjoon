import sys
input=sys.stdin.readline

N,K = map(int,input().split())

NUM : list[int] = list(map(int,input().strip()))

stack : list[int] = [] 
result : list[int] = [i for i in range(N)]

count : int = 0
for i in range(N):
    while stack:
        if count==K: break
        if NUM[stack[-1]]<NUM[i]:
            result[stack.pop()]=-1
            count+=1
            if count==K: break
        else: break
    stack.append(i)

while count!=K and len(stack)>1:
    p=stack.pop()
    if NUM[stack[-1]]>=NUM[p]:
        result[p]=-1
        count+=1

for i in result:
    if i == -1: pass
    else: print(NUM[i],end='')