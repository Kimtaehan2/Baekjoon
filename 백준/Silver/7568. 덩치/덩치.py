N=int(input())
bulk=[]
for i in range(N):
    bulk.append(list(map(int,input().split())))

bulk_count=[]
for i in range(N):
    count=0
    for j in range(N):
        if bulk[i][0]<bulk[j][0] and bulk[i][1]<bulk[j][1]:
            count+=1
    bulk_count.append(str(count+1))
print(" ".join(bulk_count))