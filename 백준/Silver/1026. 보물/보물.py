import sys

n=int(sys.stdin.readline())

A=list(map(int,sys.stdin.readline().split()))
B=list(map(int,sys.stdin.readline().split()))

A.sort()
B.sort()
sum=0
for i in range(n):
  sum+=A[i]*B[n-i-1]

print(sum)