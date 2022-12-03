import sys

def find_next_min(i,S):
    result=[]
    for j in range(0,i):
        if num[i-j-1]<num[i]:
            result.append(S[i-j-1]+num[i])
            
    # 현재 값을 이어 붙일 수 있는 이전까지 나온 S 중에서 가장 큰 값을 S에 저장
    if len(result)!=0:
        S.append(max(result))
        return
    # 만약 지금 값이 가장 작다면 지금 값을 저장
    S.append(num[i])
    return 

n=int(input())
num=list(map(int,input().split()))

def dp(n):
    if n==1: return num[0]
    S=[num[0]]
    for i in range(1,n):
        
        find_next_min(i,S)
    return max(S)

print(dp(n))