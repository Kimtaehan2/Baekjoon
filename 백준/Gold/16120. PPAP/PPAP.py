import sys
input=sys.stdin.readline

word=list(input().strip())
stack=[]
#스택에 넣어서 PPAP가 되면 바로 P로 다시 어펜드

for i in range(len(word)):
    stack.append(word[i])
    if len(stack)>=4:
        if stack[-4:]==['P','P','A','P']:
            for i in range(4):
                stack.pop()
            stack.append('P')
   

if stack==['P'] or stack==['P','P','A','P']:
    print('PPAP')
else: print('NP')