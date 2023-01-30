import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n,m = map(int,input().split())

graph = [list(map(int,input().split())) for i in range(n)]
dp = [[-1]*m for i in range(n)]
dire = [(0,1),(0,-1),(1,0),(-1,0)]


def dfs(x,y):
    if x == m-1 and y == n-1:
        dp[y][x] = 1
        return 1
    cnt = 0
    for d in dire:
        if x + d[0] < 0 or x + d[0] > m-1:
            continue
        if y + d[1] < 0 or y + d[1] > n-1:
            continue
        if graph[y+d[1]][x+d[0]] < graph[y][x]:
            if dp[y+d[1]][x+d[0]] != -1:
                cnt += dp[y+d[1]][x+d[0]]
            else:
                cnt += dfs(x+d[0],y+d[1])
    dp[y][x] = cnt
    return cnt
dfs(0,0)
print(dp[0][0])