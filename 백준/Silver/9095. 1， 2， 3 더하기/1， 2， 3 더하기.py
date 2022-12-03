import sys

result=[]

T=int(input())

def dp(n):
    if n==1: return 1
    elif n==2: return 2
    elif n==3: return 4

    l=[1,2,4]

    for i in range(3,n):
        l.append(l[i-3]+l[i-2]+l[i-1])
    return l[-1]


for i in range(T):
    n=int(sys.stdin.readline())
    result.append(str(dp(n)))

print('\n'.join(result))