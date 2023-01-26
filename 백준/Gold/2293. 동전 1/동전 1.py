import sys
input = sys.stdin.readline

n,k = map(int,input().split())
coin = list(int(input()) for i in range(n))

dp_table = [0]*(k+1)

# 점화식 a[k] = a[k-C] + a[k]


def bottom_up():

    # x : 1~n
    for x in range(1,n+1):
        # i : 0~k
        for i in range(k+1):
            # i > 동전 가격
            if i > coin[x-1]:
                dp_table[i] = dp_table[i-coin[x-1]] + dp_table[i]
            # i == 동전 가격
            elif i == coin[x-1]:
                dp_table[i] = dp_table[i] + 1
            else:
                dp_table[i] = dp_table[i]
    print(dp_table[-1])

bottom_up()