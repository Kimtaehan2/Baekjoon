import sys
input=sys.stdin.readline

N = int(input())
arr = list(map(int,input().split()))
stack = []
check = [0]*N
result = []
def BT(depth):
  if depth==N:
    S=0
    for i in range(N-1):
      S+=abs(stack[i]-stack[i+1])
    result.append(S)
    return

  for i in range(N):
    if check[i]==0:
      stack.append(arr[i])
      check[i]=1
      BT(depth+1)
      check[i]=0
      stack.pop()

BT(0)
print(max(result))