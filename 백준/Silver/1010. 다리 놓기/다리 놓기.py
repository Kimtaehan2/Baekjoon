import sys
input=sys.stdin.readline
T=int(input())

def fac(n):
    if n==1: return 1
    return fac(n-1)*n

for i in range(T):
    n,m=map(int,input().split())
    if n==m: print(1)
    else: print(fac(m)//(fac(m-n)*fac(n)))
