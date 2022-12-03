N=int(input())
num=list(map(int,input().split()))

def f(num):
    if num==1:
        return 0
    for j in range(2,num+1):
        if j==num:
            return 1
        if num%j==0:
            return 0
        
sum=0
for i in range(N):
    sum+=f(num[i])
print(sum)