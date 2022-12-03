import sys
T=int(sys.stdin.readline())

arr=[(1),(2,4,8,6),(3,9,7,1),(4,6),(5),(6),(7,9,3,1),(8,4,2,6),(9,1),(10)]

for i in range(T):
    a,b=map(int,sys.stdin.readline().split())
    a=a%10
    
    if a==0:
        print(10)
    elif a==1 or a==5 or a==6:
        print(a)
    elif a==4 or a==9:
        n=(b%2)-1
        if n==-1: n=1
        print(arr[a-1][n])
    else:
        n=(b%4)-1
        if n==-1: n=3
        print(arr[a-1][n])