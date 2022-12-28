import sys
input = sys.stdin.readline

n,m = map(int,input().split())

arr = list(map(int,input().split()))
result = [0]
stack = []
visited = [0]*n
def back_tracking(depth):
    if depth == 3:
        if sum(stack) <= m and result[-1] < sum(stack):
           result.append(sum(stack)) 
        return
    
    for i in range(n):
        if visited[i] == 0:
            visited[i] = 1
            stack.append(arr[i])
            back_tracking(depth+1)
            stack.pop()
            visited[i] = 0

back_tracking(0)

print(result[-1])