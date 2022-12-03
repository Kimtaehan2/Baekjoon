n=int(input())

for i in range(n):
    H,W,N=map(int,input().split())
    Y=N%H
    X=(N//H)+1
    if N%H==0:
        Y=H
        X=N//H
    print(Y*100+X)
