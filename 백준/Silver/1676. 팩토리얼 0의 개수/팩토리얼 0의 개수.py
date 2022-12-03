import sys
input=sys.stdin.readline

def fac(n):
  if n==0: return 0
  if n==1: return 1
  return fac(n-1)*n
n=int(input())
num=fac(n)
count=0
if num==0: count=0
else:
  while num%10==0:
    count+=1
    num//=10

print(count)