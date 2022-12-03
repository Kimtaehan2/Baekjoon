import itertools
n,m=map(int,input().split())
arr=list(map(int,input().split()))

per=list(itertools.permutations(arr,m))
per.sort()
for i in per:
    print(*i)
