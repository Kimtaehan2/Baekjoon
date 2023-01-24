import sys
input = sys.stdin.readline

N = int(input())

def bottom_up():
    dp_table = [[0,[1]],[1,[1,2]],[1,[1,3]]]
    if N == 1:
        print(dp_table[0][0])
        print(*dp_table[0][1][::-1])
        return
    elif N == 2:
        print(dp_table[1][0])
        print(*dp_table[1][1][::-1])
        return
    elif N == 3:
        print(dp_table[2][0])
        print(*dp_table[2][1][::-1])
        return
    
    for i in range(3,N):
        result = []
        # 3으로 나누어 떨어질 때
        if (i+1)%3 == 0:
            result.append([dp_table[(i+1)//3-1][0],(i+1)//3])
        # 2로 나누어 떨어질 때
        if (i+1)%2 == 0:
            result.append([dp_table[(i+1)//2-1][0],(i+1)//2])
        # 1을 뺄 때
        result.append([dp_table[i-1][0],i])
        dp_table.append([min(result)[0]+1,dp_table[min(result)[1]-1][1]+[i+1]])

    print(dp_table[-1][0])
    print(*dp_table[-1][1][::-1])

bottom_up()