import sys
#리스트 insert의 시간복잡도가 커서 시간 초과 발생 -> 스택 이용

#문장을 왼쪽 스택에 받음
Rstack=[]
Lstack=list(sys.stdin.readline().strip())

#n입력
n=int(sys.stdin.readline())

for i in range(n):
    strput=sys.stdin.readline().strip()
    #입력이 L이고, 왼쪽 스택이 0이 아닐때 왼쪽 스택을 팝 하는 동시에 오른쪽 스택에 푸쉬
    if 'L'==strput[0] and len(Lstack)!=0: 
        Rstack.append(Lstack.pop())
    #입력이 D이고, 오른쪽 스택이 0이 아닐때 오른쪽 스택을 팝 하는 동시에 왼쪽 스택에 푸쉬
    if 'D'==strput[0] and len(Rstack)!=0:
        Lstack.append(Rstack.pop())
    #D는 커서 왼쪽을 삭제하는 것이므로 Lstack에서 pop사용
    if 'B'==strput[0] and len(Lstack)!=0:
        Lstack.pop()
    #P는 왼쪽 스택에 입력받은 문자를 append 해줌
    if 'P'==strput[0]:
        Lstack.append(strput[2])


#출력은 두 스택을 더해서 출력 (오른쪽 스택은 뒤집어 줌)
print(''.join(Lstack+Rstack[::-1]))
