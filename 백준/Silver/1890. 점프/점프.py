import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n = int(input())

graph = [list(map(int,input().split())) for i in range(n)]
dp = [[-1]*n for i in range(n)]


def dfs(x,y):
    # 가장 오른쪽 아래 칸에 도달했을 때
    if x == n-1 and y == n-1:
        dp[y][x] = 1
        return 1
    
    cnt = 0

    add = graph[y][x]

    # 가장 오른쪽 아래 칸이 아닌 종착지에 도달했을 때
    if add == 0 :
        dp[y][x] = 0
        return 0

    # cnt = 오른쪽으로 점프하는 경우의 수 + 아래로 점프하는 경우의 수
    if x + add < n:
        # dp_table에 저장이 되지 않았다면
        if dp[y][x+add] == -1:
            cnt += dfs(x+add,y)
        # 저장이 되어 있다면
        else:
            cnt += dp[y][x+add]

    if y + add < n:
        # dp_table에 저장이 되지 않았다면
        if dp[y+add][x] == -1:
            cnt += dfs(x,y+add)
        # 저장이 되어 있다면
        else:
            cnt += dp[y+add][x]
    
    dp[y][x] = cnt
    return cnt

dfs(0,0)
print(dp[0][0])