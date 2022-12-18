import sys
input = sys.stdin.readline

n = int(input())

l = [input().split() for i in range(n)]
l.sort()
s = set()
last = ''
result = []
new = []
for i in l:
  s.add(i[0])
  if i[0] == last:
    new.append(i[1])
  else:
    last = i[0]
    result.append(new)
    new = []
    new.append(i[1])
result.append(new)
del result[0]

s = list(s)
s.sort()
for i in range(len(result)):
  result[i] = result[i][::-1]

for i in range(len(result)):
  for j in range(len(result[i])):
    print(s[i],result[i][j])