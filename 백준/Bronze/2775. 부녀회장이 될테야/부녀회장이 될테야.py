import sys

T=int(input())

def dp(n,k):
    if n==0:
        return floor[0][k]
    
    for i in range(1,n+1):
        room=[]
        for j in range(k):
            if j==0: room.append(1)
            else:
                room.append(room[j-1]+floor[i-1][j])
        floor.append(room)
    return floor[n][k-1]
        
result=[]
for i in range(T):
    n=int(sys.stdin.readline())
    k=int(sys.stdin.readline())
    floor=[[i for i in range(1,k+1)]]
    result.append(str(dp(n,k)))

print('\n'.join(result))