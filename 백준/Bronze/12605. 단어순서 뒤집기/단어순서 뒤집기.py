import sys

n=int(sys.stdin.readline())
result=[]

for i in range(n):
    word=sys.stdin.readline().split()
    word.reverse()
    result.append(word)

for i in range(1,n+1):
    print("Case #%i: "%i+' '.join(result[i-1]))
