import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)
class Node:
    def __init__(self,value):
        self.value = value
        self.left = None
        self.right = None

def push(leaf,start):
    root = start
    while 1:
        if leaf.value < root.value:
            if root.left == None:
                root.left = leaf
                return
            else:
                root = root.left
        else:
            if root.right == None:
                root.right = leaf
                return
            else:
                root = root.right

def postorder(root,parant,d):
    if root.left != None:
        postorder(root.left,root,0)
    if root.right != None:
        postorder(root.right,root,1)
    if root.left == None and root.right == None:
        if d == 0:
            parant.left = None
        else:
            parant.right = None
        print(root.value)


root = 0

while 1:
    try:
        if root == 0:
            root = Node(int(input()))
        else:
            push(Node(int(input())),root)
    except:
        break

postorder(root,root,0)
