import sys

#()개수 체크 함수
def count_PS(PS):
    if PS.count('(')==PS.count(')'): return 1
    else: return 0
#(개수 왼쪽에 더 많은지 체크하는 함수
def L_judge_PS(PS):
    count_L=0
    count_R=0
    for i in PS:
        if count_L<count_R: return 0
        if i=='(': count_L+=1
        elif i==')':count_R+=1
    return 1
#)개수 오른쪽에 더 많은지 체크하는 함수
def R_judge_PS(PS):
    count_L=0
    count_R=0
    for i in PS:
        if count_R<count_L: return 0
        
        if i=='(': count_L+=1
        elif i==')':count_R+=1
        
    return 1

result=[]
list=[]
n=int(sys.stdin.readline())
for i in range(n):
    PS=sys.stdin.readline().strip()
    list.append(PS)
    if L_judge_PS(PS)==1 and count_PS(PS)==1 and R_judge_PS(PS[::-1])==1: result.append("YES")
    else: result.append("NO")


print('\n'.join(result))