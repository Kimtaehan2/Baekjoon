import sys
input=sys.stdin.readline

n,m=map(int,input().split())
global d
global c
global r
c,r,d=map(int,input().split())

arr=[]
for i in range(n):
    arr.append(list(map(int,input().split())))

global count
count=0

# 1 1번 실행 -1 종료 2 2번 실행
# 왼쪽 3 오른쪽 1 위쪽 0 아래쪽 2

def robot():
    global d
    global c
    global r
    global count

    #로봇이 위를 보고 있을 때
    if d==0:
        #네 방향 모두 청소가 이미 되어있거나 벽일 때
        if arr[c][r-1]>=1 and arr[c][r+1]>=1 and arr[c-1][r]>=1 and arr[c+1][r]>=1:
            # 뒤쪽 방향이 벽이라 후진도 할 수 없는 경우
            if arr[c+1][r]==1: return -1
            #아닌 경우
            else:
                c+=1
                return 2
            
        # 왼쪽 방향에 아직 청소하지 않은 공간이 존재한다면, 그 방향으로 회전한 다음 한 칸을 전진하고 1번부터 진행한다.
        elif arr[c][r-1]==0: 
            d=3
            r-=1
            arr[c][r]=2
            return 1
        
        # 왼쪽 방향에 청소할 공간이 없다면, 그 방향으로 회전하고 2번으로 돌아간다.
        elif arr[c][r-1]>=1: 
            d=3
            return 2

    #로봇이 오른쪽을 보고 있을 때
    elif d==1:
        #네 방향 모두 청소가 이미 되어있거나 벽일 때
        if arr[c][r-1]>=1 and arr[c][r+1]>=1 and arr[c-1][r]>=1 and arr[c+1][r]>=1:
            # 뒤쪽 방향이 벽이라 후진도 할 수 없는 경우
            if arr[c][r-1]==1: return -1
            #아닌 경우
            else:
                r-=1
                return 2

        # 왼쪽 방향에 아직 청소하지 않은 공간이 존재한다면, 그 방향으로 회전한 다음 한 칸을 전진하고 1번부터 진행한다.
        elif arr[c-1][r]==0: 
            d=0
            c-=1
            arr[c][r]=2
            return 1
        
        # 왼쪽 방향에 청소할 공간이 없다면, 그 방향으로 회전하고 2번으로 돌아간다.
        elif arr[c-1][r]>=1:
            d=0
            return 2

    #로봇이 아래쪽을 보고 있을 때
    elif d==2:
        #네 방향 모두 청소가 이미 되어있거나 벽일 때
        if arr[c][r-1]>=1 and arr[c][r+1]>=1 and arr[c-1][r]>=1 and arr[c+1][r]>=1:
            # 뒤쪽 방향이 벽이라 후진도 할 수 없는 경우
            if arr[c-1][r]==1: return -1
            #아닌 경우
            else:
                c-=1
                return 2

        # 왼쪽 방향에 아직 청소하지 않은 공간이 존재한다면, 그 방향으로 회전한 다음 한 칸을 전진하고 1번부터 진행한다.
        elif arr[c][r+1]==0: 
            d=1
            r+=1
            arr[c][r]=2
            count+=1

        # 왼쪽 방향에 청소할 공간이 없다면, 그 방향으로 회전하고 2번으로 돌아간다.
        elif arr[c][r+1]>=1:
            d=1
            return 2
    #로봇이 왼쪽을 보고 있을 때
    elif d==3:
        #네 방향 모두 청소가 이미 되어있거나 벽일 때
        if arr[c][r-1]>=1 and arr[c][r+1]>=1 and arr[c-1][r]>=1 and arr[c+1][r]>=1:
            # 뒤쪽 방향이 벽이라 후진도 할 수 없는 경우
            if arr[c][r+1]==1: return -1
            #아닌 경우
            else:
                r+=1
                return 2
        
        # 왼쪽 방향에 아직 청소하지 않은 공간이 존재한다면, 그 방향으로 회전한 다음 한 칸을 전진하고 1번부터 진행한다.
        elif arr[c+1][r]==0: 
            d=2
            c+=1
            arr[c][r]=2
            return 1

        # 왼쪽 방향에 청소할 공간이 없다면, 그 방향으로 회전하고 2번으로 돌아간다.
        elif arr[c+1][r]>=1:
            d=2
            return 2

n=1
while n!=-1:
    if n==1:
        count+=1
        arr[c][r]=2
    elif n==2: pass
    elif n==-1: break
    n=robot()
print(count)