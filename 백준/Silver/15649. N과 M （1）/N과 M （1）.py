import sys
import itertools
input=sys.stdin.readline
N,M=map(int,input().split())

linerlist=[i for i in range(1,N+1)]

result=itertools.permutations(linerlist,M)

for i in result:
  print(*i)