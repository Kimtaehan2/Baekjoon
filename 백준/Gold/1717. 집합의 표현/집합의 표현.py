import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

n,m = map(int,input().split())

disjoint_set = [i for i in range(n+1)]

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

for i in range(m):
    order,a,b = map(int,input().split())

    if order == 0:
        union(a,b)
    else:
        if find(a) == find(b):
            print("YES")
        else:
            print("NO")
