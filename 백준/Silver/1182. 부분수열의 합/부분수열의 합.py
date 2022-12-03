import sys
input=sys.stdin.readline

N,S = map(int,input().split())
arr = list(map(int,input().split()))
count = 0
def BT(depth,SUM):
  global count

  if depth==N: return
  SUM+=arr[depth]
  if SUM==S:
    count+=1
  BT(depth+1,SUM-arr[depth])
  BT(depth+1,SUM)
    

BT(0,0)
print(count)