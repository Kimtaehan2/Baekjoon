n=int(input())
k=int(input())
arr=[[0 for i in range(n+2)] for i in range(n+2)]

# 시작값 초기화
startx,starty=(n-1)//2+1,(n-1)//2+1

arr[starty][startx]=1
if k==1:
    kindex=[n-starty+1,startx]
else: kindex=[]

for i in range(2,n**2+1):
    
    # 주위에 다 0이면 위로 한칸
    if arr[starty][startx+1]==0 and arr[starty][startx-1]==0 and arr[starty+1][startx]==0 and arr[starty-1][startx]==0:
        starty+=1
    # 아래만 0이 아니면 오른쪽으로 한칸
    elif arr[starty][startx+1]==0 and arr[starty][startx-1]==0 and arr[starty+1][startx]==0 and arr[starty-1][startx]!=0:
        startx+=1
    # 왼쪽만 0이 아니면 아래쪽으로 한칸
    elif arr[starty][startx+1]==0 and arr[starty][startx-1]!=0 and arr[starty+1][startx]==0 and arr[starty-1][startx]==0:
        starty-=1
    # 위만 0이 아니면 왼쪽으로 한칸
    elif arr[starty][startx+1]==0 and arr[starty][startx-1]==0 and arr[starty+1][startx]!=0 and arr[starty-1][startx]==0:
        startx-=1
    # 오른쪽만 0이 아니면 위로 한칸
    elif arr[starty][startx+1]!=0 and arr[starty][startx-1]==0 and arr[starty+1][startx]==0 and arr[starty-1][startx]==0:
        starty+=1
    # 왼쪽이랑 위쪽이 0이 아니면 아래로 한칸
    elif arr[starty][startx+1]==0 and arr[starty][startx-1]!=0 and arr[starty+1][startx]!=0 and arr[starty-1][startx]==0:
        starty-=1
    # 오른쪽이랑 위쪽 0이 아니면 왼쪽으로 한칸
    elif arr[starty][startx+1]!=0 and arr[starty][startx-1]==0 and arr[starty+1][startx]!=0 and arr[starty-1][startx]==0:
        startx-=1
    # 왼쪽이랑 아래 오른쪽
    elif arr[starty][startx+1]==0 and arr[starty][startx-1]!=0 and arr[starty+1][startx]==0 and arr[starty-1][startx]!=0:
        startx+=1
    # 오른쪽이랑 아래 위
    elif arr[starty][startx+1]!=0 and arr[starty][startx-1]==0 and arr[starty+1][startx]==0 and arr[starty-1][startx]!=0:
        starty+=1
    if i==k:
        kindex=[n-starty+1,startx]
    arr[starty][startx]=i

arr.reverse()
arr.pop()
arr.pop(0)

for i in arr:
    i.pop(0)
    i.pop()
    print(*i)
print(*kindex)