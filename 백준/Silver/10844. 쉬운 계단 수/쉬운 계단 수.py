import sys
input=sys.stdin.readline
n=int(input())
def dp(n):
    if n==1: return 9
    arr1=[0,1,1,1,1,1,1,1,1,1]
    arr2=[0,0,0,0,0,0,0,0,0,0]
    for i in range(1,n):
        for j in range(10):
            if j==0:
                arr2[j]=arr1[j+1]
            elif j==9:
                arr2[j]=arr1[j-1]
            else:
                arr2[j]=arr1[j+1]+arr1[j-1]
        for x in range(10):
            arr1[x]=arr2[x]
    return sum(arr2)

print(dp(n)%1000000000)