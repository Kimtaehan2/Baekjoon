n=int(input())
m=int(input())
sum=0
for i in range(m):
    a,b=map(int,input().split())
    sum+=a*b
if sum==n: print('Yes')
else: print('No')