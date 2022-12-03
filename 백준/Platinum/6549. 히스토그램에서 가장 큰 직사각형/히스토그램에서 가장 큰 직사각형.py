import sys
input=sys.stdin.readline

while 1:
    high : list[int] = list(map(int,input().split()))
    if high == [0]: break
    N : int = high.pop(0)

    stack : list = []
    result : list[int] = []

    # 넓이가 측정되는 시점 >자신보다 낮은 높이의 히스토그램이 등장할 때
    for i in range(N):
        while stack:
            if stack[-1][1]>high[i]:
                P = stack.pop()
                result.append((i-P[0])*P[1])
            else: break
        # 스택에는 높이[i]가 가장 먼저 히스토그램이 등장하는 인덱스,높이,인덱스를 푸쉬
        # 스택의 크기가 0이라면 지금까지 현재 인덱스의 히스토그램의 높이가 가장 작은 것이므로 가장 먼저 등장하는 인덱스를 0으로 푸쉬해 준다
        if len(stack)==0: stack.append([0,high[i],i])
        # 스택에 크기가 0이 아니라면 스택 가장 위의 히스토그램보다 크다는 뜻이므로 스택[-1]의 인덱스+1로 푸쉬해 준다
        else: stack.append([stack[-1][2]+1,high[i],i])

    #스택에 남아있는 값들은 마지막까지 작은 값이 나오지 않았다는 뜻이므로 비교인덱스를 N으로 설정하여 다 빼준다
    while stack:
        P = stack.pop()
        result.append((N-P[0])*P[1])

    print(max(result))