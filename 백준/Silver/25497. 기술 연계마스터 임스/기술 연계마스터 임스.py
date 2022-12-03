import sys

#1~9 연계 x 기술
#L R의 사전 기술
#S K의 사전 기술

cast_S=0
cast_L=0
count=0

n=int(input())
stack=sys.stdin.readline().strip()
for i in range(n):
    cmd=stack[i]
    if cmd=='L':
        cast_L+=1
    elif cmd=='R': 
        cast_L-=1
        if cast_L>=0:count+=1 
        else: 
            print(count)
            break
    elif cmd=='S':
        cast_S+=1
        ast_L=0
    elif cmd=='K':
        cast_S-=1
        if cast_S>=0:count+=1 
        else: 
            print(count)
            break
    elif cmd=='1'or cmd=='2'or cmd=='3'or cmd=='4'or cmd=='5'or cmd=='6'or cmd=='7'or cmd=='8'or cmd=='9': count+=1
    if i==n-1:print(count)
