import sys
import copy
input=sys.stdin.readline

N = int(input())

RBY = [int(input()) for i in range(N)]

check = []
result = []

def RBYboom(RBY): # 4개 이상 합쳐진 공을 삭제하여 남은 공의 개수를 반환하는 함수
    stack = []
    while RBY:
        if len(stack)>0 and stack[-1][0]==RBY[-1]:
            stack.append([RBY.pop(),stack[-1][1]+1])
        else:
            if len(stack)>0 and stack[-1][1]>=4:
                del stack[-stack[-1][1]:]
            else:
                stack.append([RBY.pop(),1])
    if len(stack)>0 and stack[-1][1]>=4:
        del stack[-stack[-1][1]:]
    return len(stack)

# 공의 색을 바꾸었을 때 RBY 팡이 일어날 가능성이 있을 공의 위치, 바꿀 공의 색을 check에 저장
for i in range(N-3):
    # 1 x 1 1
    if RBY[i]==RBY[i+2] and RBY[i+2]==RBY[i+3] and RBY[i+1]!=RBY[i]:
        check.append([i+1,RBY[i]])
    # x 1 1 1
    elif RBY[i+1]==RBY[i+2] and RBY[i+2]==RBY[i+3] and RBY[i+1]!=RBY[i]:
        check.append([i,RBY[i+1]])
    # 1 1 x 1
    elif RBY[i]==RBY[i+1] and RBY[i+1]==RBY[i+3] and RBY[i+2]!=RBY[i]:
        check.append([i+2,RBY[i+1]])
    # 1 1 1 x
    elif RBY[i]==RBY[i+1] and RBY[i+1]==RBY[i+2] and RBY[i+3]!=RBY[i]:
        check.append([i+3,RBY[i+1]])

# deepcopy를 이용하여 check에 있는 공을 바꾸어서 RBYboom 함수에 넣어 보고 리턴값을 result에 저장 후
# 다시 초기 RBY 값으로 바꾸어 준다
for i in range(len(check)):
    start = RBY[check[i][0]]
    RBY[check[i][0]]=check[i][1]
    result.append(RBYboom(copy.deepcopy(RBY)))
    RBY[check[i][0]]=start


if len(result)==0: # 이것 때문에 런타임 에러 남 항상 예외를 생각하자
    if len(RBY)==4 and RBY[i]==RBY[i+1] and RBY[i+1]==RBY[i+2] and RBY[i+2]==RBY[i+3]:
        print(0)
    else: print(len(RBY))

else: print(min(result))