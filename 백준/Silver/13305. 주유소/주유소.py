import sys
input=sys.stdin.readline
n=int(input())
distance=list(map(int,input().split()))
price=list(map(int,input().split()))

for i in range(1,n-1):
    if price[i]>price[i-1]:
        price[i]=price[i-1]
result=0
for i in range(n-1):
    result+=price[i]*distance[i]

print(result)