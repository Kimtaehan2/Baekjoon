import sys
input=sys.stdin.readline

d=[]
n=int(input())
for i in range(n):
  age,name=map(str,input().split())
  age=int(age)
  d.append((age,i,name))

d.sort()
for i in d:
  print(i[0],i[2])