import sys
def check(cmd):
    global index_stone
    global index_king
    #돌이 킹 바로 왼쪽, L
    if index_stone==[index_king[0]-1,index_king[1]] and cmd=='L':
        if index_stone[0]==1: return 0
        else: 
            index_stone[0]-=1
            return 1
    #돌이 킹 바로 오른쪽, R
    elif index_stone==[index_king[0]+1,index_king[1]] and cmd=='R':
        if index_stone[0]==8: return 0
        else:
            index_stone[0]+=1
            return 1
    #돌이 킹 바로 아래, B
    elif index_stone==[index_king[0],index_king[1]-1] and cmd=='B':
        if index_stone[1]==1: return 0
        else:
            index_stone[1]-=1
            return 1
    #돌이 킹 바로 위, T
    elif index_stone==[index_king[0],index_king[1]+1] and cmd=='T':
        if index_stone[1]==8: return 0
        else: 
            index_stone[1]+=1
            return 1
    #돌이 킹 바로 왼쪽 아래, LB
    elif index_stone==[index_king[0]-1,index_king[1]-1] and cmd=='LB':
        if index_stone[0]==1 or index_stone[1]==1: return 0
        else:
            index_stone[0]-=1
            index_stone[1]-=1
            return 1
    #돌이 킹 바로 왼쪽 위, LT
    elif index_stone==[index_king[0]-1,index_king[1]+1] and cmd=='LT':
        if index_stone[0]==1 or index_stone[1]==8: return 0
        else:
            index_stone[0]-=1
            index_stone[1]+=1
            return 1 
    #돌이 킹 바로 오른쪽 아래, RB
    elif index_stone==[index_king[0]+1,index_king[1]-1] and cmd=='RB':
        if index_stone[0]==8 or index_stone[1]==1: return 0
        else: 
            index_stone[0]+=1
            index_stone[1]-=1
            return 1
    #돌이 킹 바로 오른쪽 위, RT
    elif index_stone==[index_king[0]+1,index_king[1]+1] and cmd=='RT':
        if index_stone[0]==8 or index_stone[1]==8: return 0
        else:
            index_stone[0]+=1
            index_stone[1]+=1
            return 1
    else: return 1

kingl,stonel,n=list(sys.stdin.readline().split())
temp='ABCDEFGH'
index_king=[temp.index(kingl[0])+1,int(kingl[1])]
index_stone=[temp.index(stonel[0])+1,int(stonel[1])]


for i in range(int(n)):
    cmd=sys.stdin.readline().strip()
    if cmd=='R':
        #킹이 맨 오른쪽 일때 확인
        if index_king[0]==8: pass
        else:
            if check(cmd)==0: pass
            else: index_king[0]+=1
    if cmd=='L':
        #킹이 맨 왼쪽 일때 확인
        if index_king[0]==1: pass
        else:
            if check(cmd)==0: pass
            else: index_king[0]-=1
    if cmd=='B':
        #킹이 맨 아래 일때 확인
        if index_king[1]==1: pass
        else:
            if check(cmd)==0: pass
            else: index_king[1]-=1
    if cmd=='T':
        #킹이 맨 위 일때 확인
        if index_king[1]==8: pass
        else:
            if check(cmd)==0: pass
            else:
                index_king[1]+=1
    if cmd=='RB':
        #킹이 오른쪽 끝과 아래쪽 끝 일때 확인
        if index_king[0]==8 or index_king[1]==1: pass
        else:
            if check(cmd)==0: pass
            else:
                index_king[0]+=1
                index_king[1]-=1
    if cmd=='RT':
        #킹이 오른쪽 끝과 위쪽 끝 일때 확인
        if index_king[0]==8 or index_king[1]==8: pass
        else:
            if check(cmd)==0: pass
            else:
                index_king[0]+=1
                index_king[1]+=1
    if cmd=='LB':
        #킹이 제일 왼쪽 과 제일 아래 일때 확인
        if index_king[0]==1 or index_king[1]==1: pass
        else:
            if check(cmd)==0: pass
            else:
                index_king[0]-=1
                index_king[1]-=1
    if cmd=='LT':
        #킹이 제일 왼쪽 과 제일 위 일때 확인
        if index_king[0]==1 or index_king[1]==8: pass
        else:
            if check(cmd)==0: pass
            else:
                index_king[0]-=1
                index_king[1]+=1

print(temp[index_king[0]-1],index_king[1],sep='')
print(temp[index_stone[0]-1],index_stone[1],sep='')