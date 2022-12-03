import sys
from collections import deque
input=sys.stdin.readline

def check(i):
    if i>='A' and i<='Z': return True
    elif i>='a' and i<='z': return True
    elif i=='-': return True
    else: return False


result=[]
id=0
while (1):
    word=list(input().rstrip())
    reword=''
    for i in word:
        if check(i): reword+=i
        else: 
            reword+=' '
    reword=reword.strip()
    W=reword.rstrip().split()
    length=[]
    for i in W:
        if i=='E-N-D': break
        length.append([len(i),id,i])
        id-=1
    if len(length)!=0:
        length.sort()
        result.append(length[-1])
        if W[-1]=='E-N-D': break
    if len(W)!=0:
        if W[-1]=='E-N-D': break
result.sort()
print(result[-1][2].lower())
