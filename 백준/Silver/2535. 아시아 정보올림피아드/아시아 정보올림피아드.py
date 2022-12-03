import sys
input=sys.stdin.readline
n=int(input())
students=[list(map(int,input().split())) for _ in range(n)]
result=[]
students=sorted(students,key=lambda x: x[2])

result.append(students.pop())
result.append(students.pop())
while len(result)!=3 and students:
    p=students.pop()
    if result[0][0]==result[1][0]:
        if p[0]!=result[0][0] and p[0]!=result[1][0]:
            result.append(p)
    else: result.append(p)
for i in result:
    print(i[0],i[1])
