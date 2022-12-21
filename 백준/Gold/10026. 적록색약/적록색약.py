import sys
import copy
from collections import deque
input = sys.stdin.readline

n = int(input())

dire = [(1,0),(-1,0),(0,1),(0,-1)]
graph1 = [list(input().strip()) for i in range(n)]
graph2 = copy.deepcopy(graph1)

def bfs(x,y,color):
    cnt = 0
    que = deque([[x,y]])
    while que:
        new = deque.popleft(que)
        x,y = new[0],new[1]
        if graph1[y][x] != 0:
            graph1[y][x] = 0
            for d in dire:
                if x+d[0] < 0 or x+d[0] > n-1:
                    continue
                if y+d[1] < 0 or y+d[1] > n-1:
                    continue
                if graph1[y+d[1]][x+d[0]] == color:
                    que.append([x+d[0],y+d[1]])
            cnt = 1
    return cnt

def bfs_cs(x,y,color):
    if color == 'G' or color == 'R':
        color1 = 'G'
        color2 = 'R'
    else: 
        color1 = color
        color2 = color
    cnt = 0
    que = deque([[x,y]])
    while que:
        new = deque.popleft(que)
        x,y = new[0],new[1]
        if graph2[y][x] != 0:
            graph2[y][x] = 0
            for d in dire:
                if x+d[0] < 0 or x+d[0] > n-1:
                    continue
                if y+d[1] < 0 or y+d[1] > n-1:
                    continue
                if graph2[y+d[1]][x+d[0]] == color1 or graph2[y+d[1]][x+d[0]] == color2:
                    que.append([x+d[0],y+d[1]])
            cnt = 1
    return cnt

cnt1 = 0
cnt2 = 0
for y in range(n):
    for x in range(n):
        cnt1 += bfs(x,y,graph1[y][x])
for y in range(n):
    for x in range(n):
        cnt2 += bfs_cs(x,y,graph2[y][x]) 
print(cnt1,cnt2)