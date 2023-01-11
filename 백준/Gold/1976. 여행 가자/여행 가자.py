import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

n = int(input())
m = int(input())
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

for a in range(n):
    arr = list(map(int,input().split()))
    for b in range(len(arr)):
        if arr[b] == 1:
            union(a,b)

result = list(map(int,input().split()))

table = []
for i in range(len(result)):
    if len(table) == 0:
        table.append(find(result[i]-1))
    else:
        if table[-1] != find(result[i]-1):
            print("NO")
            table.clear()
            break
if len(table) != 0:
    print("YES")