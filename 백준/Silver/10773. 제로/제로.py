import sys
k=int(sys.stdin.readline())

stack=[]

for i in range(k):
    order=int(sys.stdin.readline())
    if order==0:
        stack.pop()
    else: stack.append(order)

print(sum(stack))
