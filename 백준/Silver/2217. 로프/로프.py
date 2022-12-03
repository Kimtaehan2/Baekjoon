import sys
input=sys.stdin.readline
n=int(input())
rope=[(int(input()))for i in range(n)]
rope.sort()
rope_count=len(rope)

for i in range(n):
    rope[i]=rope[i]*(rope_count-i)

print(max(rope))