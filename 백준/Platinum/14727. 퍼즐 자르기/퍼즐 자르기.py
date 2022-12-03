import sys
input=sys.stdin.readline

N = int(input())

high = list(int(input()) for i in range(N))

stack = []
result = []

for i in range(N):
    while stack:
        if stack[-1][1]>high[i]:
            P = stack.pop()
            result.append((i-P[0])*P[1])
        else: break
    if len(stack)==0: stack.append([0,high[i],i])
    else: stack.append([stack[-1][2]+1,high[i],i])

while stack:
    P = stack.pop()
    result.append((N-P[0])*P[1])

print(max(result))