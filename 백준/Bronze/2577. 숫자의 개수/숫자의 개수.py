A=int(input())
B=int(input())
C=int(input())

MUL=A*B*C
MUL=str(MUL)
count=[0,0,0,0,0,0,0,0,0,0]
for i in range(len(MUL)):
    for j in range(10):
        if int(MUL[i])==j:
            count[j]=count[j]+1

for i in range(10):
    print(count[i])

