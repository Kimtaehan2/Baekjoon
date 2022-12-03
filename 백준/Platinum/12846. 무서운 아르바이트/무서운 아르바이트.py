import sys
input=sys.stdin.readline

N = int(input())

pay = list(map(int,input().split()))

stack = []
result = []

for i in range(N):
    while stack:
        if stack[-1][1]>pay[i]:
            P = stack.pop()
            result.append((i-P[0])*P[1])
        else: break
    if len(stack)==0: stack.append([0,pay[i],i])
    else: stack.append([stack[-1][2]+1,pay[i],i])

while stack:
    P = stack.pop()
    result.append((N-P[0])*P[1])

print(max(result))