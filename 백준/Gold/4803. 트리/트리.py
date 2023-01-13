import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

# 유니온 파인드
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

casecnt = 1

while 1:
    n,m = map(int,input().split())
    cycleset = set()
    result_cycleset = set()
    hashset = set()
    
    if n == 0 and m == 0: break
    
    disjoint_set = [i for i in range(n)]

    for _ in range(m):
        a,b = map(int,input().split())
        if find(a-1) == find(b-1):
            # 만약 사이클이 형성되었다면 cycleset에 저장한다
            cycleset.add(find(a-1))
        else:
            union(a-1,b-1)
    
    # 각 분리집합의 대표 값을 해시 셋에 저장하여 해시 셋의 크기를 이용해 분리집합의 개수를 구한다
    for x in disjoint_set:
        hashset.add(find(x))
    # cycleset에서의 각 대표값을 뽑아 result_cycleset에 저장한다
    for x in cycleset:
        result_cycleset.add(find(x))

    treecnt = len(hashset) - len(result_cycleset)
    
    if treecnt <= 0:
        print("Case %d: No trees." %casecnt)
    elif treecnt == 1:
        print("Case %d: There is one tree." %casecnt)
    else:
        print("Case %d: A forest of %d trees." %(casecnt,treecnt))
    casecnt += 1
