import sys

result=[]
while 1:
   M=sys.stdin.readline().split()
   if ' '.join(M)=='# 0 0': break
   if int(M[1])>17 or int(M[2])>=80:
      result.append(M[0]+' '+'Senior')
   else:
      result.append(M[0]+' '+'Junior')

print('\n'.join(result))