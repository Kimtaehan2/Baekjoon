import sys

n=int(input())
l=set()
for i in range(n):
    order=sys.stdin.readline().split()
    if len(order)==1:
        if order[0]=='all':
            l=set(i for i in range(1,21))
        else:
            l=set()

    else:
        m,k=order[0],int(order[1])

        if m=='add':
            l.add(k)
        elif m=='remove':
            if k in l:
                l.discard(k)
        elif m=='check':
            if k in l: print(1)
            else: print(0)
        else:
            if k in l:
                l.discard(k)
            else:
                l.add(k)
#시간초과 해결을 위해 else 처리를 많이 함