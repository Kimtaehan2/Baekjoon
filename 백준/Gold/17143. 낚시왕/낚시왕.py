import sys
input = sys.stdin.readline

R,C,M = map(int,input().split())

def move(r,c,s,d,z,i):
    move_point = 0
    # 이동 방향이 '위' 일때
    # 위에서 시작할 때에는 맨 아래를 기준으로
    if d == 1:
        distance = s + (R - r) # 속도 + 현재 위치

        if s == 0:
            return [r,c,s,d,z,i]
        elif distance % (R-1) == 0:
            check = (distance-1) // (R-1)
        else:
            check = distance // (R-1)

        if check % 2 != 0: # 방향이 바뀔 때
            d = 2
            move_point = distance % (R-1)
            if move_point == 0:
                move_point = R-1
            r = move_point + 1
        else:
            move_point = distance % (R-1)
            if move_point == 0:
                move_point = R-1
            r = R - move_point
        
        # 이동 방향이 '아래' 일때
        # 아래에서 시작할 때에는 맨 위를 기준으로
    elif d == 2:
        distance = s + r - 1
        
        if s == 0:
            return [r,c,s,d,z,i]
        elif distance % (R-1) == 0:
            check = (distance-1) // (R-1)
        else:
            check = distance // (R-1)

        if check % 2 != 0:
            d = 1
            move_point = distance % (R-1)
            if move_point == 0:
                move_point = R-1
            r = R - move_point
        else:
            move_point = distance % (R-1)
            if move_point == 0:
                move_point = R-1
            r = move_point + 1

        # 이동 방향이 '오른쪽' 일때
        # 오른쪽에서 시작할 때에는 맨 왼쪽을 기준으로
    elif d == 3:
        distance = s + c - 1
        check = distance // (C-1)

        if s == 0:
            return [r,c,s,d,z,i]
        elif distance % (C-1) == 0:
            check = (distance-1) // (C-1)
        else:
            check = distance // (C-1)

        if check % 2 != 0:
            d = 4
            move_point = distance % (C-1)
            if move_point == 0:
                move_point = C-1
            c = C - move_point
        else:
            move_point = distance % (C-1)
            if move_point == 0:
                move_point = C-1
            c = move_point + 1
        
        # 이동 방향이 '왼쪽' 일때
        # 왼쪽에서 시작할 때에는 맨 오른쪽을 기준으로
    elif d == 4:
        distance = s + (C - c)
        
        if s == 0:
            return [r,c,s,d,z,i]
        elif distance % (C-1) == 0:
            check = (distance-1) // (C-1)
        else:
            check = distance // (C-1)
        
        if check % 2 != 0:
            d = 3
            move_point = distance % (C-1)
            if move_point == 0:
                move_point = C-1
            c = move_point + 1
        else:
            move_point = distance % (C-1)
            if move_point == 0:
                move_point = C-1
            c = C - move_point
    return [r,c,s,d,z,i]

shark = []
map1 = [[[] for i in range(C)] for i in range(R)]
map2 = [[[] for i in range(C)] for i in range(R)]
for idx in range(M):
    r,c,s,d,z = map(int,input().split())
    if d == 1 or d == 2:
        s = s%(2*R-2)
    else:
        s = s%(2*C-2)
    map1[r-1][c-1].append([r,c,s,d,z,idx])
    shark.append([r,c,s,d,z,idx])

def move_in_map():
    global movecnt
    if movecnt % 2 == 0:
        for i in range(M):
            if shark[i] == 0:
                continue
            map2[shark[i][0]-1][shark[i][1]-1].clear()
            new = move(shark[i][0],shark[i][1],shark[i][2],shark[i][3],shark[i][4],shark[i][5])
            shark[new[5]] = [new[0],new[1],new[2],new[3],new[4],new[5]]

            

            if len(map1[new[0]-1][new[1]-1]) == 0:
                map1[new[0]-1][new[1]-1].append([new[0],new[1],new[2],new[3],new[4],new[5]])
            else:
                # 기존의 상어보다 더 클때
                if map1[new[0]-1][new[1]-1][0][4] < new[4]:
                    # 기존의 상어 삭제
                    shark[map1[new[0]-1][new[1]-1][0][5]] = 0
                    map1[new[0]-1][new[1]-1][0] = [new[0],new[1],new[2],new[3],new[4],new[5]]

                # 기존의 상어가 더 클때 
                else:
                    # 현재 상어 삭제
                    shark[i] = 0
    else:
        for i in range(M):
            if shark[i] == 0:
                continue
            map1[shark[i][0]-1][shark[i][1]-1].clear()
            new = move(shark[i][0],shark[i][1],shark[i][2],shark[i][3],shark[i][4],shark[i][5])
            shark[new[5]] = [new[0],new[1],new[2],new[3],new[4],new[5]]

            if len(map2[new[0]-1][new[1]-1]) == 0:
                map2[new[0]-1][new[1]-1].append([new[0],new[1],new[2],new[3],new[4],new[5]])
            else:
                # 기존의 상어보다 더 클때
                if map2[new[0]-1][new[1]-1][0][4] < new[4]:
                    # 기존의 상어 삭제
                    shark[map2[new[0]-1][new[1]-1][0][5]] = 0
                    map2[new[0]-1][new[1]-1][0] = [new[0],new[1],new[2],new[3],new[4],new[5]]

                # 기존의 상어가 더 클때 
                else:
                    # 현재 상어 삭제
                    shark[i] = 0


# 최대 1000000번의 연산
def fishing():
    global movecnt,score
    if movecnt % 2 == 0:
        for i in range(R):
            if len(map2[i][movecnt-1]) == 1:
                score += map2[i][movecnt-1][0][4]
                shark[map2[i][movecnt-1][0][5]] = 0
                map2[i][movecnt-1].clear()
                return
    else:
        for i in range(R):
            if len(map1[i][movecnt-1]) == 1:
                score += map1[i][movecnt-1][0][4]
                shark[map1[i][movecnt-1][0][5]] = 0
                map1[i][movecnt-1].clear()
                return
        

score = 0
for movecnt in range(1,C+1):
    fishing()
    move_in_map()


print(score)