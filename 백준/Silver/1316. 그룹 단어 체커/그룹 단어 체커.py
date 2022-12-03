N=int(input())


def f(STR):
    for j in range(len(STR)-1):
        if STR.find(STR[j])>STR.find(STR[j+1]):
            return 0
    return 1
count=0
for i in range(N):
    STR=str(input())
    count+=f(STR)
print(count)