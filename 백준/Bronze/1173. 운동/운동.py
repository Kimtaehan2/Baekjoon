import sys

N,m,M,T,R=map(int,sys.stdin.readline().split())
X=m
time=0
ex_time=0

if M-m<T: 
    print(-1)
else: 
    while ex_time!=N:
        #휴식
        if X+T>M:
            X-=R
            if X<m: X=m
        #운동
        else : 
            ex_time+=1
            X+=T
        time+=1
    print(time)