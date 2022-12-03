import sys

result=[]
#한 글자씩 리스트로 입력받음
stack=list(sys.stdin.readline().strip())
# stack.reverse()
#스택에 아무것도 없을때까지 반복

while len(stack)!=0:
    word=stack.pop()
    #스택에서 한 글자식 pop 하면서 >나,' '가 나오면 temp에 뒤집어 저장
    if word=='>':
        temp=''
        while word!='<':
            word=stack.pop()
            temp=temp+word
        result.append(temp[::-1]+'>')
    else: 
        result.append(word)

anwser=[]

temp=''
for i in result:
    if len(i)!=1:
        anwser.append(' '.join(temp.split()[::-1]))
        anwser.append(i)
        temp=''
    else: 
        temp=temp+i
anwser.append(' '.join(temp.split()[::-1]))

print(''.join(anwser[::-1]))