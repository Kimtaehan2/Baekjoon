import sys
input=sys.stdin.readline

T=int(input())

for i in range(T):
    x1,y1,x2,y2=map(int,input().split())
    
    n=int(input())
    count=0
    for i in range(n):
        #행성 반지름
        cx,cy,r=map(int,input().split())
        #구해야 할 것 
        #출발점과 행성 중심과의 거리
        d1=(x1-cx)**2+(y1-cy)**2
        #도착점과 행성 중심과의 거리
        d2=(x2-cx)**2+(y2-cy)**2
        if d1<r**2 and d2>r**2: count+=1
        elif d2<r**2 and d1>r**2: count+=1
    print(count)