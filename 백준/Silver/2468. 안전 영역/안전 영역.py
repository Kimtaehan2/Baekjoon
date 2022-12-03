import sys
input=sys.stdin.readline
sys.setrecursionlimit(10**6)
n=int(input())

graph=[list(map(int,input().split())) for i in range(n)]
dif=[0]
l=[(1,0),(-1,0),(0,1),(0,-1)]

def dfs(x,y,depth):
  if check[y][x]==1 or graph[y][x]<=depth: return
  check[y][x]=1
  dif[0]+=1
  for i in l:
    if x+i[0]<0 or x+i[0]>n-1:
      pass
    elif y+i[1]<0 or y+i[1]>n-1:
      pass
    else:
      if graph[y+i[1]][x+i[0]]>depth and check[y+i[1]][x+i[0]]==0:
        dfs(x+i[0],y+i[1],depth)

def play(d):
  count=0
  for i in range(n):
    for j in range(n):
        last=dif[0]
        dfs(j,i,d)
        if last!=dif[0]:
          count+=1
  return count

COU=[0]
dep=0
while 1:
  check=[[0 for i in range(n)] for i in range(n)]
  dif[0]=0
  c=play(dep)
  dep+=1
  if c==0: break
  COU.append(c)

print(max(COU))