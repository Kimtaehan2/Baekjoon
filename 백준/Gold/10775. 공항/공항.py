import sys
sys.setrecursionlimit(10*6)
input = sys.stdin.readline

G = int(input())
P = int(input())

gates = [i for i in range(G+1)]

# union find
def find(x):
    if x == gates[x]:
        return x
    
    gates[x] = find(gates[x])
    return gates[x]

def union(a,b):
    pa = find(a)
    pb = find(b)

    if pa > pb:
        gates[pa] = pb
    else:
        gates[pb] = pa

result = -1

# 유니온 파인드를 이용하여 
# 입력되는 게이트 번호의 부모를 find하여 부모를 찾은 후 
# 노드의 부모 번호 - 1 과 입력된 게이트 번호의 노드를 union 해준다

for i in range(P):
    g = int(input())

    # 만약 찾은 부모가 0이라면 더 이상 게이트에 들어갈 자리가 없다는것을 의미하므로 union 하지 않는다
    if find(g) > 0:
        union(g,find(g)-1)
    else:
        if result == -1:
            result = i
        else:
            pass

if result == -1:
    result = P

print(result)