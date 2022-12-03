import sys
input=sys.stdin.readline

# find_next_minlen 정의
def find_next_minlen(i,S):
    result=[]
    for j in range(0,i):
        # 구성하는 값도 출력하기 위해 리스트 연산을 이용하였다
        if num[i-j-1]<num[i]:
            result.append((S[i-j-1][0]+1,S[i-j-1][1]+[num[i]]))
            
    # 현재 값을 이어 붙일 수 있는 이전까지 나온 S 중에서 가장 긴 값을 S에 저장
    if len(result)!=0:
        S.append(max(result))
        return
    # 긴 값이 없다면 길이를 1로,  초기화 하여 저장
    S.append((1,[num[i]]))
    return 

#dp
def dp(n):
    if n==1: return (1,[num[0]])
    #sub solution은 (num[i]+이전에 구한 가장 긴 증가하는 부분 수열, [구성하는 값])이다
    S=[(1,[num[0]])]
    for i in range(1,n):
        find_next_minlen(i,S)
    return max(S)

#---------------------------------------------------------------------
n=int(input())
num=list(map(int,input().split()))
print_dp=dp(n)
print(print_dp[0])
print(*print_dp[1])