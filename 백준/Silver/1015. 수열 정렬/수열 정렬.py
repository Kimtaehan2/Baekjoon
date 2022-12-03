import sys
input=sys.stdin.readline

n=int(input())
arr2=list(map(int,input().split()))
arr1=sorted(arr2)

for i in range(n):
    arr2[i]=arr1.index(arr2[i])
    arr1[arr2[i]]=-1

print(*arr2)