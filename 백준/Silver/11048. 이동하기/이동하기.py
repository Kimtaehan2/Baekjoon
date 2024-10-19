import sys
input = sys.stdin.readline

n,m = map(int,input().split())
candy_cnt_map = [list(map(int,input().split())) for i in range(n)]
dp_table = [[0 for i in range(m)] for i in range(n)]

# bottom-up 방식의 dp
def dp(n,m):
    for i in range(n):
        for j in range(m):
            max_candy = 0
            # 이동 가능한 방향은 3가지
            if j-1 >= 0: # (i,j-1) 방의 dp_table에서의 최댓값 가져오기
                max_candy = max(max_candy, dp_table[i][j-1])
            if i-1 >= 0: # (i-1,j) 방의 dp_table에서의 최댓값 가져오기
                max_candy = max(max_candy, dp_table[i-1][j])
            if i-1 >= 0 and j-1 >= 0: # (i-1,j-1) 방의 dp_table에서의 최댓값 가져오기
                max_candy = max(max_candy, dp_table[i-1][j-1])
            # 최댓값과 현재 방의 캔디 수를 더한 값을 dp_table에 최신화
            dp_table[i][j] = max_candy + candy_cnt_map[i][j]

dp(n,m)
# (N,M)의 dp_table 값을 출력
print(dp_table[-1][-1])

