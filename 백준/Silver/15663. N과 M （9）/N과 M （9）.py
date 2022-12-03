import sys
import itertools
input=sys.stdin.readline

n,m=map(int,input().split())
arr=list(map(int,input().split()))
per=list(itertools.permutations(arr,m))

per=list(set(per))
per.sort()
for i in per:
    print(*i)