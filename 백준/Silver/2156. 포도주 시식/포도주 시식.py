import sys

n=int(input())
arr=[int(input()) for i in range(n)]

def dp(n):
  if n==1: return arr[0]
  elif n==2: return arr[0]+arr[1]
  elif n==3: return max(arr[0]+arr[2],arr[1]+arr[2],arr[0]+arr[1])

  SUM=[arr[0],arr[0]+arr[1],max(arr[0]+arr[2],arr[1]+arr[2]),max(arr[0]+arr[1]+arr[3],arr[0]+arr[2]+arr[3])]
  for i in range(4,n):
    SUM.append(max(SUM[i-2]+arr[i],SUM[i-3]+arr[i-1]+arr[i],SUM[i-4]+arr[i-1]+arr[i]))
  return max(SUM)

print(dp(n))