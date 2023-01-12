import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

n,m = map(int,input().split())
disjoint_set = [i for i in range(n)]

def find(x):
    if x == disjoint_set[x]:
        return x
    disjoint_set[x] = find(disjoint_set[x])
    return disjoint_set[x]

def union(a,b):
    a = find(a)
    b = find(b)
    if a > b:
        disjoint_set[a] = b
    else:
        disjoint_set[b] = a

cont = 0

for i in range(1,m+1):
    a,b = map(int,input().split())
    if cont == 0:
        if find(a) == find(b):
            cont = i
        else:
            union(a,b)

print(cont)