import sys
input=sys.stdin.readline

N = int(input())
arr = list(map(int,input().split()))
check = list(map(int,input().split()))
stack = []
operater = ['+','-','*','/']
result = set()
def BT(depth):
  global last
  if depth==N-1:
    S=arr[0]
    for i in range(N-1):
      if stack[i]=='+':
        S+=arr[i+1]
      if stack[i]=='-':
        S-=arr[i+1]
      if stack[i]=='*':
        S*=arr[i+1]
      if stack[i]=='/':
        if S<0 and arr[i+1]>=0:
          S=-(abs(S)//arr[i+1])
        else: S//=arr[i+1]
    result.add(S)
    return
  for j in range(len(operater)):
    if check[j]>0:
      check[j]-=1
      stack.append(operater[j])
      BT(depth+1)
      stack.pop()
      check[j]+=1

BT(0)
print(max(result),min(result),sep='\n')