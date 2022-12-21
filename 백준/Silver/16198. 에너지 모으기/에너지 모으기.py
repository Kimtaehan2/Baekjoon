import sys
input = sys.stdin.readline

n = int(input())
energe = list(map(int,input().split()))
visited = [0]*n
result = []
stack = []
def get_energe1(i):
    for j in range(i):
        if visited[i-j-1] == 0:
            return energe[i-j-1]

def get_energe2(i):
    for j in range(i+1,n):
        if visited[j] == 0:
            return energe[j]

def back_tracking(depth):
    if depth == n-2:
        result.append(sum(stack))
        return 

    for i in range(1,n-1):
        if visited[i] == 0:
            visited[i] = 1
            stack.append(get_energe1(i)*get_energe2(i))
            back_tracking(depth+1)
            stack.pop()
            visited[i] = 0

back_tracking(0)        
print(max(result))