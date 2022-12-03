n=int(input())

l=[-1 for i in range(n)]

def dp(n):

    if n==3: return 1
    elif n==5: return 1
    elif n<=5: return -1
    l[2]=1
    l[4]=1

    for i in range(5,n):
        if l[i-5]!=-1: l[i]=l[i-5]+1
        elif l[i-3]!=-1: l[i]=l[i-3]+1
        else: pass
    return l[-1]

print(dp(n))