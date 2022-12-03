import sys
input=sys.stdin.readline

n=int(input())
meeting=[0]*n
for i in range(n):
    start,end=map(int,input().split())
    meeting[i]=[start,end,end-start]
meeting.sort()

count=1
for i in range(n-1):
    #이전 회의가 끝나는 시간이 다음 회의가 끝나는 시간보다 늦으면 
    if meeting[i][1]>meeting[i+1][1]: pass
    #이전 회의가 끝나는 시간이 다음 회의가 시작되는 시간보다 빠르면
    elif meeting[i][1]<=meeting[i+1][1]: 
        # 이전 회의의 끝 시간이 다음 회의의 시작 시간이랑 같거나 빠르면
        if meeting[i][1]<=meeting[i+1][0]: count+=1
        else: meeting[i+1]=meeting[i]
print(count)