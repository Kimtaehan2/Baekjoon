list=[]

n=int(input())

result=[]
for i in range(n):
    name=input()
    namelist=name.split()
    if namelist[0]=='push':
        list.append(namelist[1])
    if namelist[0]=='pop':
        if len(list)==0: result.append('-1')
        else: result.append(str(list.pop()))
    if namelist[0]=='size':
        result.append(str(len(list)))
    if namelist[0]=='empty':
        if len(list)==0:
            result.append('1')
        else: result.append('0')
    if namelist[0]=='top':
        if len(list)==0:
            result.append('-1')
        else: 
            f=list.pop()
            result.append(str(f))
            list.append(f)
        

print('\n'.join(result))
