import sys
input=sys.stdin.readline

def NUM_X(X):
    stack.append(X)

def POP():
    if len(stack)==0: return -1
    stack.pop()
    return 0

def INV():
    if len(stack)==0: return -1
    stack.append(-int(stack.pop()))
    return 0

def DUP():
    if len(stack)==0: return -1
    stack.append(stack[-1])
    return 0

def SWP():
    if len(stack)<=1: return -1
    first_num=stack.pop()
    second_num=stack.pop()
    stack.append(first_num)
    stack.append(second_num)
    return 0

def ADD():
    if len(stack)<=1: return -1
    first_num=stack.pop()
    second_num=stack.pop()
    if abs(first_num+second_num)>10**9: return -1
    stack.append(first_num+second_num)
    return 0

def SUB():
    if len(stack)<=1: return -1
    first_num=stack.pop()
    second_num=stack.pop()
    if abs(second_num-first_num)>10**9: return -1
    stack.append(second_num-first_num)
    return 0

def MUL():
    if len(stack)<=1: return -1
    first_num=stack.pop()
    second_num=stack.pop()

    if abs(first_num*second_num)>10**9: return -1

    stack.append(first_num*second_num)
    return 0

def DIV():
    if len(stack)<=1: return -1

    first_num=stack.pop()
    second_num=stack.pop()

    if first_num==0: return -1

    
    Q=abs(second_num)//abs(first_num)
    if abs(Q)>10**9: return -1

    if first_num*second_num<0:
        stack.append(-Q)
    else: stack.append(Q)
    return 0

def MOD():
    if len(stack)<=1: return -1

    first_num=stack.pop()
    second_num=stack.pop()

    if first_num==0: return -1
    
    R=abs(second_num)%abs(first_num)
    if abs(R)>10**9: return -1

    if second_num<0:
        stack.append(-R)
    else: stack.append(R)
    return 0

while (1):
    result=[]
    order=[]
    while 1:
        explan=input().split()
        if explan==['END']: 
            order.append(explan)
            break
        if explan==['QUIT']:
            order.append(explan)
            break
        if explan==[]: pass
        else: order.append(explan)
    if order[0]==['QUIT']: break

    N=int(input())
    for _ in range(N):
        input_num=int(input())
        stack=[input_num]
        break_num=0
        for Program in order:
            if Program[0]=='END': break
            if Program[0]=='NUM':
                NUM_X(int(Program[1]))
        
            elif Program[0]=='POP':
                break_num=POP()
        
            elif Program[0]=='INV':
                break_num=INV()
        
            elif Program[0]=='DUP':
                break_num=DUP()

            elif Program[0]=='SWP':
                break_num=SWP()

            elif Program[0]=='ADD':
                break_num=ADD()

            elif Program[0]=='SUB':
                break_num=SUB()

            elif Program[0]=='MUL':
                break_num=MUL()

            elif Program[0]=='DIV':
                break_num=DIV()

            elif Program[0]=='MOD':
                break_num=MOD()
            if break_num==-1: break

        if len(stack)!=1 or break_num==-1:
            result.append('ERROR')
        else: result.append(stack[-1])
    print(*result,sep='\n',end='')
    print('\n')