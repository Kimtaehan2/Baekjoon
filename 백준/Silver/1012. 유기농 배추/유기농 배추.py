import sys
input=sys.stdin.readline

T=int(input())

for _ in range(T):
    M,N,K=map(int,input().split())
    baechu=[[0 for i in range(M)] for i in range(N)]
    graph=[[[] for i in range(M)] for i in range(N)]
    hashset=set()
    count=0
    vetor_x,vetor_y=[],[]
    for _ in range(K):
        x,y=list(map(int,input().split()))
        baechu[y][x]=1
        vetor_x.append(x)
        vetor_y.append(y)
    for i in range(K):
        vx,vy=vetor_x[i],vetor_y[i]
        
        if vx-1>=0 and baechu[vy][vx-1]==1:
            graph[vy][vx].append((vy,vx-1))
            graph[vy][vx-1].append((vy,vx))
        if vx+1<M and baechu[vy][vx+1]==1:
            graph[vy][vx].append((vy,vx+1))
            graph[vy][vx+1].append((vy,vx))
        if vy-1>=0 and baechu[vy-1][vx]==1:
            graph[vy][vx].append((vy-1,vx))
            graph[vy-1][vx].append((vy,vx))
        if vy+1<N and baechu[vy+1][vx]==1:
            graph[vy][vx].append((vy+1,vx))
            graph[vy+1][vx].append((vy,vx))
            
        if vx-1>=0 and baechu[vy][vx-1]==0 and vx+1<M and baechu[vy][vx+1]==0 and vy-1>=0 and baechu[vy-1][vx]==0 and vy+1<N and baechu[vy+1][vx]==0:
            graph[vy][vx].append((vy,vx))
            graph[vy][vx].append((vy,vx))
        
        if vx-1>=0 and baechu[vy][vx-1]==0 and vx+1>=M and vy-1>=0 and baechu[vy-1][vx]==0 and vy+1<N and baechu[vy+1][vx]==0:
            graph[vy][vx].append((vy,vx))
            graph[vy][vx].append((vy,vx))
        if vx-1<0 and vx+1<M and baechu[vy][vx+1]==0 and vy-1>=0 and baechu[vy-1][vx]==0 and vy+1<N and baechu[vy+1][vx]==0:
            graph[vy][vx].append((vy,vx))
            graph[vy][vx].append((vy,vx))
        if vx-1>=0 and baechu[vy][vx-1]==0 and vx+1<M and baechu[vy][vx+1]==0 and vy-1<0 and vy+1<N and baechu[vy+1][vx]==0:
            graph[vy][vx].append((vy,vx))
            graph[vy][vx].append((vy,vx))
        if vx-1>=0 and baechu[vy][vx-1]==0 and vx+1<M and baechu[vy][vx+1]==0 and vy-1>=0 and baechu[vy-1][vx]==0 and vy+1>=N:
            graph[vy][vx].append((vy,vx))
            graph[vy][vx].append((vy,vx))

        if vx-1<0 and vx+1<M and baechu[vy][vx+1]==0 and vy-1>=0 and baechu[vy-1][vx]==0 and vy+1>=N:
            graph[vy][vx].append((vy,vx))
            graph[vy][vx].append((vy,vx))
        if vx-1<0 and vx+1<M and baechu[vy][vx+1]==0 and vy-1<0 and vy+1<N and baechu[vy+1][vx]==0:
            graph[vy][vx].append((vy,vx))
            graph[vy][vx].append((vy,vx))
        if vx-1>=0 and baechu[vy][vx-1]==0 and vx+1>=M and vy-1>=0 and baechu[vy-1][vx]==0 and vy+1>=N:
            graph[vy][vx].append((vy,vx))
            graph[vy][vx].append((vy,vx))
        if vx-1>=0 and baechu[vy][vx-1]==0 and vx+1>=M and vy-1<0 and vy+1<N and baechu[vy+1][vx]==0:
            graph[vy][vx].append((vy,vx))
            graph[vy][vx].append((vy,vx))

    for i in range(N):
        for j in range(M):
            lastlen=len(hashset)
            while graph[i][j]:
                p=graph[i][j].pop()
                if p==(i,j): 
                    hashset.add(p)
                    pass
                else: 
                    while graph[p[0]][p[1]]:
                        q=graph[p[0]][p[1]].pop()
                        graph[i][j].append(q)
                        hashset.add(q)
            if len(hashset)!=lastlen: count+=1
    print(count)