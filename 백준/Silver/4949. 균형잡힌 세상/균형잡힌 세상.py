import sys

word=list(sys.stdin.readline().rstrip())

def check():
    if len(temp)==1: pass
    elif temp[-2]==')' and temp[-1]=='(':
        temp.pop()
        temp.pop()
    elif temp[-2]==']' and temp[-1]=='[':
        temp.pop()
        temp.pop()



while word!=['.']:
    temp=[]
    while word:
        W=word.pop()
        #만약 (,),[,] 라면 temp에 저장
        if W=='(' or W==')' or W=='[' or W==']':
            temp.append(W)
            check()
    #모든 입력이 끝났을때 temp에 남아있는 것이 없다면 'yes' 남아있다면 'no'
    print('yes' if len(temp)==0 else 'no')
    word=list(sys.stdin.readline().rstrip())