import sys
input=sys.stdin.readline

n=int(input())
arr=list(map(int,input().split()))
result=[-1 for i in range(n)]
stack=[]

count=[0 for i in range(max(arr))]
for i in range(n):
  count[arr[i]-1]+=1

for i in range(n):
  while stack:
    if count[arr[i]-1]<=count[arr[stack[-1]]-1]:
      break
    result[stack.pop()]=arr[i]
  stack.append(i)
print(*result)