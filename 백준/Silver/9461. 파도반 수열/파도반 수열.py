import sys
input = sys.stdin.readline

T = int(input())

def bottom_up(N):
    dp_table = [1, 1, 1, 2, 2, 3, 4, 5]

    if N <= 8:
        print(dp_table[N-1])
        return

    for i in range(8,N):
        dp_table.append(dp_table[i-1] + dp_table[i-5])
    print(dp_table[-1])


for _ in range(T):
    N = int(input())
    bottom_up(N)