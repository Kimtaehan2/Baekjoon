import sys
input=sys.stdin.readline

word=list(map(str,input().rstrip()))
boom=list(map(str,input().rstrip()))
#스택 초기화
stack=[]
#word가 없어질 때 까지 돌려줌
while word:
    #리스트 슬라이싱으로 스택의 가장 위쪽에서부터 폭발 문자열의 길이만큼 비교해줌
    #만약 같다면 삭제
    if stack[-len(boom):]==boom[::-1]:
        del(stack[-len(boom):])
    #다르다면 word를 팝 하여 스택에 푸쉬
    else:
        stack.append(word.pop())
#마지막으로 스택 확인
if stack[-len(boom):]==boom[::-1]:
    del(stack[-len(boom):])

if len(stack)==0: print('FRULA')
else: print(*stack[::-1],*word[::-1],sep='')