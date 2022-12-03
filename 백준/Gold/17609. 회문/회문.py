import sys
from collections import deque
input=sys.stdin.readline

n=int(input())

for i in range(n):
  word=deque(list(input().strip()))
  right=-1
  left=0
  C=0
  r1=-2
  l1=0
  r2=-1
  l2=1
  c1=1
  c2=1
  while len(word)>2:
    if word[left]==word[right] and C==0:
      word.pop()
      deque.popleft(word)

    else:
      C=1
      if word[l1]!=word[r1]:
        c1+=1
      if word[l2]!=word[r2]:
        c2+=1
      word.pop()
      deque.popleft(word)
  if len(word)==2 and C==0:
    if word[right]==word[left]: print(0)
    else: print(1)
  elif C==0: print(0)
  elif c1==1 or c2==1: print(1)
  else: print(2)