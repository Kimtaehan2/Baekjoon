import sys
input = sys.stdin.readline

w = ['a', 'e', 'i', 'o', 'u']

while 1:
    words = input().rstrip().lower()
    if words == '#':
        break
    cnt = 0
    for i in w:
        cnt += words.count(i)
    print(cnt)