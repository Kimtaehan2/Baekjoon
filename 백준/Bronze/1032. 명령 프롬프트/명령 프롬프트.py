
n=int(input())

str1=str(input())
liststr=list(map(str,str1))

for i in range(n-1):
    str2=str(input())
    for j in range(len(str1)):
        if str1[j]!=str2[j]:
            liststr[j]='?'

print("".join(liststr))