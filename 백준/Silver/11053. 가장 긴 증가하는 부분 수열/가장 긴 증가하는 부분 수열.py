import sys
input=sys.stdin.readline

# find_next_minlen 정의
def find_next_minlen(i,S):
    result=[]
    for j in range(0,i):
        if num[i-j-1]<num[i]:
            result.append(S[i-j-1]+1)
            
    # 현재 값을 이어 붙일 수 있는 이전까지 나온 S 중에서 가장 긴 값을 S에 저장
    if len(result)!=0:
        S.append(max(result))
        return
    # 긴 값이 없다면 길이를 1로 초기화 하여 저장
    S.append(1)
    return 

#dp
def dp(n):
    if n==1: return 1
    S=[1]
    for i in range(1,n):
        find_next_minlen(i,S)
    return max(S)

#---------------------------------------------------------------------
n=int(input())
num=list(map(int,input().split()))
print(dp(n))