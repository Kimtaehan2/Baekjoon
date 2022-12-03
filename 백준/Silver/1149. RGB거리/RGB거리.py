import sys
input=sys.stdin.readline

n=int(input())
price=[]
for i in range(n):
    price.append(list(map(int,input().split())))

def dp(n):
    if n==1: return min(price[0])
    sol1=[price[0][0]]
    sol2=[price[0][1]]
    sol3=[price[0][2]]
    for i in range(1,n):
        sol1.append(min(sol2[i-1],sol3[i-1])+price[i][0])
        sol2.append(min(sol1[i-1],sol3[i-1])+price[i][1])
        sol3.append(min(sol1[i-1],sol2[i-1])+price[i][2])
    return min(sol1[-1],sol2[-1],sol3[-1])

print(dp(n))
