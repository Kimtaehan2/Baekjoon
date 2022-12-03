N,X=map(int,input().split())
L=list(map(int,input().split()))

for i in range(N):
    if X>L[i]:
        print(L[i],end=" ")