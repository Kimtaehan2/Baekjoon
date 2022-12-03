N=int(input())

friend=[]

for i in range(N):
    friend.append(list(input()))

friend_copy=[[0]*N for i in range(N)]

for i in range(N):
    for j in range(N):
            for k in range(N):
                if j==i: continue
                if friend[i][j]=='Y' or (friend[i][k]=='Y' and friend[k][j]=='Y'):
                    friend_copy[i][j]=1
                    
friend_count=[]

for i in friend_copy:
    count=0
    for j in range(N):
        count+=i[j]
    friend_count.append(count)

print(max(friend_count))