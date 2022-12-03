import sys
input=sys.stdin.readline

n,m=map(int,input().split())


none_listen=set()
none_look=set()
for i in range(n):
  none_listen.add(input().strip())
for i in range(m):
  none_look.add(input().strip())

memberset=none_listen&none_look
print(len(memberset))
print('\n'.join(sorted(memberset)))