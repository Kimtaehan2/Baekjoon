import sys
input=sys.stdin.readline

n=int(input())
num=0
sum=0
count=0
while sum!=n:
  if sum+num+1>n:
    sum-=num
    num=n-sum
  else:
    num+=1
    count+=1
  sum+=num
print(count)