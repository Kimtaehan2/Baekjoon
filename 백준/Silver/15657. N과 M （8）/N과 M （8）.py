import sys
input=sys.stdin.readline
sys.setrecursionlimit(10**6)
N,M=map(int,input().split())
arr=list(map(int,input().split()))
arr.sort()
visited=[0]*N
stack=[]

# 백트래킹 알고리즘 구현
def bt(m,d):
    # 깊이가 최대 방문에 도달했다면 배열을 출력해 준다
    if d==m: 
        print(*stack)
        # 함수를 종료해 줘야 시간초과가 나지 않는다
        return
    for i in range(N):
       # 만약 스택에 아무것도 들어있지 않거나 (방문이 m번 이하고 전의 수가 비내림차순이라면)
        if len(stack)==0 or (visited[i]<=m and stack[-1]<=arr[i]):
            # 최대 방문은 m번까지이므로 visited가 m이 될때까지 스택에 추가 해 준다
            visited[i]+=1
            stack.append(arr[i])
            # 백트래킹 함수를 호출 해 줄때마다 깊이+1 을 해 준다
            bt(m,d+1)
            # 다른 것도 탐색할 수 있도록 stack을 pop 해 주고 i의 방문을 -1 해준다
            stack.pop()
            visited[i]-=1
bt(M,0)