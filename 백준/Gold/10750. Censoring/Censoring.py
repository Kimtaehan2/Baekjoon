import sys
input=sys.stdin.readline

word=list(map(str,input().rstrip()))
boom=list(map(str,input().rstrip()))
#스택 초기화
stack=[]
#word가 없어질 때 까지 돌려줌
for i in word:
    stack.append(i)
    #리스트 슬라이싱으로 스택의 가장 위쪽에서부터 폭발 문자열의 길이만큼 비교해줌
    #만약 같다면 삭제
    if stack[-len(boom):]==boom:
        del(stack[-len(boom):])

print(''.join(stack))
#문자열 폭발로 날먹하기