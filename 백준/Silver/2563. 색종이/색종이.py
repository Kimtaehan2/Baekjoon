n=int(input())

arr=[[0 for i in range(100)] for i in range(100)]

for i in range(n):
    x,y=map(int,input().split())
    
    for i in range(10):
        for j in range(10):
            arr[y-1+i][x-1+j]=1

result=0
for i in range(100):
    result+=sum(arr[i])

print(result)