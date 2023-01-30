import sys
input = sys.stdin.readline

N,S = map(int,input().split())

arr = list(map(int,input().split()))

end = 0
start = 0

cur_sum = arr[0]

result = []

while end >= start:
    if end >= N:
        break
    # 현재의 부분합이 S 이상일 때
    if cur_sum >= S:
        result.append(end-start)
        cur_sum -= arr[start]
        start += 1
    # 현재의 부분합이 S 미만일 때
    else:
        end += 1
        if end >= N:
            break
        cur_sum += arr[end]

if len(result) == 0:
    print(0)
else:
    print(min(result)+1)