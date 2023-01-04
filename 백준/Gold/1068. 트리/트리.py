import sys
input = sys.stdin.readline

n = int(input())

rootleaf = 0

class Node:
    def __init__(self):
        self.parent = False
        self.value = True
        self.leaf = []

# 리스트로 트리의 잎 정보를 저장
tree = [0]*n
for i in range(n):
    tree[i] = Node()

# 부모 노드 입력
arr = list(map(int,input().split()))

# 노드에 따라 트리 정보 저장
for i in range(n):
    p = arr[i]
    if p != -1:
        tree[p].leaf.append(tree[i])
    else:
        tree[i].parent = True

# 루트 노드 찾기
for i in range(n):
    if tree[i].parent and len(tree[i].leaf) != 0:
        rootleaf = i

remove_leaf = int(input())

tree[remove_leaf].value = False
cnt = 0

def leaf_cnt(root):
    global cnt
    if not root.value:
        return
    
    for l in root.leaf:
        if l.value:
            leaf_cnt(l)

    if len(root.leaf) == 0 or (len(root.leaf) == 1 and not root.leaf[0].value):
        cnt += 1
        
leaf_cnt(tree[rootleaf])
print(cnt)
