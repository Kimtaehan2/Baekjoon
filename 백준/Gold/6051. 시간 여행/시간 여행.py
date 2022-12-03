import sys
input=sys.stdin.readline
n=int(input())
Query=[[] for i in range(80001)]
C=1
for i in range(n):
  cmd=list(input().split())
  if cmd[0]=='t':
    for i in Query[int(cmd[1])-1]:
      Query[C].append(i)
    if len(Query[C])==0:
        print(-1)
    else: print(Query[C][-1])
  else:
    for i in Query[C-1]:
      Query[C].append(i)
  if cmd[0]=='a':
    Query[C].append(cmd[1])
    print(Query[C][-1])
  if cmd[0]=='s':
    if len(Query[C])==0:
      print(-1)
    else:
      Query[C].pop()
      if len(Query[C])==0:
        print(-1)
      else: print(Query[C][-1])
  C+=1