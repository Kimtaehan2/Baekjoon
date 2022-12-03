import sys
input=sys.stdin.readline

infix : list = list(input().strip())

stack : list =[]
operate : list = []
operand : list = []
result : list = []

while infix:
    p=infix.pop()
    if p=='(':
        while stack[-1]!=')':
            result.append(stack.pop())
        result.reverse()
        while result:
            a=result.pop()
            if a=='*' or a=='/':
                if len(operate)!=0 and (operate[-1]=='*' or operate[-1]=='/'):
                    # 이거 안고쳐서 틀렸었음 ㅋㅋㅋㅋ 진짜 하
                    operand.append(operate.pop())
                    operate.append(a)
                else: operate.append(a)
            elif a=='+' or a=='-':
                if len(operate)!=0 and (operate[-1]=='*' or operate[-1]=='/'):
                    while operate:
                        operand.append(operate.pop())
                    operate.append(a)
                elif len(operate)==0:
                    operate.append(a)
                else:
                    while operate:
                        operand.append(operate.pop())
                    operate.append(a)
            else:
                operand.append(a)
        while operate:
            operand.append(operate.pop())
        stack.pop()
        
        stack.append(''.join(operand))
        operand.clear()
    else: stack.append(p)

while stack:
    result.append(stack.pop())
result.reverse()
while result:
    a=result.pop()
    if a=='*' or a=='/':
        if len(operate)!=0 and (operate[-1]=='*' or operate[-1]=='/'):
            operand.append(operate.pop())
            operate.append(a)
        else:
            operate.append(a)
    elif a=='+' or a=='-':
        if len(operate)!=0 and (operate[-1]=='*' or operate[-1]=='/'):                
            while operate:
                operand.append(operate.pop())
            operate.append(a)
        elif len(operate)==0:
            operate.append(a)
        else:
            while operate:
                operand.append(operate.pop())
            operate.append(a)
    else:
        operand.append(a)
while operate:
    operand.append(operate.pop())
print(''.join(operand))