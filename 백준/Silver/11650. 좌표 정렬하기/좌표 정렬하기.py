n=int(input())
num=[]

for i in range(n):
    num.append(list(map(int,input().split())))

num.sort()
for i in range(n):
    print(num[i][0],end=" ")
    print(num[i][1])