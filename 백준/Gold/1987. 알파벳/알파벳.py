import sys
input = sys.stdin.readline
r,c = map(int,input().split())
graph = [list(input().strip()) for i in range(r)]

dire = [(1,0),(-1,0),(0,1),(0,-1)]
visited = [[True]*c for i in range(r)]
result = [0]
alpha = [0]*26
alpha[ord(graph[0][0])-65] = 1

def back_tracking(depth,x,y):
  for d in dire:
    if x + d[0] < 0 or x + d[0] > c-1:
      continue
    if y + d[1] < 0 or y + d[1] > r-1:
      continue
    #스택 대신 알바벳 체크 리스트로 시간초과 해결
    if visited[y+d[1]][x+d[0]] and alpha[ord(graph[y+d[1]][x+d[0]])-65] == 0:
      alpha[ord(graph[y+d[1]][x+d[0]])-65] = 1
      visited[y+d[1]][x+d[0]] = False
      back_tracking(depth+1,x+d[0],y+d[1])
      alpha[ord(graph[y+d[1]][x+d[0]])-65] = 0
      visited[y+d[1]][x+d[0]] = True
  if result[-1] < depth:
    result.append(depth)
    return
visited[0][0] = False
back_tracking(0,0,0)
print(result[-1]+1)