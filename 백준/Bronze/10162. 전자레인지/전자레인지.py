n=int(input())

arr=(360,60,10)
result=[]
for i in arr:
  result.append(n//i)
  n=n%i

if n!=0: print(-1)
else: print(*result)