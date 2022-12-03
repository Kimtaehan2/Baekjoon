import sys
from collections import deque
input=sys.stdin.readline
T=int(input())

for i in range(T):
  order=list(input().strip())
  n=int(input())
  arr=input()
  arr=arr.replace('[','')
  arr=arr.replace(']','').rstrip()
  arr=arr.split(',')

  l=deque([i for i in range(0,n)])
  check=1
  for i in order:
    if i=='R':
      check*=-1
    else: 
      if len(l)==0: check=0
      elif check==1: deque.popleft(l)
      else: 
        deque.pop(l)
  
  result=[]
  if check==-1:
    for i in range(len(l)):
      result.append(arr[l[(len(l)-1-i)]])
    print('['+(','.join(result))+']',sep='')
  elif check==1:
    for i in l:
      result.append(arr[i])
    print('['+(','.join(result))+']',sep='')
  else: print('error')
  