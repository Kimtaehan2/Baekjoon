import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    n = int(input())
    # 위에 있는 스티커와 아래에 있는 스티커를 나누어 입력받음
    score_up = list(map(int,input().split()))
    score_down = list(map(int,input().split()))

    # 예외처리
    if n == 1:
        print(max(score_up[0],score_down[0]))
        continue

    # 떼야 할 스티커가 위일 경우의 dp_table
    dp_table_up = [score_up[0],score_down[0]+score_up[1]]
    # 떼야 할 스티커가 아래일 경우의 dp_table
    dp_table_down = [score_down[0],score_up[0]+score_down[1]]

    for i in range(2,n):
        # 점화식
        dp_table_up.append(max(dp_table_down[i-1],dp_table_down[i-2]) + score_up[i])
        dp_table_down.append(max(dp_table_up[i-1],dp_table_up[i-2]) + score_down[i])
    
    print(max(dp_table_up[-1],dp_table_down[-1]))