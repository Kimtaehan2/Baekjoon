import sys
input=sys.stdin.readline

def find_next_maxlen_L(i,S):
    result=[]
    for j in range(0,i):
        if num[i-j-1]<num[i]:
            result.append(S[i-j-1]+1)
            
    if len(result)!=0:
        S.append(max(result))
        return
    S.append(1)
    return

def find_next_maxlen_R(i,S):
    result=[]
    for j in range(0,i):
        if rightnum[i-j-1]<rightnum[i]:
            result.append(S[i-j-1]+1)
            
    if len(result)!=0:
        S.append(max(result))
        return
    S.append(1)
    return 

#dp
def dp_L(n):
    if n==1: return [1]
    S=[1]
    for i in range(1,n):
        find_next_maxlen_L(i,S)
    return S
def dp_R(n):
    if n==1: return [1]
    S=[1]
    for i in range(1,n):
        find_next_maxlen_R(i,S)
    return S
#---------------------------------------------------------------------
n=int(input())
num=list(map(int,input().split()))
rightnum=num[::-1]

S1=dp_L(n)
S2=dp_R(n)
SUM=[]
for i in range(len(S1)):
    SUM.append(S1[i]+S2[len(S1)-i-1]-1)
print(max(SUM))