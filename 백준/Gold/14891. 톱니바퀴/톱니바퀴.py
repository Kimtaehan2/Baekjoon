import sys
from collections import deque
input=sys.stdin.readline

def spin_clockwise(gear):
    deque.appendleft(gear,gear.pop())
def spin_counter(gear):
    gear.append(deque.popleft(gear))

# N극은 0 S극은 1
def check_score(gear1,gear2,gear3,gear4):
    score=0
    if gear1[0]==0: pass
    if gear1[0]==1: score+=1
    if gear2[0]==0: pass
    if gear2[0]==1: score+=2
    if gear3[0]==0: pass
    if gear3[0]==1: score+=4
    if gear4[0]==0: pass
    if gear4[0]==1: score+=8
    return score

# N극은 0 S극은 1
# 1 시계 -1 반시계
def spin(gearnum,diretion):
    # 1번 톱니바퀴를 돌릴 때
    if gearnum==1:
        # 시계 방향일 때
        if diretion==1:
            # 옆 톱니바퀴와 극이 같을 때
            if gear1[2]==gear2[6]: spin_clockwise(gear1)
            # 옆 톱니바퀴와 극이 다를 때    
            elif gear1[2]!=gear2[6]:
                # 톱니바퀴 회전
                spin_clockwise(gear1)
                # 옆 톱니바퀴와 극이 같을 때
                if gear2[2]==gear3[6]: spin_counter(gear2)
                # 옆 톱니바퀴와 극이 다를 때
                elif gear2[2]!=gear3[6]:
                    # 톱니바퀴 회전
                    spin_counter(gear2)
                    # 옆 톱니바퀴와 극이 같을 때
                    if gear3[2]==gear4[6]: spin_clockwise(gear3)
                    # 옆 톱니바퀴와 극이 다를 때
                    elif gear3[2]!=gear4[6]:
                        spin_clockwise(gear3)
                        spin_counter(gear4)


        # 반시계 방향일 때
        elif diretion==-1:
            # 옆 톱니바퀴와 극이 같을 때
            if gear1[2]==gear2[6]: spin_counter(gear1)
            # 옆 톱니바퀴와 극이 다를 때    
            elif gear1[2]!=gear2[6]:
                # 톱니바퀴 회전
                spin_counter(gear1)
                # 옆 톱니바퀴와 극이 같을 때
                if gear2[2]==gear3[6]: spin_clockwise(gear2)
                # 옆 톱니바퀴와 극이 다를 때
                elif gear2[2]!=gear3[6]:
                    # 톱니바퀴 회전
                    spin_clockwise(gear2)
                    # 옆 톱니바퀴와 극이 같을 때
                    if gear3[2]==gear4[6]: spin_counter(gear3)
                    # 옆 톱니바퀴와 극이 다를 때
                    elif gear3[2]!=gear4[6]:
                        spin_counter(gear3)
                        spin_clockwise(gear4)
    
    # 2번 톱니바퀴를 돌릴 때
    if gearnum==2:
        # 시계 방향일 때
        if diretion==1:
            
            # 옆 톱니바퀴와 극이 같을 때
            if gear2[6]==gear1[2] and gear2[2]==gear3[6]: 
                spin_clockwise(gear2)
                
            elif gear2[6]!=gear1[2] and gear2[2]==gear3[6]:
                spin_clockwise(gear2)
                spin_counter(gear1)

            elif gear2[6]==gear1[2] and gear2[2]!=gear3[6]:
                spin_clockwise(gear2)
                if gear3[2]==gear4[6]: 
                    spin_counter(gear3)
                else:
                    spin_counter(gear3)
                    spin_clockwise(gear4)

            elif gear2[6]!=gear1[2] and gear2[2]!=gear3[6]:
                spin_clockwise(gear2)
                spin_counter(gear1)
                if gear3[2]==gear4[6]: 
                    spin_counter(gear3)
                else:
                    spin_counter(gear3)
                    spin_clockwise(gear4)

        # 반시계 방향일 때
        elif diretion==-1:
            
            # 옆 톱니바퀴와 극이 같을 때
            if gear2[6]==gear1[2] and gear2[2]==gear3[6]: 
                spin_counter(gear2)
                
            elif gear2[6]!=gear1[2] and gear2[2]==gear3[6]:
                spin_counter(gear2)
                spin_clockwise(gear1)

            elif gear2[6]==gear1[2] and gear2[2]!=gear3[6]:
                spin_counter(gear2)
                if gear3[2]==gear4[6]: 
                    spin_clockwise(gear3)
                else:
                    spin_clockwise(gear3)
                    spin_counter(gear4)

            elif gear2[6]!=gear1[2] and gear2[2]!=gear3[6]:
                spin_counter(gear2)
                spin_clockwise(gear1)
                if gear3[2]==gear4[6]: 
                    spin_clockwise(gear3)
                else:
                    spin_clockwise(gear3)
                    spin_counter(gear4)

    # 3번 톱니바퀴를 돌릴 때
    if gearnum==3:
        # 시계 방향일 때
        if diretion==1:
            
            # 옆 톱니바퀴와 극이 같을 때
            if gear3[6]==gear2[2] and gear3[2]==gear4[6]: 
                spin_clockwise(gear3)

            elif gear3[6]!=gear2[2] and gear3[2]==gear4[6]:
                spin_clockwise(gear3)
                if gear2[6]==gear1[2]:
                    spin_counter(gear2)
                else:
                    spin_counter(gear2)
                    spin_clockwise(gear1)

            elif gear3[6]==gear2[2] and gear3[2]!=gear4[6]:
                spin_clockwise(gear3)
                spin_counter(gear4)

            elif gear3[6]!=gear2[2] and gear3[2]!=gear4[6]:
                spin_clockwise(gear3)
                spin_counter(gear4)
                if gear2[6]==gear1[2]:
                    spin_counter(gear2)
                else:
                    spin_counter(gear2)
                    spin_clockwise(gear1)



        # 반시계 방향일 때
        elif diretion==-1:
            
            # 옆 톱니바퀴와 극이 같을 때
            if gear3[6]==gear2[2] and gear3[2]==gear4[6]: 
                spin_counter(gear3)

            elif gear3[6]!=gear2[2] and gear3[2]==gear4[6]:
                spin_counter(gear3)
                if gear2[6]==gear1[2]:
                    spin_clockwise(gear2)
                else:
                    spin_clockwise(gear2)
                    spin_counter(gear1)

            elif gear3[6]==gear2[2] and gear3[2]!=gear4[6]:
                spin_counter(gear3)
                spin_clockwise(gear4)

            elif gear3[6]!=gear2[2] and gear3[2]!=gear4[6]:
                spin_counter(gear3)
                spin_clockwise(gear4)
                if gear2[6]==gear1[2]:
                    spin_clockwise(gear2)
                else:
                    spin_clockwise(gear2)
                    spin_counter(gear1)
                
    # 4번 톱니바퀴를 돌릴 때
    if gearnum==4:
        if diretion==1:
            
            # 옆 톱니바퀴와 극이 같을 때
            if gear4[6]==gear3[2]: spin_clockwise(gear4)
            # 옆 톱니바퀴와 극이 다를 때    
            elif gear4[6]!=gear3[2]:
                # 톱니바퀴 회전
                spin_clockwise(gear4)
                
                # 옆 톱니바퀴와 극이 같을 때
                if gear3[6]==gear2[2]: spin_counter(gear3)
                # 옆 톱니바퀴와 극이 다를 때
                elif gear3[6]!=gear2[2]:
                    # 톱니바퀴 회전
                    spin_counter(gear3)
                    
                    # 옆 톱니바퀴와 극이 같을 때
                    if gear2[6]==gear1[2]: spin_clockwise(gear2)
                    # 옆 톱니바퀴와 극이 다를 때
                    elif gear2[6]!=gear1[2]:
                        spin_clockwise(gear2)
                        spin_counter(gear1)
            
        elif diretion==-1:
            
            # 옆 톱니바퀴와 극이 같을 때
            if gear4[6]==gear3[2]: spin_counter(gear4)
            # 옆 톱니바퀴와 극이 다를 때    
            elif gear4[6]!=gear3[2]:
                # 톱니바퀴 회전
                spin_counter(gear4)
                # 옆 톱니바퀴와 극이 같을 때
                if gear3[6]==gear2[2]: spin_clockwise(gear3)
                # 옆 톱니바퀴와 극이 다를 때
                elif gear3[6]!=gear2[2]:
                    # 톱니바퀴 회전
                    spin_clockwise(gear3)
                    # 옆 톱니바퀴와 극이 같을 때
                    if gear2[6]==gear1[2]: spin_counter(gear2)
                    # 옆 톱니바퀴와 극이 다를 때
                    elif gear2[6]!=gear1[2]:
                        spin_counter(gear2)
                        spin_clockwise(gear1)



gear1=deque(list(map(int,input().strip())))
gear2=deque(list(map(int,input().strip())))
gear3=deque(list(map(int,input().strip())))
gear4=deque(list(map(int,input().strip())))

K=int(input())
for i in range(K):
    gearnum, diretion=map(int,input().split())
    spin(gearnum,diretion)

print(check_score(gear1,gear2,gear3,gear4))

