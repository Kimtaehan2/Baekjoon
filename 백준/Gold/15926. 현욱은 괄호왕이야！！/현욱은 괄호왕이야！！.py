import sys
input=sys.stdin.readline

N : int = int(input())

word : list[str] = list(input().strip())

word_and_index = []

for i in range(N):
    word_and_index.append([word[i],i])

stack : list[str] = []
count : int = [0]*N

id=N-1
while word_and_index:
    p=word_and_index.pop()
    if len(stack)!=0 and stack[-1][0]==')' and p[0]=='(':
        count[stack.pop()[1]]=1
        count[p[1]]=1
    else:
        stack.append(p)

result=[]
cnt=0
for i in range(len(count)):
    if count[i]==0:
        result.append(cnt)
        cnt=0
    else: 
        cnt+=1
result.append(cnt)
print(max(result))