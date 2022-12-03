import sys
n,m=map(int,sys.stdin.readline().split())
setword=set()

for i in range(n):
    setword.add(sys.stdin.readline().strip())

count=0
for i in range(m):
    word=sys.stdin.readline().strip()
    if word in setword:
        count+=1

print(count)