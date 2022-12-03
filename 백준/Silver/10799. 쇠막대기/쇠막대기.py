import sys

word=sys.stdin.readline().strip()
#문자열 replace, sep, split등을 활용해보았다

stick=list(word.replace('()','r'))

#처음 조각 수 저장
split=stick.count(')')

# count를 추가해서 오른쪽부터 팝 하며 만약 ')' 나오면 count+1 '('가 나오면 count-1
# 'r' 이 나온다면 count를 result에 추가
result=[]
count=0
for i in range(len(stick)):
    judge=stick.pop()
    if judge==')':
        count+=1
    elif judge=='(':
        count-=1
    else: 
        if count==0: pass
        else: result.append(count)

#자른 횟수 + 처음 조각 수
print(sum(result)+split)