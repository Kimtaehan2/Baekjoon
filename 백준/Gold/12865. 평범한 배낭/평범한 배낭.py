import sys
input=sys.stdin.readline

n,k=map(int,input().split())

# 각 n개의 물건의 무게와 가치를 입력받는 리스트
arr=[list(map(int,input().split()))for i in range(n)]

# dp_table의 초기값은 0으로 초기화
dp_table : list = [[0 for i in range(k+1)] for i in range(n+1)]

# i : 배낭에 넣을 수 있는 물건, j : 배낭에 넣을 수 있는 무게
def dp(n,k):
    for i in range(1,n+1):
        for j in range(1,k+1):
            # 배낭에 넣을 수 있는 무게 보다 물건의 무게가 작거나 같을 때
            if j>=arr[i-1][0]:
                # 이미 구한 물건을 넣지 않았을 때의 경우의 최대 가치와, 이 물건의 가치 + (최대 무게 - 이 물건의 무게) 일때의 dp_table 가치 값 중 큰 값을
                # dp_table에 저장
                dp_table[i][j]=max(dp_table[i-1][j],arr[i-1][1]+dp_table[i-1][j-arr[i-1][0]])
            else: dp_table[i][j]=dp_table[i-1][j]

    return dp_table[-1][-1]

# 실수한 점: 
# 1. 이전 제출에서는 dp_table[i][j-arr[i-1][0]]로 설정하여 물건이 중복되어 넣어질 수 있었다
# 2. dp_table 중 현재 탐색 중인 물건의 무게보다 작은 경우는 고려하지 못했다
print(dp(n,k))