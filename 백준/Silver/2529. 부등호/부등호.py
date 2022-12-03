import sys
input = sys.stdin.readline

K = int(input())

sign_list = list(input().split())
check = [0]*10
result = []
stack = []
def back_tracking(root,head,depth):
    if depth == K:
        result.append(''.join([str(root)]+stack))
        return

    for i in range(10):
        if sign_list[depth]=='<':
            if head<i and check[i]==0:
                check[i]=1
                stack.append(str(i))
                back_tracking(root,i,depth+1)
                stack.pop()
                check[i]=0

        elif sign_list[depth]=='>':
            if head>i and check[i]==0:
                check[i]=1
                stack.append(str(i))
                back_tracking(root,i,depth+1)
                stack.pop()
                check[i]=0



for i in range(10):
    stack.clear()
    check[i]=1
    back_tracking(i,i,0)
    check[i]=0

result.sort()
print(result[-1],result[0],sep='\n')