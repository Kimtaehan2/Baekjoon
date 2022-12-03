import sys
n=int(sys.stdin.readline())
list=[]
for i in range(n):
    word=sys.stdin.readline()[::-1].split()
    list.append(' '.join(word[::-1]))
print('\n'.join(list))
