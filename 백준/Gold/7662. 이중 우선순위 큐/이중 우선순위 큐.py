import sys
import heapq
input = sys.stdin.readline

T = int(input())
for i in range(T):
    Q_min = []
    Q_max = []
    hashset = set()
    k = int(input())

    for i in range(k):

        last = len(hashset)
        cmd1,cmd2 = input().split()
        if cmd1 == 'I':
            heapq.heappush(Q_min,[int(cmd2),i])
            heapq.heappush(Q_max,[-int(cmd2),i])
        elif cmd1 == 'D':
            if cmd2 == '-1':
                while last == len(hashset):
                    try: 
                        hashset.add(heapq.heappop(Q_min)[1])
                    except:
                        break
            elif cmd2 == '1':
                while last == len(hashset):
                    try:
                        hashset.add((heapq.heappop(Q_max)[1]))
                    except:
                        break

    

    if len(Q_min) == 0 or len(Q_max) == 0:
        print('EMPTY')
    else:
        C = 0
        last = len(hashset)
        while last == len(hashset):
            try: 
                A,x = heapq.heappop(Q_min)
                hashset.add(x)
            except:
                C = 1
                break
        if C == 0:
            hashset.remove(x)
        while last == len(hashset):
            try:
                B,y = heapq.heappop(Q_max)
                hashset.add(y)
            except:
                C = 1
                break
        try:
            if C == 1:
                print('EMPTY')
            else: print(-B,A)
        except:
            print('EMPTY')
