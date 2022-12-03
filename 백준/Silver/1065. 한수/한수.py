N=int(input())
def f(i):
    i=str(i)
    if int(i)==0:
        return 0
    elif len(i)==2 or len(i)==1:
        return 1
    else :
        for j in range(len(i)):
            dif=int(i[0])-int(i[1])
            start=0
            for k in range(len(i)-1):
                if int(i[start])-int(i[start+1])==dif:
                 start+=1
                else:
                    return 0
            return 1

        
global count
count=0
for i in range(1,N+1):
    count=count+f(i)

print(count)

