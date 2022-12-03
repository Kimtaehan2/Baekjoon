import sys

A=list(sys.stdin.readline().strip())
B=list(sys.stdin.readline().strip())

result=[]
result2=[]
for i in range(14):
    if i==0: 
        for i in range(7):
            Sol=int(A[i])+int(B[i])
            if Sol>=10: result.append(Sol%10)
            else: result.append(Sol)
            Sol=int(A[i+1])+int(B[i])
            if Sol>=10: result.append(Sol%10)
            else: result.append(Sol)
        if (int(A[-1])+int(B[-1]))>=10: result.append((int(A[-1])+int(B[-1]))%10)
        else: result.append(int(A[-1])+int(B[-1]))
    if i%2!=0:
        for i in range(len(result)-1):
            Sol=int(result[i])+int(result[i+1])
            if Sol>=10: result2.append(Sol%10)
            else: result2.append(Sol)
        result=[]
    else:
        for i in range(len(result2)-1):
            Sol=int(result2[i])+int(result2[i+1])
            if Sol>=10: result.append(Sol%10)
            else: result.append(Sol)
        result2=[]
print(result2[0],result2[1],sep='')