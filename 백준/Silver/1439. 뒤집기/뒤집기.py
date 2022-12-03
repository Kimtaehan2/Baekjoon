import sys
import math
input=sys.stdin.readline

word=list(map(int,input().strip()))
result=[word[0]]
for i in range(1,len(word)):
    if word[i]!=result[-1]:
        result.append(word[i])
if result[0]==result[-1]:
    print(math.ceil(len(result)/2)-1)
else: print(math.ceil(len(result)/2))
