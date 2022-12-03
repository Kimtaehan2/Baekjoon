import sys
input=sys.stdin.readline

T=int(input())
stair=[]
for i in range(T):
    stair.append(int(input()))

def dp(n):
    if n==1: return stair[0]
    elif n==2: return stair[0]+stair[1]
    elif n==3: return max(stair[0]+stair[2],stair[1]+stair[2])
    #계단 초기값 (n==1,2,3 번째 칸)
    S=[stair[0],stair[0]+stair[1],max(stair[0]+stair[2],stair[1]+stair[2])]

    for i in range(3,n):
        #n번째 칸 + 그 전까지의 최대
        S.append(max(S[i-2]+stair[i],S[i-3]+stair[i-1]+stair[i]))
    return S[-1]

print(dp(T))