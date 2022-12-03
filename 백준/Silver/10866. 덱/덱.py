import sys

n=int(sys.stdin.readline())
result=[]
#덱을 반으로 쪼개 앞에서 넣는 스택과 뒤에서 넣는 스택으로 구현함
front_deq=[]
back_deq=[]

for i in range(n):
    #공백을 기준으로 리스트로 입력받음
    order=sys.stdin.readline().split()

    if order[0]=='push_front':
        front_deq.append(str(order[1]))
    if order[0]=='push_back':
        back_deq.append(str(order[1]))

    if order[0]=='pop_front':
        if len(front_deq)+len(back_deq)==0: result.append('-1')
        elif len(front_deq)==0 and len(back_deq)!=0: result.append(str(back_deq.pop(0)))
        else: result.append(str(front_deq.pop()))
    if order[0]=='pop_back':
        if len(front_deq)+len(back_deq)==0: result.append('-1')
        elif len(back_deq)==0 and len(front_deq)!=0: result.append(str(front_deq.pop(0)))
        else: result.append(str(back_deq.pop()))
    
    if order[0]=='size': result.append(str(len(front_deq)+len(back_deq)))
    if order[0]=='empty':
        if len(front_deq)+len(back_deq)==0: result.append('1')
        else: result.append('0')

    if order[0]=='front': 
        if len(front_deq)+len(back_deq)==0: result.append('-1')
        elif len(front_deq)==0 and len(back_deq)!=0: result.append(str(back_deq[0]))
        else: result.append(str(front_deq[-1]))
    if order[0]=='back':
        if len(front_deq)+len(back_deq)==0: result.append('-1')
        elif len(back_deq)==0 and len(front_deq)!=0: result.append(str(front_deq[0]))
        else: result.append(str(back_deq[-1]))

print('\n'.join(result))
