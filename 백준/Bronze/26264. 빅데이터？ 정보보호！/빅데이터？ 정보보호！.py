import sys
input = sys.stdin.readline

n = int(input())

string = input()
security = string.count('s')
bigdata = n-security

if security == bigdata:
  print("bigdata? security!")
elif security > bigdata:
  print("security!")
else: print("bigdata?")