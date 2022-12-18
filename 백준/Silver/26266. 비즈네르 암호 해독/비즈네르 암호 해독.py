import sys
input = sys.stdin.readline

alpha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
check = [0]*26
word = input().strip()
password = input().strip()

passwordkey = []
wordkey = []
newkey = []
for i in range(len(word)):
  wordkey.append(alpha.index(word[i])+1)
for i in range(len(password)):
  passwordkey.append(alpha.index(password[i])+1)
for i in range(len(wordkey)):
  new = passwordkey[i]-wordkey[i]
  if new < 0:
    newkey.append(26 + new)
  else: 
    newkey.append(new)
result = 0
for i in range(1,len(word)+1):
  if len(word)%(i) == 0:
    if newkey[:i]*(len(word)//i)==newkey:
      result = newkey[:i]
      break
for i in result:
  print(alpha[i-1],end='')