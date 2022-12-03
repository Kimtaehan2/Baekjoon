import sys

n=int(input())

arr=list(map(int,input().split()))
result=[-1 for i in range(n)]
temp=[]

for i in range(n-1):
  if arr[i]<arr[i+1]:
    result[i]=arr[i+1]
    while temp:
      if arr[temp[-1]]<arr[i+1]:
        result[temp.pop()]=arr[i+1]
      else: break
    
  else: temp.append(i)

print(*result)