import sys
result=[]
n,m=map(int,input().split())
arr=list(map(int,sys.stdin.readline().split()))
sum=[0]
def dp(n):
    if n==1: sum.append(arr[0])
    else:
        sum.append(arr[0])
        for i in range(1,n):
            sum.append(sum[i]+arr[i])
dp(n)
for x in range(m):
    i,j=map(int,sys.stdin.readline().split())
    result.append(sum[j]-sum[i-1])

print(*result,sep='\n')