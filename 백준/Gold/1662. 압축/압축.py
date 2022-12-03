import sys
input=sys.stdin.readline

word=list(input().strip())
stack=[]
while word:
    if word[-1]=='(':
        count=0
        while stack:
            if stack[-1]==')' or stack[-1]=='(': break
            num=stack.pop()
            if type(num)==str:
                count+=1
            elif type(num)==int:
                count+=num
        if len(stack)==0: break
        word.pop()
        mul=int(word.pop())
        stack.pop()
        stack.append(mul*count)
    else:
        p=word.pop()
        stack.append(p)
count=0

while stack:
    if stack[-1]==')' or stack[-1]=='(':
        stack.pop()
    else: 
        num=stack.pop()
        if type(num)==str:
            count+=1
        elif type(num)==int:
            count+=num
print(count)