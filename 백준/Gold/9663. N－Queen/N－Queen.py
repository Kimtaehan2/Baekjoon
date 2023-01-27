import sys
input = sys.stdin.readline

N = int(input())

X = [0]*N

# 세로 - 가로 + N
diagonal_x = [0]*(2*N-1)
# 가로 - 세로 + N
diagonal_y = [0]*(2*N-1)

result = 0

def back_tracking(y):
    global result
    if y == N:
        result += 1
        return
    
    for x in range(N):
        if X[x] == 0 and diagonal_x[y-x+N-1] == 0 and diagonal_y[x+y] == 0:
            X[x] = 1
            diagonal_x[y-x+N-1] = 1
            diagonal_y[x+y] = 1
            back_tracking(y+1)
            X[x] = 0
            diagonal_x[y-x+N-1] = 0
            diagonal_y[x+y] = 0

back_tracking(0)
print(result)