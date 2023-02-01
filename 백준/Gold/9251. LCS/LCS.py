import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

A = input().strip()
B = input().strip()

dp_table = [[-1]*(len(B)+1) for i in range(len(A)+1)]

def lcs(i,j):
    if i == 0 or j == 0:
        dp_table[i][j] = 0
        return 0
    # 맨 뒤의 문자가 같은 경우
    if A[i-1] == B[j-1]:
        if dp_table[i-1][j-1] != -1:
            dp_table[i][j] = dp_table[i-1][j-1] + 1
        else:
            dp_table[i][j] = lcs(i-1,j-1) + 1
    else:
        # A 뒤의 문자를 선택하는 경우와 B 뒤의 문자를 선택하는 경우 중 큰 경우 채택
        if dp_table[i][j-1] != -1:
            a = dp_table[i][j-1]
        else:
            a = lcs(i,j-1)
        if dp_table[i-1][j] != -1:
            b = dp_table[i-1][j]
        else:
            b = lcs(i-1,j)
        dp_table[i][j] = max(a,b)
    return dp_table[i][j]

lcs(len(A),len(B))
print(dp_table[-1][-1])