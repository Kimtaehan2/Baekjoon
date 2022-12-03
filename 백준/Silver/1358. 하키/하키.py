import sys
input=sys.stdin.readline

W,H,X,Y,P=map(int,input().split())
cx1=X
cx2=X+W
cy1,cy2=Y+H//2,Y+H//2
r1,r2=H//2,H//2
count=0
for i in range(P):
    x,y=map(int,input().split())
    if x>=X and x<=X+W and y>=Y and y<=Y+H:
        count+=1
    elif (cx1-x)**2+(cy1-y)**2<=r1**2 or (cx2-x)**2+(cy2-y)**2<=r2**2:
        count+=1
print(count)