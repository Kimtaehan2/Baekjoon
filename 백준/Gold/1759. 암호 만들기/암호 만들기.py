import sys
import heapq
input = sys.stdin.readline

L,C = map(int,input().split())

alpha = list(input().split())

result = []
stack = []
visited = [0]*C
def back_tracking(depth,cnt1,cnt2):
    if depth == L:
        if cnt1>=1 and cnt2>=2:
            result.append(''.join(stack))
        return
    for i in range(C):
        if visited[i] == 0 and (len(stack)==0 or stack[-1]<alpha[i]):
            visited[i] = 1
            stack.append(alpha[i])
            if alpha[i] in ['a','e','i','o','u']:
                back_tracking(depth+1,cnt1+1,cnt2)
            else:
                back_tracking(depth+1,cnt1,cnt2+1)
            stack.pop()
            visited[i] = 0

back_tracking(0,0,0)
result.sort()
print(*result,sep='\n')