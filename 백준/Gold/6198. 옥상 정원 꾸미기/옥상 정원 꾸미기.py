import sys
input=sys.stdin.readline
n : int = int(input())
high : list[int] = [int(input()) for i in range(n)]
stack : list[int] = []
count : list[int] = [0]*n

# 1. 현재 탐색 중인 건물이 스택 가장 위의 건물보다 높을 때 스택에서 인덱스를 꺼내 (현재 건물 인덱스 - 스택 인덱스) 로 count를 파악
# 2. 탐색한 건물의 인덱스는 스택에 넣음
for i in range(n):
    while stack:
        if high[stack[-1]]<=high[i]:
            count[stack[-1]]=i-stack[-1]-1
            stack.pop()
        else: break
    stack.append(i)

# 3. 모든 건물 탐색이 끝나면 건물 개수를 기준으로 스택에서 모두 제거 해 줌
while stack:
    count[stack[-1]]=n-stack[-1]-1
    stack.pop()

print(sum(count))