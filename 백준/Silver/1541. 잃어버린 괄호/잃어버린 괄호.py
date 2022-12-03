import sys
input=sys.stdin.readline

n=(input().replace('-',' - ').replace('+', ' + ')).split()

#연산자가 나올 때마다 sum을 재정의
#+가 나온다면 -가 나올때까지 계속 더함
#-가 나온다면 +가 나올때까지 계속 더함
sum=int(n[0])
cmd=-1
for i in range(len(n)):
  
  if n[i]=='+':
    if cmd==0:
        cmd==2
    else: cmd=1
  elif n[i]=='-':
    cmd=0
  else:
    if cmd==1:
      sum+=int(n[i])
    elif cmd==0:
      sum-=int(n[i])
    elif cmd==2:
      sum-=int(n[i])
print(sum)
