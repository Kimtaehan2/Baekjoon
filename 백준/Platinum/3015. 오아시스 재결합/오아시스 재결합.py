import sys
input = sys.stdin.readline

n : int = int(input())

arr : list[int] = [int(input()) for i in range(n)]

stack : list[int] = []
count : list[int] = [[0,0] for i in range(n)]

l = 0
for i in range(n):
    while stack:
        if arr[stack[-1]]<arr[i]:
            stack.pop()
            count[i][0]+=1
            l = len(stack)
        elif arr[stack[-1]]>arr[i]:
            count[i][1]+=1
            l = len(stack)
            break
        else:
            count[i][1] += count[stack[-1]][1]+1
            break
    stack.append(i)

result = 0
for i in count:
    result += sum(i)
print(result)