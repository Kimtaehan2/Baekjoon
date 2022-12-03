n=int(input())
numlist1=set(map(int,input().split()))
m=int(input())
numlist2=list(map(int,input().split()))
for i in numlist2:
    if i in numlist1:
        print(1)
    else:
        print(0)
