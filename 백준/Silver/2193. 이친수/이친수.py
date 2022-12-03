import sys

n=int(input())

def dp(n):
    if n==1: return 1
    elif n==2: return 1
    # 0과1을 구분하기 위해 2개의 리스트를 만들어 준다
    count0=[0,1]
    count1=[1,0]

    for i in range(2,n):
        count0.append(count0[i-1]+count1[i-1])
        count1.append(count0[i-1])
    return count1[-1]+count0[-1]

print(dp(n))