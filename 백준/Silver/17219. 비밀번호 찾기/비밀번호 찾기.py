import sys
input=sys.stdin.readline

n,m=map(int,input().split())

password={}
for i in range(n):
  adr,pw=map(str,input().strip().split())
  password[adr]=pw

for i in range(m):
  print(password[input().strip()])