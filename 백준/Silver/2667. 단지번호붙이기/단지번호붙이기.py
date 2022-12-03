import sys
input=sys.stdin.readline
sys.setrecursionlimit(10**6)
l=[(0,1),(0,-1),(1,0),(-1,0)]


def dfs(y,x):
    global n
    global count
    if world[y][x]==0: return
    count+=1
    world[y][x]=0
    for i in l:
        if y+i[0]<0 or y+i[0]>n-1 or x+i[1]<0 or x+i[1]>n-1: pass
        else:   
            if world[y+i[0]][x+i[1]]==1:
                dfs(y+i[0],x+i[1])


n=int(input())
world=[list(map(int,input().strip())) for i in range(n)]
count=0
result=[]
for i in range(n):
    for j in range(n):
        if world[i][j]==1:
            result.append(count)
            count=0
        dfs(i,j)
result.append(count)
result.sort()
print(len(result)-1,*result[1:],sep='\n')
