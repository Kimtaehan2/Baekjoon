import sys

n=int(input())
arr=list(map(int,sys.stdin.readline().split()))

def dp(n):
    # n=1,n=2일때는 솔루션 적용이 안되므로 예외처리
    if n==1: return arr[0]
    if n==2: return max(arr[0],arr[0]+arr[1])

    sum=[arr[0]]
    for i in range(1,n):
        # 전까지의 연속합+새로운 수와 연속합을 끊고 인덱스-1의 수+새로운 수와 비교
        sum.append(max(arr[i-1]+arr[i],sum[i-1]+arr[i]))
    #끊긴 연속합끼리는 비교할 수 없기에 max로 가장 큰 연속합 리턴
    return max(sum+arr)
    
print(dp(n))