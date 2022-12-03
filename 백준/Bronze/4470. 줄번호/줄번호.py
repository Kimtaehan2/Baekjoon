import sys
input=sys.stdin.readline
n=int(input())
arr=[[i,'. ',input().rstrip()]for i in range(1,n+1)]

for i in arr:
  print(*i,sep='')