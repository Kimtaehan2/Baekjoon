import sys

n,k=map(int,input().split())
greedy=[]
for i in range(n):
    greedy.append(int(sys.stdin.readline()))
count=0
while k!=0:
    price=greedy.pop()
    while k>=price:
        count+=k//price
        k=k%price
print(count)