import sys
from collections import deque
input=sys.stdin.readline

n,m=map(int,input().split())

graph=[list(map(int,input().split())) for i in range(n)]
visited=[[0 for i in range(m)] for i in range(n)]

# p[0] : x, p[1] : y
def bfs(x,y):
    if visited[y][x]==1 or graph[y][x]==0: return 0
    count=0
    que=deque([[x,y]])

    while que:
        p=deque.popleft(que)
        if visited[p[1]][p[0]]==0:
            count+=1
            visited[p[1]][p[0]]=1

            if p[0]-1>=0 and graph[p[1]][p[0]-1]==1:
                que.append([p[0]-1,p[1]])
            if p[0]+1<m and graph[p[1]][p[0]+1]==1:
                que.append([p[0]+1,p[1]])
            if p[1]-1>=0 and graph[p[1]-1][p[0]]==1:
                que.append([p[0],p[1]-1])
            if p[1]+1<n and graph[p[1]+1][p[0]]==1:
                que.append([p[0],p[1]+1])
    return count

result=[]
for i in range(n):
    for j in range(m):
        start=0
        last=bfs(j,i)
        if start!=last:
            result.append(last)

print(len(result),max(result) if len(result)!=0 else 0,sep='\n')