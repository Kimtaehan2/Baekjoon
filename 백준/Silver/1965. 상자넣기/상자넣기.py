import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int,input().split()))

# 자신보다 작은 상자가 등장하면 그 상자의 저장된 수 + 1
# 자신보다 작은 상자가 등장하지 않는다면 1
def find(x,dp_table):
    result = [1]
    for i in range(1,x+1):
        if arr[x-i] < arr[x]:
            result.append(dp_table[x-i] + 1)
    return max(result)

def bottom_up():
    if n == 1:
        return 1

    dp_table = [1]

    for i in range(1,n):
        dp_table.append(find(i,dp_table))

    print(max(dp_table))

bottom_up()