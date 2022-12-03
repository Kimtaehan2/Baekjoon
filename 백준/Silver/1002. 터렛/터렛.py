import sys
def T(x1,y1,r1,x2,y2,r2):
    # 두 점 사이의 거리 = r1+r2 or abs(r1-r2)
    d=(x1-x2)**2+(y1-y2)**2

    #두 점의 위치가 같을 때
    if x1==x2 and y1==y2:
        #원이 겹칠 때
        if r1==r2: return -1
        #원이 겹치지 않을 때
        else: return 0
    #두 점의 위치가 다를 때
    else:
        # 1점에서 만날 때
        if d==(abs(r1)+abs(r2))**2 or d==(r1-r2)**2:
            return 1
        # 만나지 않을 때
        elif d>(r1+r2)**2 or d<(r1-r2)**2:
            return 0
        # 2점에서 만날 때
        else: return 2

n=int(sys.stdin.readline())

result=[]
for i in range(n):
    x1,y1,r1,x2,y2,r2=map(int,sys.stdin.readline().split())
    result.append(str(T(x1,y1,r1,x2,y2,r2)))

print('\n'.join(result))