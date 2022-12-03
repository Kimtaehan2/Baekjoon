import sys
input=sys.stdin.readline

n,m=map(int,input().split())

l={}
for i in range(1,n+1):
  keys=input().strip()
  l[keys]=str(i)
  l[str(i)]=keys


for i in range(m):
  order=input().strip()
  print(l[order])