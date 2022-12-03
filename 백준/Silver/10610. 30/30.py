import sys
input=sys.stdin.readline
num=list(map(int,input().strip()))

if sum(num)%3==0:
    num=sorted(num,reverse=True)
    if num[-1]!=0: print(-1)
    else: print(*num,sep='')

else: print(-1)