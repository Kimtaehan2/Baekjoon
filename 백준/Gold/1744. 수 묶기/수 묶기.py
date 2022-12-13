import sys
import heapq
input = sys.stdin.readline

N = int(input())

que = []
for i in range(N):
    heapq.heappush(que,int(input()))

result = []

A = 1
B = 1

check_A = True
check_B = True

while len(que)>=2:
    if check_A:
        A = heapq.heappop(que)
    if check_B:
        B = heapq.heappop(que)
    check_A = True
    check_B = True

    if A<0 and B==0:
        result.append(A*B)
    elif A==0 or B==0:
        result.append(A+B)
    elif A<0 and B>0:
        check_B = False
        result.append(A)
    elif A>0 and B>0:
        if len(que)%2 == 0:
            if A*B < A+B:
                result.append(A+B)
            else: result.append(A*B)
        else:
            MIN = min(A,B)
            result.append(MIN)
            if MIN == A:
                check_B = False
            else: check_A = False
    else:
        result.append(A*B)

if len(que) == 0:
    if not check_A:
        result.append(A)
    elif not check_B:
        result.append(B)

elif len(que) > 0:
    if not check_A:
        B = que.pop()
    elif not check_B:
        A = que.pop()
    else:
        A = 1
        B = que.pop()
    result.append(A*B)

print(sum(result))