
n = int(input())
list=['"재귀함수가 뭔가요?"','"잘 들어보게. 옛날옛날 한 산 꼭대기에 이세상 모든 지식을 통달한 선인이 있었어.','마을 사람들은 모두 그 선인에게 수많은 질문을 했고, 모두 지혜롭게 대답해 주었지.','그의 답은 대부분 옳았다고 하네. 그런데 어느 날, 그 선인에게 한 선비가 찾아와서 물었어."']
def f(n):
    if n <= 2:
        return '____'
    else:
        return f(n-1)+'____'
for i in range(n+1):
    if i==0:
        print('''어느 한 컴퓨터공학과 학생이 유명한 교수님을 찾아가 물었다.\n"재귀함수가 뭔가요?"\n"잘 들어보게. 옛날옛날 한 산 꼭대기에 이세상 모든 지식을 통달한 선인이 있었어.\n마을 사람들은 모두 그 선인에게 수많은 질문을 했고, 모두 지혜롭게 대답해 주었지.\n그의 답은 대부분 옳았다고 하네. 그런데 어느 날, 그 선인에게 한 선비가 찾아와서 물었어."''')
    elif i==n:
        print(f(i+1)+'"재귀함수가 뭔가요?"')
        print(f(i+1)+'"재귀함수는 자기 자신을 호출하는 함수라네"')
    else :
        for j in list:
            print(f(i+1)+j)
j=n
for i in range(n+1):
    if j==0:
        print('라고 답변하였지.')
    else:
        print(f(j+1)+'라고 답변하였지.')
    j-=1