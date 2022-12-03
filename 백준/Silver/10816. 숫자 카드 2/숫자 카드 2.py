import sys
input=sys.stdin.readline
n=int(input())
cards=list(map(int,input().split()))
m=int(input())
select_cards=list(map(int,input().split()))


count={}
for i in range(n):
    count[cards[i]]=0
for i in range(m):
    count[select_cards[i]]=0

for i in range(n):
    count[cards[i]]+=1

for i in range(m):
    print(count[select_cards[i]],end=' ')