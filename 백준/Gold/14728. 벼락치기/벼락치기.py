import sys
input=sys.stdin.readline

N,T = map(int,input().split())
arr : list = [list(map(int,input().split()))for i in range(N)]
dp_table : list = [[0 for i in range(T+1)] for i in range(N+1)]

def dp(N,T):
    #(1~N 까지)
    for i in range(1,N+1):
        # (1~T 까지)
        for t in range(1,T+1):
            # 시간이 되지 않아도 이전 솔루션을 활용함
            if arr[i-1][0]>t: 
                dp_table[i][t]=dp_table[i-1][t]
            else:
                dp_table[i][t]=max(dp_table[i-1][t],dp_table[i-1][t-arr[i-1][0]]+arr[i-1][1])
    return dp_table[-1][-1]
print(dp(N,T))