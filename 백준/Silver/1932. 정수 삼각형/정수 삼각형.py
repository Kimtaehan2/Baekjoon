import sys
input=sys.stdin.readline

n=int(input())
tree=[list(map(int,input().split())) for i in range(n)]

def dp(n):
    if n==1: return tree[0][0]
    S=[[tree[0][0]]]
    for i in range(1,n):
        sol=[0]*(i+1)
        for j in range(len(S[i-1])):
            if S[i-1][j]+tree[i][j]>=sol[j]:
                sol[j]=S[i-1][j]+tree[i][j]
            if S[i-1][j]+tree[i][j+1]>=sol[j+1]:
                sol[j+1]=S[i-1][j]+tree[i][j+1]
        S.append(sol)
    return max(S[-1])

print(dp(n))