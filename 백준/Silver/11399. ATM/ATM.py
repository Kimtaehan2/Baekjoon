n=int(input())

atm=list(map(int,input().split()))

atm.sort()

m=0
result=[]
for i in range(n):
  m+=atm[i]
  result.append(m)
print(sum(result))